import numpy as np
import cv2
import cv2.aruco as aruco
from picamera.array import PiRGBArray
from picamera import PiCamera
import picamera

# Loading camera matrix and distortion coeficients
fs = cv2.FileStorage("./calibration.yaml", cv2.FILE_STORAGE_READ)
fn = fs.getNode("camera_matrix")
mtx = fn.mat()
fn = fs.getNode("dist_coeff")
dist = fn.mat()

MARKER_SIZE = int(input("What is the size of the Aruco marker ? d="))


with picamera.PiCamera() as camera:
    camera.resolution = (1920, 1088)
    with picamera.array.PiRGBArray(camera) as output:
        while(True):
            camera.capture(output, 'rgb')
            frame = output.array
            output.truncate(0)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
            parameters = aruco.DetectorParameters_create()
            corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
            if np.all(ids != None):
                rvec, tvec = aruco.estimatePoseSingleMarkers(corners[0], MARKER_SIZE, mtx, dist) 
                euclDist = ((tvec[0][0][0])**2 + (tvec[0][0][1])**2 + (tvec[0][0][2])**2)**(1/2)
                print(euclDist)

