import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mpv4')
out = cv2.VideoWriter('write_video.mp4',fourcc,30.0,(640, 480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame',frame)
    out.write(frame)
    delay_time = int(1000 / 60)
    if cv2.waitKey(delay_time) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()