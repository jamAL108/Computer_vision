import cv2
cap = cv2.VideoCapture('./videos/motionVideo.mp4')
#cap = cv2.VideoCapture(0)
_, frame1 = cap.read()
_, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _, thres = cv2.threshold(blur,20,255,0)
    dilate = cv2.dilate(thres,None,iterations=5)
    contours,_ = cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cont in contours:
        (x,y,w,h) = cv2.boundingRect(cont)

        if cv2.contourArea(cont) < 700:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
    #cv2.drawContours(frame1,contours,-1,(255,255,0),2)\

    cv2.imshow('img',frame1)
    frame1=frame2
    _,frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break
cv2.destroyAllWindows()
cap.release()