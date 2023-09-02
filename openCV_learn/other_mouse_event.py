import numpy as np
import cv2
import os

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event,x,y,flag,params):
    print(x, ' ', y)
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        NewImage = np.zeros((512,512,3),np.uint8)
        NewImage[:] = [red,green,blue]
        strs = str(blue) + "," + str(green) + "," + str(red)
        cv2.putText(NewImage,strs,(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        cv2.imshow('tempimage',NewImage)
    cv2.imshow('image',img)
img = cv2.imread('chill.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()