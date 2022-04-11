import numpy as np
import cv2 as cv
cap = cv.VideoCapture(2)
cap2 = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Cam 1 err")
        break

    if not ret2:
        print("Cam 2 err")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', frame)
    cv.imshow('frame', frame2)
    
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()