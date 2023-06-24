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
                cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color1, thickness)
                # frame label
                cv2.putText(frame, 'Frame ID: ' + str(frame_id), (700, 500), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color2, thickness)
            video.write(frame)

            # Stop after twenty frames (id < 20 in previous query)
            if frame_id == 20:
                break

            # Show every fifth frame
            if frame_id % 5 == 0:
                plt.imshow(frame)
                plt.show()


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
      yolo_query = yolo_query.filter("id < 20")
      yolo_query = yolo_query.select("id, Yolo(data)")

      response = yolo_query.df()
      print(response)

      input_path = 'videos/' + video_file
      output_path = 'videos/output_' + video_file

      annotate_video(response, input_path, output_path)
      Video.from_file(output_path)

if __name__ == '__main__' :
    main()