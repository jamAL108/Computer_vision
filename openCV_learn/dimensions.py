import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    if not ret:
        break
    x1, y1 = 100, 50
    x2, y2 = 300, 200
    color = (0, 255, 0)  # Green
    # Draw the rectangle
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness=2)
    cv2.putText(frame,"Hello world", (x1+6, y2+30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('frame',frame)
    delay_time = int(1000 / 60)
    if cv2.waitKey(delay_time) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()