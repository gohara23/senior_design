import numpy as np
import cv2 as cv


def list_ports():
    is_working = True
    dev_port = 0
    working_ports = []
    available_ports = []
    while is_working:
        camera = cv.VideoCapture(dev_port)
        if not camera.isOpened():
            # is_working = False
            print("Port %s is not working." % dev_port)
        else:
            is_reading, img = camera.read()
            w = camera.get(3)
            h = camera.get(4)
            if is_reading:
                print("Port %s is working and reads images (%s x %s)" %
                        (dev_port, h, w))
                working_ports.append(dev_port)
            else:
                print("Port %s for camera ( %s x %s) is present but does not reads." % (
                    dev_port, h, w))
                available_ports.append(dev_port)
        dev_port += 1
        if dev_port > 25:
            break
    return available_ports, working_ports


if __name__ == "__main__":

    # ports, working = list_ports()

    # print(ports)
    # print(working)

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
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', frame)
    cv.imshow('frame', frame2)

    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
