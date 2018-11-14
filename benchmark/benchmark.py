import numpy as np
import cv2 as cv
import cv2.aruco as aruco
import time as ti
 
BENCH_TIME = 5
 
img = cv.imread("bench.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print("Benchmarking for " + str(BENCH_TIME) + " seconds...")
T0 = ti.time()
frames = 0
while(T0 + BENCH_TIME > ti.time()):

    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()

    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    frames+=1

print("Total frame processed : " + str(frames))
print("Result : " + str(frames / BENCH_TIME) + " FPS")