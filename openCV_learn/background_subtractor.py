import cv2

cap = cv2.VideoCapture('./videos/motionVideo.mp4')
# fgbg =cv2.bgsegm.createBackgroundSubtractorMOG()
# fgbg =cv2.createBackgroundSubtractorMOG2()
# fgbg = cv2.bgsegm.createBackgroundSubtractorCNT()
# fgbg = cv2.bgsegm.createBackgroundSubtractorLSBP()
# fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
fgbg = cv2.createBackgroundSubtractorKNN()
while cap.isOpened():
    _,frame = cap.read()
    if not _:
        break
    fgframe = fgbg.apply(frame)

    cv2.imshow('frmae',fgframe)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()