import torch
from ultralytics import YOLO

def train_yolo():
    # Load the YOLOv8 model
    device_use = 'cpu'
    model = YOLO("yolov8n.pt")
    if torch.cuda.is_available(): # Checks to see if the user has Cuda/NVDA Gpu
        device_use = 0

    # Train the model on your dataset
    model.train(
        data=r"D:\Programming\BGracing\Cone_Detection\Model_training\cone_detection_img\data.yaml",  # Path to your dataset YAML file
        epochs=20,                 
        imgsz=640,                 
        batch=16,                 
        device=device_use                 
    )

if __name__ == '__main__':
    train_yolo()
