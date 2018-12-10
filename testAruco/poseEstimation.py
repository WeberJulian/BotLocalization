import numpy as np
import cv2
import cv2.aruco as aruco
import glob
import time

# Loading camera matrix and distortion coeficients
fs = cv2.FileStorage("./test.yaml", cv2.FILE_STORAGE_READ)
fn = fs.getNode("camera_matrix")
mtx = fn.mat()
fn = fs.getNode("dist_coeff")
dist = fn.mat()

frame = cv2.imread("arucoTest.jpg")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()

#lists of ids and the corners beloning to each id
corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

if np.all(ids != None):
    rvec, tvec = aruco.estimatePoseSingleMarkers(corners[0], 14, mtx, dist) #Estimate pose of each marker and return the values rvet and tvec---different from camera coefficients
    #(rvec-tvec).any() # get rid of that nasty numpy value array error

print(rvec, tvec)

