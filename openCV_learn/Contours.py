# Used to detect the boundaries of objects in a image
import cv2
messi = cv2.imread('./images/insta.jpg')
messi = cv2.resize(messi,(620,500))
messi_gray = cv2.cvtColor(messi,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(messi_gray,(5,5),0)
cv2.imshow('G',blur)

ret, thres = cv2.threshold(messi_gray,127,255,0)

Adapthressy = cv2.adaptiveThreshold(messi_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11,2)

contours , heirarchy = cv2.findContours(Adapthressy,cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE)
print('The Number of Contours are :' + str(len(contours)))

# Draw Contours
# print(contours[0])
cv2.drawContours(messi,contours,-1,(255,255,0),2)


cv2.imshow('messi',Adapthressy)
cv2.imshow('OG',messi)
cv2.waitKey(0)
cv2.destroyAllWindows()
