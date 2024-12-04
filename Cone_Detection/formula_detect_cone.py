from ultralytics import YOLO
import cv2

#Yolov8 model after training
model = YOLO("Model_training/runs/detect/train/weights/best.pt")  # Replace with the path to your .pt file

#Video to analyse
video_path = "fsd1.mp4"  # Replace with the path to your video file
cap = cv2.VideoCapture(video_path)

#Video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Saving the output
output_path = "output_video.mp4"  # Output video file
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec for saving the video
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Process the video frame by frame
while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    annotated_frame = results[0].plot()
    out.write(annotated_frame)
    cv2.imshow("YOLOv8 Inference", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Output video saved at: {output_path}")