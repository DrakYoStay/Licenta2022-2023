import cv2 as cv
import cv2.aruco as aruco
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
time.sleep(2)
SWITCH_STATE = False

GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_UP)
servo_pin = 18
pwm_freq = 50
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM object
pwm = GPIO.PWM(servo_pin, pwm_freq)
pwm.start(2)



while SWITCH_STATE == False:
    ret, image = cap.read()
    image = cv.flip(image,0)
    image = cv.flip(image,1)
    time.sleep(1/60)
    if image is not None:
        image = cv.resize(image,(300,300))
        image_blurred = cv.GaussianBlur(image,(17,17),0)

        imageHSV = cv.cvtColor(image_blurred,cv.COLOR_BGR2HSV)


        thresh = cv.inRange(imageHSV,lower_hsv,high_hsv)
        thresh = cv.erode(thresh ,None , iterations=2)
        thresh = cv.dilate(thresh ,None , iterations=2)
        x_camera, _ = center
        contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        if len(contours) == 0:
            print("INTRU AICI")
            control_motor.stop()
            if GPIO.input(16) == GPIO.LOW:
                control_motor.stop()
                SWITCH_STATE = True
                pwm.ChangeDutyCycle(12)
                print("180 degree")
                # Wait for a second
                time.sleep(5)
                
                # Move the servo motor to 180 degrees
                pwm.ChangeDutyCycle(2)
                print("0 degree")
                
        for contour in contours:
            (x, y), radius = cv.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            cv.circle(image, center, radius, (0, 255, 0), 2)
            cv.circle(image,center,radius=2,color=(255,0,0),thickness=2)
            if x_camera >= camera_center - 50 and x_camera <= camera_center + 50:
                print("Mergi in fata")
                control_motor.forward(40)
            elif x_camera < camera_center - 50:
                print("Fa stanga")
                control_motor.left(40)
            elif x_camera > camera_center + 50:
                print("Fa dreapta")
                control_motor.right(40)

            if GPIO.input(16) == GPIO.LOW:
                control_motor.stop()
                SWITCH_STATE = True
                pwm.ChangeDutyCycle(12)
                print("180 degree")
                # Wait for a second
                time.sleep(5)
                
                # Move the servo motor to 180 degrees
                pwm.ChangeDutyCycle(2)
                print("0 degree")


            break

        cv.imshow("kek", image)
        #cv.imshow("kek", thresh)



        if cv.waitKey(10) & 0xFF == ord('q'):
            control_motor.stop()
            break
    else:
        print("Image is none")
        break

if SWITCH_STATE == True:
    cap.release()
    cap = cv.VideoCapture(0)

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)
parameters = aruco.DetectorParameters_create()
parameters.adaptiveThreshConstant = 10
camera_center = 200
marker_size = 0.05
DROPPED_BALL = False

camera_matrix = np.array([[1000, 0, 500], [0, 1000, 500], [0, 0, 1]])
dist_coeffs = np.array([0, 0, 0, 0])
CICLU_CAUTARE = False

while SWITCH_STATE == True:
    ret, image = cap.read()
    image = cv.flip(image,0)
    image = cv.flip(image,1)
    time.sleep(1/60)
    if image is not None:
        image = cv.resize(image,(400,400))
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        if ids is not None:
            CICLU_CAUTARE = True
            # Draw the detected marker(s) and label them with their ID(s)
            aruco.drawDetectedMarkers(image, corners)
            for i, marker_id in enumerate(ids):
            # Calculate the distance to the marker
                if marker_id == 0 and DROPPED_BALL == False:
                    for i in range(len(ids)):
                        # Get the corner coordinates for this marker
                        marker_corners = corners[i][0]

                        # Calculate the center point of the marker
                        aruco_center = int(np.mean(marker_corners[:, 0]))
                    print(aruco_center)
                    rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners[i], marker_size, camera_matrix, dist_coeffs)
                    distance = np.linalg.norm(tvec)
                    label = 'ID: {}, Distance: {:.2f} meters'.format(marker_id, distance)
                    cv.putText(image, label, tuple(corners[i][0][0].astype(int)), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2, cv.LINE_AA)
                    if aruco_center >= camera_center - 100 and aruco_center <= camera_center + 100:
                        control_motor.forward(40)
                        if distance < 0.4:
                            print(distance)
                            control_motor.stop()
                            print("am ajuns unde trebuie")
                            #servoradarada
                            DROPPED_BALL = True
                            time.sleep(2)
                            control_motor.backward(40)
                            time.sleep(2)
                    elif aruco_center < camera_center - 100:
                        print("Fa stanga")
                        control_motor.left(40)
                    elif aruco_center > camera_center + 100:
                        print("Fa dreapta")
                        control_motor.right(40)
                elif marker_id == 1 and DROPPED_BALL == True:
                    for i in range(len(ids)):
                        # Get the corner coordinates for this marker
                        marker_corners = corners[i][0]

                        # Calculate the center point of the marker
                        aruco_center = int(np.mean(marker_corners[:, 0]))
                    print(aruco_center)
                    rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners[i], marker_size, camera_matrix, dist_coeffs)
                    distance = np.linalg.norm(tvec)
                    label = 'ID: {}, Distance: {:.2f} meters'.format(marker_id, distance)
                    cv.putText(image, label, tuple(corners[i][0][0].astype(int)), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2, cv.LINE_AA)
                    if aruco_center >= camera_center - 100 and aruco_center <= camera_center + 100:
                        control_motor.forward(40)
                        if distance < 0.4:
                            print(distance)
                            control_motor.stop()
                            print("am ajuns unde trebuie")
                            time.sleep(1)
                            print("ma sinucid")
                            GPIO.cleanup()                                                        
                            cap.release()
                            cv.destroyAllWindows()
                    elif aruco_center < camera_center - 100:
                        print("Fa stanga")
                        control_motor.left(40)
                    elif aruco_center > camera_center + 100:
                        print("Fa dreapta")
                        control_motor.right(40)
                        
                else:
                    control_motor.right(40)
        elif ids is None and CICLU_CAUTARE == False:
            control_motor.right(40)
            
        cv.imshow("keklwl",image)
        
        
        if cv.waitKey(10) & 0xFF == ord('q'):
            control_motor.stop()
            GPIO.cleanup()
            break
    
    else:
        print("Image is none")
        break



cap.release()
cv.destroyAllWindows()

