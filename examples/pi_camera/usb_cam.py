from time import sleep
import numpy as np
import cv2 as cv


def list_ports():
    """
    Test the ports and returns a tuple with the available ports and the ones that are working.
    """
    non_working_ports = []
    dev_port = 0
    working_ports = []
    available_ports = []
    while len(non_working_ports) < 5: # if there are more than 5 non working ports stop the testing. 
        camera = cv.VideoCapture(dev_port)
        if not camera.isOpened():
            non_working_ports.append(dev_port)
            print("Port %s is not working." %dev_port)
        else:
            is_reading, img = camera.read()
            w = camera.get(3)
            h = camera.get(4)
            if is_reading:
                print("Port %s is working and reads images (%s x %s)" %(dev_port,h,w))
                working_ports.append(dev_port)
            else:
                print("Port %s for camera ( %s x %s) is present but does not reads." %(dev_port,h,w))
                available_ports.append(dev_port)
        dev_port +=1
    return available_ports,working_ports,non_working_ports


if __name__ == "__main__":

    ports, working, not_working = list_ports()

    print(ports)
    print(working)
    print(not_working)

    # caps = [cv.VideoCapture(port) for port in working]

    # cam_one = caps[0]
    # cam_two = caps[1]

    while True:
        cam_one = cv.VideoCapture(working[0])
        ret_one, frame_one = cam_one.read()
        if not ret_one:
            print("Cam one error")
            break 
        # cv.imshow("CAM_ONE", frame_one)
        cam_one.release()

        cam_two = cv.VideoCapture(working[1])
        ret_two, frame_two = cam_two.read()
        if not ret_two:
            print("cam two error")
            break
        # cv.imshow("CAM_TWO", frame_two)

        cam_two.release()
        
        v1 = frame_one[50:140, 140:330]

        cv.imshow("VIAL ONE", v1)


        if cv.waitKey(1) == ord('q'):
            break

    # cap = cv.VideoCapture(2)
    # cap2 = cv.VideoCapture(0)

    # if not cap.isOpened():
    #     print("Cannot open camera")
    #     exit()

    cam_one.release()
    cam_two.release()
    cv.destroyAllWindows()



# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     ret2, frame2 = cap2.read()

#     # if frame is read correctly ret is True
#     if not ret:
#         print("Cam 1 err")
#         break

#     if not ret2:
#         print("Cam 2 err")
#         break
#     # Our operations on the frame come here
#     # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv.imshow('frame', frame)
#     cv.imshow('frame', frame2)

#     if cv.waitKey(1) == ord('q'):
#         break
# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()
