import cv2
import numpy as np
image = cv2.imread('./images/sudoku.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray,50,150,apertureSize=3)
Lines = cv2.HoughLines(canny,1,np.pi/180,200)
# 1: This is the resolution of the accumulator in pixels.
# In this case, it's set to 1, which means that the accumulator has the same resolution as the input image.
# np.pi/180: This parameter represents the angle resolution of the accumulator in radians.
# np.pi/180 converts degrees to radians,
# so this value means that the accumulator will consider angles from 0 to 180 degrees.
for line in Lines:
    rho , thetha = line[0]
    a = np.cos(thetha)
    b = np.sin(thetha)
    # a = np.cos(thetha) and  b = np.sin(thetha) are used to find the direction of line

    x0 = a*rho
    y0 = b*rho
    # x0 = a * rho and y0 = b * rho are used to get the closest point frmo the origin (0,0)

    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    # To calculate the endpoints (x1, y1) and (x2, y2) of the line,
    # extend the line in both directions by a length of 1000 units.
    # This is a common practice to ensure that the line spans the entire width of the image or a region of interest.
    # The negative signs in 1000*(-b) and 1000*(a) ensure that the line extends in both directions along
    # x1 and y1 represent one endpoint of the line,
    # which is 1000 units away from x0 and y0 in the direction of the normal vector.
    # x2 and y2 represent the other endpoint of the line,
    # which is 1000 units away from x0 and y0 in the opposite direction of the normal vector.

    cv2.line(image, (x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


