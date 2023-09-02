import cv2

cap = cv2.VideoCapture("nNotepreiew.mp4")

while(True):
    ret,frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame',frame)
    delay_time = int(1000 / 60)
    if cv2.waitKey(delay_time) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()