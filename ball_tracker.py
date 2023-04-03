import cv2 as cv
import numpy as np
import time
import control_motor

CONTROLLER = control_motor.Motoare()
CONTROLLER.__init__()
CONTROLLER.stop()
cap = cv.VideoCapture(0)
lower_hsv = np.array([28,47,47])
high_hsv = np.array([43,255,255])
camera_center = 150
center = (0,0)
time.sleep(2)

while True:
    ret, image = cap.read()
    time.sleep(1/60)
    if image is not None:
        image = cv.resize(image,(300,300))
        image_blurred = cv.GaussianBlur(image,(11,11),0)

        imageHSV = cv.cvtColor(image_blurred,cv.COLOR_BGR2HSV)


        thresh = cv.inRange(imageHSV,lower_hsv,high_hsv)
        thresh = cv.erode(thresh ,None , iterations=2)
        thresh = cv.dilate(thresh ,None , iterations=2)
        x_camera, _ = center
        contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        if len(contours) == 0:
            CONTROLLER.stop()

        for contour in contours:
            (x, y), radius = cv.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            cv.circle(image_blurred, center, radius, (0, 255, 0), 2)
            cv.circle(image_blurred,center,radius=2,color=(255,0,0),thickness=2)
            if x_camera >= camera_center - 70 and x_camera <= camera_center + 70:
                print("Mergi in fata")
                CONTROLLER.inainte()
            elif x_camera < camera_center - 70:
                print("Fa stanga")
                CONTROLLER.stanga()
            elif x_camera > camera_center + 70:
                print("Fa dreapta")
                CONTROLLER.dreapta()
            break


        print(x_camera)
        cv.imshow("kek", image_blurred)
        #cv.imshow("kek", thresh)



        if cv.waitKey(10) & 0xFF == ord('q'):
            CONTROLLER.stop()
            break
    else:
        print("Image is none")
        break


image.release()
cv.destroyAllWindows()