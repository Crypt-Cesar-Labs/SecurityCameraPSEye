import cv2
import numpy as np

cap = cv2.VideoCapture(2)
cap1 = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    ret1, frame1 = cap1.read()

    if not ret:
        break

    if not ret1:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    cv2.imshow('frame1', gray1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
