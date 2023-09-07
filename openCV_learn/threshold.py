import cv2

messi = cv2.imread('./images/messi.jpg',0)

_,thressy = cv2.threshold(cv2.resize(messi,(640,520)),127,255,cv2.THRESH_BINARY)
resize_messi = cv2.resize(messi,(640,520))
Adapthressy = cv2.adaptiveThreshold(resize_messi,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11,2)
cv2.imshow('thressy',thressy)
cv2.imshow('thre',Adapthressy)
cv2.waitKey(0)
cv2.destroyAllWindows()
