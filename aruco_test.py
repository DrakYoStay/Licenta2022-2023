import cv2
import cv2.aruco as aruco
import numpy as np

# Load the image
img = cv2.imread('C:\\Users\\User\\Desktop\\Licenta2022-2023\\ArucoTest.png')

# Create the ArUco detector
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters_create()
parameters.adaptiveThreshConstant = 10.0


# Define the font and text color for the labels
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.7
color = (0, 0, 255)

# Detect the markers in the image
corners, ids, _ = aruco.detectMarkers(img, aruco_dict, parameters=parameters)
print(ids)
# If two markers are detected, classify them based on their IDs
if ids is not None:
    # Draw the detected marker(s) and label them with their ID(s)
    aruco.drawDetectedMarkers(img, corners)
    for i, marker_id in enumerate(ids):
        label = 'ID: {}'.format(marker_id)
        cv2.putText(img, label, tuple(corners[i][0][0].astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow('Image with markers', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
