import numpy as np
import cv2
import os

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event,x,y,flag,params):
    print(x, ' ', y)
    if event == cv2.EVENT_LBUTTONDOWN:
        strXY = str(x) + ',' + str(y)
        cv2.putText(img,strXY,(x,y),cv2.FONT_HERSHEY_COMPLEX,.4,(255, 255, 0),2)
    elif event== cv2.EVENT_RBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        strs = str(red) + "," + str(green) + "," + str(blue)
        cv2.putText(img, strs, (x, y), cv2.FONT_HERSHEY_COMPLEX,.4,(255, 255, 0),2)
    cv2.imshow('image',img)
img = cv2.imread('chill.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)