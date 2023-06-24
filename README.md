# Object detection using EvaDB (YOLO)
[Eva DB](#https://github.com/georgia-tech-db/eva)

## Quick Start

- Footage recorded by DonkeyCar:

```shell
python yolo-object-detection.py ati_footage.mp4
```

- Traffic video:

```shell
python yolo-object-detection.py traffic.mp4
```


## Results

- **DonkeyCar video**

```
preethn@preethn-mac object-detection-evadb %python yolo-object-detection.py ati_footage.mp4
Could not find image processor class in the image processor config or the model config. Loading based on pattern matching with the model's feature extractor configuration.
                                                   0
0  Table Successfully dropped: ObjectDetectionVideos
                           0
0  Number of loaded VIDEO: 1
                                         0
0  UDF Yolo already exists, nothing added.
2023-06-25 02:44:31,003 INFO worker.py:1625 -- Started a local Ray instance.
    objectdetectionvideos.id  ...                     yolo.scores
0                          0  ...   [0.78, 0.7, 0.59, 0.35, 0.33]
1                          1  ...  [0.77, 0.77, 0.48, 0.39, 0.32]
2                          2  ...  [0.78, 0.73, 0.56, 0.42, 0.34]
3                          3  ...   [0.79, 0.71, 0.47, 0.4, 0.33]
4                          4  ...        [0.79, 0.69, 0.45, 0.34]
5                          5  ...  [0.79, 0.74, 0.54, 0.33, 0.31]
6                          6  ...   [0.8, 0.74, 0.58, 0.35, 0.32]
7                          7  ...   [0.8, 0.77, 0.56, 0.33, 0.31]
8                          8  ...        [0.81, 0.81, 0.51, 0.31]
9                          9  ...   [0.82, 0.81, 0.47, 0.33, 0.3]
10                        10  ...        [0.82, 0.82, 0.44, 0.32]
11                        11  ...        [0.83, 0.82, 0.49, 0.32]
12                        12  ...        [0.84, 0.82, 0.57, 0.32]
13                        13  ...        [0.83, 0.82, 0.52, 0.33]
14                        14  ...        [0.84, 0.82, 0.54, 0.33]
15                        15  ...        [0.84, 0.82, 0.51, 0.32]
16                        16  ...              [0.84, 0.82, 0.53]
17                        17  ...              [0.84, 0.82, 0.51]
18                        18  ...        [0.84, 0.83, 0.52, 0.31]
19                        19  ...        [0.85, 0.83, 0.58, 0.34]

[20 rows x 4 columns]
```
![atipicop](https://github.com/Preethi1609/object-detection-evadb/assets/80187583/7aea1f9e-c977-48d3-86da-7ec39b6bd55c)

- **Traffic video**
```
preethn@preethn-mac object-detection-evadb %python yolo-object-detection.py traffic.mp4    
Could not find image processor class in the image processor config or the model config. Loading based on pattern matching with the model's feature extractor configuration.
                                                   0
0  Table Successfully dropped: ObjectDetectionVideos
                           0
0  Number of loaded VIDEO: 1
                                         0
0  UDF Yolo already exists, nothing added.
2023-06-25 02:47:47,604 INFO worker.py:1625 -- Started a local Ray instance.
    objectdetectionvideos.id  ...                                        yolo.scores
0                          0  ...  [0.87, 0.84, 0.78, 0.74, 0.68, 0.68, 0.6, 0.53...
1                          1  ...  [0.88, 0.87, 0.78, 0.73, 0.67, 0.67, 0.66, 0.5...
2                          2  ...  [0.88, 0.87, 0.78, 0.73, 0.67, 0.67, 0.65, 0.5...
3                          3  ...  [0.88, 0.88, 0.75, 0.71, 0.68, 0.65, 0.63, 0.6...
4                          4  ...  [0.89, 0.88, 0.82, 0.73, 0.66, 0.66, 0.62, 0.6...
5                          5  ...  [0.89, 0.87, 0.8, 0.73, 0.72, 0.69, 0.63, 0.6,...
6                          6  ...  [0.9, 0.87, 0.82, 0.73, 0.71, 0.71, 0.67, 0.57...
7                          7  ...  [0.91, 0.89, 0.8, 0.73, 0.71, 0.7, 0.69, 0.69,...
8                          8  ...  [0.9, 0.89, 0.79, 0.73, 0.69, 0.68, 0.64, 0.62...
9                          9  ...  [0.91, 0.9, 0.78, 0.7, 0.69, 0.69, 0.69, 0.68,...
10                        10  ...  [0.91, 0.89, 0.82, 0.73, 0.73, 0.72, 0.71, 0.6...
11                        11  ...  [0.92, 0.88, 0.81, 0.77, 0.76, 0.76, 0.71, 0.7...
12                        12  ...  [0.91, 0.88, 0.82, 0.73, 0.71, 0.71, 0.7, 0.7,...
13                        13  ...  [0.91, 0.88, 0.85, 0.73, 0.72, 0.71, 0.71, 0.6...
14                        14  ...  [0.91, 0.87, 0.84, 0.75, 0.74, 0.72, 0.71, 0.6...
15                        15  ...  [0.92, 0.88, 0.83, 0.76, 0.74, 0.72, 0.71, 0.6...
16                        16  ...  [0.91, 0.88, 0.85, 0.74, 0.73, 0.72, 0.72, 0.7...
17                        17  ...  [0.92, 0.88, 0.84, 0.74, 0.7, 0.69, 0.68, 0.67...
18                        18  ...  [0.92, 0.88, 0.83, 0.74, 0.7, 0.69, 0.64, 0.63...
19                        19  ...  [0.91, 0.88, 0.85, 0.73, 0.73, 0.7, 0.68, 0.56...

[20 rows x 4 columns]
```
![WhatsApp Image 2023-06-25 at 3 19 13 AM (1)](https://github.com/Preethi1609/object-detection-evadb/assets/80187583/f165c5ae-7d58-4064-94a1-443a257d8610)

## License
Copyright (c) 2018-present [Georgia Tech Database Group](http://db.cc.gatech.edu/).
Licensed under [Apache License](LICENSE).
