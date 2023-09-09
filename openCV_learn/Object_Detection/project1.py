import cv2
from ultralytics import YOLO
import numpy as np

model= YOLO('./yolo-models/yolov8l.pt')
result = model('./images/kids1.jpg',show=True)
cv2.waitKey(0)