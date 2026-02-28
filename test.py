from ultralytics import YOLO

model = YOLO("models/best.pt")

results = model("test_image.jpg", show=True, conf=0.1)
