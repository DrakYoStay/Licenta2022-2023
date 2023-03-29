import cv2 as cv
import numpy as np
import time
import control_motor
import RPi.GPIO as GPIO
from time import sleep

cap = cv.VideoCapture(0)
lower_hsv = np.array([28,47,47])
high_hsv = np.array([43,255,255])
camera_center = 150
center = (0,0)

while True:
    ret, image = cap.read()
    time.sleep(1/30)
    if image is not None:
        image = cv.resize(image,(300,300))
        image_blurred = cv.GaussianBlur(image,(17,17),0)

        imageHSV = cv.cvtColor(image_blurred,cv.COLOR_BGR2HSV)


        thresh = cv.inRange(imageHSV,lower_hsv,high_hsv)
        thresh = cv.erode(thresh ,None , iterations=5)
        thresh = cv.dilate(thresh ,None , iterations=5)
        x_camera, _ = center
        contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        if len(contours) == 0:
            print("INTRU AICI")
            control_motor.stop()

        for contour in contours:
            (x, y), radius = cv.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            cv.circle(image, center, radius, (0, 255, 0), 2)
            cv.circle(image,center,radius=2,color=(255,0,0),thickness=2)
            if x_camera >= camera_center - 20 and x_camera <= camera_center + 20:
                print("Mergi in fata")
                control_motor.forward(50)
            elif x_camera < camera_center - 20:
                print("Fa stanga")
                control_motor.left(50)
            elif x_camera > camera_center + 20:
                print("Fa dreapta")
                control_motor.right(50)
            break

        # cv.imshow("kek", image)
        cv.imshow("kek", thresh)



        if cv.waitKey(10) & 0xFF == ord('q'):
            control_motor.stop()
            GPIO.cleanup()
            break
    else:
        print("Image is none")
        break

image.release()
cv.destroyAllWindows()

