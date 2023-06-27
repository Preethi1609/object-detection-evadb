# Object detection using EvaDB (YOLO)
[Eva DB](https://github.com/georgia-tech-db/eva)

## Quick Start

- Traffic lights video processing:

```shell
python yolo-object-detection.py traffic_light.mp4
```


## Results

- **Traffic lights video**
```
preethn@preethn-mac object-detection-evadb %python yolo-object-detection.py traffic_light.mp4
                                                   0
0  Table Successfully dropped: ObjectDetectionVideos
                           0
0  Number of loaded VIDEO: 1
                                         0
0  UDF Yolo already exists, nothing added.
2023-06-25 15:49:41,732 INFO worker.py:1625 -- Started a local Ray instance.
    objectdetectionvideos.id      yolo.labels                                        yolo.bboxes yolo.scores
0                          0  [traffic light]  [[116.49211883544922, 43.250511169433594, 207....      [0.91]
1                          1  [traffic light]  [[116.31712341308594, 45.00706481933594, 208.1...       [0.9]
2                          2  [traffic light]  [[116.3758544921875, 44.99008560180664, 208.14...       [0.9]
3                          3  [traffic light]  [[116.33740997314453, 44.998966217041016, 208....       [0.9]
4                          4  [traffic light]  [[116.35423278808594, 44.991519927978516, 208....       [0.9]
..                       ...              ...                                                ...         ...
95                        95  [traffic light]  [[118.98309326171875, 44.38285446166992, 209.3...      [0.89]
96                        96  [traffic light]  [[118.82341766357422, 44.14023208618164, 209.3...      [0.89]
97                        97  [traffic light]  [[118.77188873291016, 44.094810485839844, 209....      [0.89]
98                        98  [traffic light]  [[118.9520263671875, 43.920711517333984, 209.2...      [0.89]
99                        99  [traffic light]  [[118.96548461914062, 43.9997444152832, 209.29...      [0.89]

[100 rows x 4 columns]
```

# [CLICK HERE FOR VIDEO RESULTS](https://drive.google.com/file/d/1RsUQzldYsdCq8vzcg3HFP-_pCxb-BeAI/view?usp=sharing)
![Screenshot (430)](https://github.com/Preethi1609/object-detection-evadb/assets/80187583/6efcd8b0-cf3a-42c3-b13e-03d977b36c72)
![Screenshot (431)](https://github.com/Preethi1609/object-detection-evadb/assets/80187583/023b979b-9a72-4acb-920a-dfacb8222739)



## References
[Eva DB Object Detection Tutorial](https://colab.research.google.com/github/georgia-tech-db/eva/blob/master/tutorials/02-object-detection.ipynb)
