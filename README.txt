Hello, my name is Asaf Avitov and this is my Task for BGRacing.
I did Task number 3 in the autonomous branch, I have used many sources as it was my first time learning on how to use AI models and such, 
some of the sources were Youtube/StackOverflow/ultralytics website/chatgpt and more...

1. I have used a dataset from the specified website - Roboflow and this is the link:

	https://universe.roboflow.com/formula-student-driverless-arece-3/cone-detection-bldji/dataset/6

2.I have used VScode and using python 3.10 I have imported a couple of libraries such as - opencv, torch, ultralytics.
torch - for model training using Cuda cores on NVDA GPU.
ultralytics - for the use of YOLOv8 AI model.
opencv - in order to use the trained model I had to use some of the functions in this library.

3.My resume will be in the google drive link together with the Cone_Detection folder.

4. ----------------------------------HOW TO USE(Instructions)----------------------------------

			

	1.download "Cone_Detection" folder from this google drive link:
		https://drive.google.com/drive/folders/1yfqE6f_0iqB7Im-WtPeLQQtbMz42otEh?usp=sharing

	2.open the terminal inside your IDE/cmd and write the following commands in order to install the neccessary libraries:
		pip install ultralytics
		pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
		pip install opencv-python

	3.open the 'Model_training' folder and run the 'model_training.py' file, this will run AI model on the IMG's and train the model for him to learn how to distinguish
	the cones and color of cones.
	
	4.after it finishes training the model, enter the main folder and run the 'formula_detect_cone.py' file, you will then see a new mp4 video appearing in the folder
	named 'output_video', run it and you will see the end result.


