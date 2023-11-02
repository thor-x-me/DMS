from ultralytics import YOLO
import cv2
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 680)
cap.set(4,420)

model = YOLO('../Yolo-Weights/yolov8n.pt')

while True:
    ret, frame = cap.read()
    result = model(frame, stream=True)

    for r in result:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            print(x1, y1, x2, y2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,255),1)

    cv2.imshow('frame', frame)
    cv2.waitKey(1)
