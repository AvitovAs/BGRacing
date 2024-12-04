
# BGRacing Entry Assignment
Hello, this is my entry assignment for BGRacing, I did task number 3.  
The assignment mentions using AI to detect the cones and their color for a moving vehicle.  




## Installation
In order to use my project you must install 2 libraries,OpenCV and ultralytics, you can use the terminal in either the IDE or CMD and run the following lines:  
```
    pip install ultralytics
    pip install opencv-python
```    
If you would like to use my model_trainer file than you would need also need to install the torch library with following line:  
```
    pip3 install torch
```
The torch library can use your Cuda cores on an NVIDIA GPU and makes it train the model more efficiently and faster.

## How to Use

After downloading the repository just open the 'formula_detection_cone.py' file and run it.  
it will use the already trained dataset included in the files and run the  video.  


## Acknowledgements
About the project:  
I have used the YOLOv8 AI model from the ultralytics library using this dataset from Roboflow:  
[Cone dataset](https://universe.roboflow.com/formula-student-driverless-arece-3/cone-detection-bldji/dataset/6)

As this was my first time learning the subject I have used alot of sources.  
Mentions: Youtube, StackOverflow, Chatgpt and etc...  
