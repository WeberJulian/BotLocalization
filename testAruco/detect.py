import numpy as np
import cv2 as cv
import cv2.aruco as aruco
import time as ti
 
BENCH_TIME = 5
 
img = cv.imread("arucoTest.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters =  aruco.DetectorParameters_create()
corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
print(corners, ids)