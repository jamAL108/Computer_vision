import cv2
import numpy as np
import matplotlib.pyplot as plt


def process(img,vertices):
    mask = np.zeros_like(img)
    # for colorful image
    # channel_count = img.shape[2]
    # masked_colors = (255,) * channel_count

    # if using grayscale then avoid taking img.shape[2] values
    # directly put masked_colors = 255
    masked_colors = 255

    cv2.fillPoly(mask,vertices,masked_colors)
    masked_output = cv2.bitwise_and(img,mask)
    return masked_output


# image = cv2.imread('./images/road.jpg')

def roadlane(img):
     height = img.shape[0]
     width = img.shape[1]

     region_of_interest = [
         (0,height),
         (width/2,height/2),
         (width,height)
     ]

     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     canny = cv2.Canny(gray,100,200)
     ROI_image = process(canny,np.array([region_of_interest],np.int32))
     lines = cv2.HoughLinesP(ROI_image, 6, np.pi/60, 200 ,np.array([]), minLineLength=50, maxLineGap=4)
     for line in lines:
          x1,y1,x2,y2 = line[0]
          cv2.line(img,(x1,y1),(x2,y2),(0,255,0),7)
     return img

cap = cv2.VideoCapture('./videos/road_lane.mp4')

while(cap.isOpened()):
    _,frame = cap.read()
    if not _:
        break
    frame = roadlane(frame)
    cv2.imshow('image',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

