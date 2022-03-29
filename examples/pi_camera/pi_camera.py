from pickletools import read_uint2
import numpy as np
import cv2 as cv
import time

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 160)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 120)

frame_rate = 10
prev = 0
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    t = time.time() - prev
    # Capture frame-by-frame
    # if frame is read correctly ret is True
    # Our operations on the frame come here
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    if t > 1/frame_rate:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv.imshow('frame', frame)
        prev = time.time()

    if cv.waitKey(1) == ord('q'):
        break

    
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()