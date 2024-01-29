from ultralytics import YOLO

# loading the model
model = YOLO("yolov8s-cls.pt")

# using the model
model.train(data='/home/thor_x_me/PycharmProjects/DMS/data/',
            epochs=50, imgsz=64)
