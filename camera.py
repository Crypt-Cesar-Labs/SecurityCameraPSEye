import cv2
import numpy as np

cap = cv2.VideoCapture(2)

while(True):
    ret, frame = cap.read()

    if not ret:
        break

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
