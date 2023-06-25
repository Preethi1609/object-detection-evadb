import evadb
import sys
import cv2
from pprint import pprint
from matplotlib import pyplot as plt
from ipywidgets import Video, Image


def annotate_video(detections, input_video_path, output_video_path):
    color1=(207, 248, 64)
    color2=(255, 49, 49)
    thickness=4

    vcap = cv2.VideoCapture(input_video_path)
    width = int(vcap.get(3))
    height = int(vcap.get(4))
    fps = vcap.get(5)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') #codec
    video=cv2.VideoWriter(output_video_path, fourcc, fps, (width,height))

    frame_id = 0
    # Capture frame-by-frame
    # ret = 1 if the video is captured; frame is the image
    ret, frame = vcap.read()

    while ret:
        df = detections
        df = df[['yolo.bboxes', 'yolo.labels']][df.index == frame_id]
        if df.size:
            dfLst = df.values.tolist()
            for bbox, label in zip(dfLst[0][0], dfLst[0][1]):
                x1, y1, x2, y2 = bbox
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                # object bbox
                frame=cv2.rectangle(frame, (x1, y1), (x2, y2), color1, thickness)
                # object label
                if label == "traffic light":
                    lower_red = (0, 50, 50)
                    upper_red = (10, 255, 255)
                    hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    mask = cv2.inRange(hsv_roi, lower_red, upper_red)
                    red_pixel_count = cv2.countNonZero(mask)
                    threshold = 800
                    if red_pixel_count > threshold:
                        cv2.putText(frame, "TRAFFIC LIGHT RED, STOP!", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color1, thickness)
                    else:
                        cv2.putText(frame, "TRAFFIC LIGHT RED, GO!", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color1, thickness)
                else:
                    cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color1, thickness)
                # frame label
                cv2.putText(frame, 'Frame ID: ' + str(frame_id), (700, 500), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color2, thickness)
            video.write(frame)

            if frame_id == 100:
                break

        frame_id+=1
        ret, frame = vcap.read()

    video.release()
    vcap.release()

def main():
      cursor = evadb.connect().cursor()

      response = cursor.query("DROP TABLE IF EXISTS ObjectDetectionVideos;").df()
      print(response)

      video_file = sys.argv[1]
      input_path = './videos/' + video_file
      response = cursor.load(input_path, table_name="ObjectDetectionVideos", format="VIDEO").df()
      print(response)

      response = cursor.query("""
                              CREATE UDF IF NOT EXISTS Yolo
                              TYPE  ultralytics
                              'model' 'yolov8m.pt';
                              """).df()
      print(response)

      yolo_query = cursor.table("ObjectDetectionVideos")
      yolo_query = yolo_query.filter("id < 100")
      yolo_query = yolo_query.select("id, Yolo(data)")

      response = yolo_query.df()
      print(response)

      input_path = 'videos/' + video_file
      output_path = 'videos/output_' + video_file

      annotate_video(response, input_path, output_path)
      Video.from_file(output_path)

if __name__ == '__main__' :
    main()