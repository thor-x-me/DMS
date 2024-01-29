# Run this piece of code after train the model using train.py file

# importing libraries
from ultralytics import YOLO
import cv2


cap = cv2.VideoCapture(0)            # camera object
cap.set(3, 640)                      # setting width
cap.set(4, 500)                      # setting height

pt1 = (40, 40)                        # top-left point for drawing bounding box
pt2 = (600, 460)                        # bottom-right point for drawing bounding box
green = (0, 255, 0)                      # BGR value for Green colour
red = (0, 0, 255)                        # BGR value for Red colour


# loading the model
model = YOLO('/home/thor_x_me/PycharmProjects/DMS/runs/classify/train/weights/best.pt')  # load a custom model

while True:
    _, frame = cap.read()
    results = model(frame)  # predict on an image
    probs = results[0].probs.top1
    if probs == 1:
        cv2.rectangle(frame, pt1, pt2, color=red, thickness=10)    # drawing Red box
    elif probs == 0:
        cv2.rectangle(frame, pt1, pt2, color=green, thickness=10)    # drawing Green box
    else:
        pass
    print(probs)
    cv2.imshow('image1', frame)
    cv2.waitKey(1)
