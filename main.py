from ultralytics import YOLO
import cv2


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 500)

pt1 = (40, 40)
pt2 = (600, 460)
green = (0, 255, 0)
red = (0, 0, 255)


# loading the model
model = YOLO('/home/thor_x_me/PycharmProjects/DMS/runs/classify/train/weights/best.pt')  # load a custom model

while True:
    _, frame = cap.read()
    results = model(frame)  # predict on an image
    probs = results[0].probs.top1
    if probs == 1:
        cv2.rectangle(frame, pt1, pt2, color=red, thickness=10)
    elif probs == 0:
        cv2.rectangle(frame, pt1, pt2, color=green, thickness=10)
    else:
        pass
    print(probs)
    cv2.imshow('image1', frame)
    cv2.waitKey(1)
