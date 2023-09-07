import cv2
import numpy as np

image = cv2.imread('./images/road.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray,50,150,apertureSize=3)
lines = cv2.HoughLinesP(canny , 1 , np.pi/180 , 200 , minLineLength=100, maxLineGap=10)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

