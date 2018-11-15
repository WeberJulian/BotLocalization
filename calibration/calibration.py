from picamera.array import PiRGBArray
from picamera import PiCamera
import picamera.arrays
import cv2

CALIBRATION_FRAMES = 300

print("Press enter to start the generation of the board...")
input()

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
board = cv2.aruco.CharucoBoard_create(3,3,.025,.0125,dictionary)
img = board.draw((200*3,200*3))

#Dump the calibration board to a file
cv2.imwrite('charuco.png',img)

print("Board saved")

print("Press enter to start capture...")
input()


#Start capturing images for calibration
with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as output:
        allCorners = []
        allIds = []
        decimator = 0
        for i in range(CALIBRATION_FRAMES):
            camera.capture(output, 'rgb')
            image = output.array

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            res = cv2.aruco.detectMarkers(gray,dictionary)

            if len(res[0])>0:
                res2 = cv2.aruco.interpolateCornersCharuco(res[0],res[1],gray,board)
                if res2[1] is not None and res2[2] is not None and len(res2[1])>3 and decimator%3==0:
                    allCorners.append(res2[1])
                    allIds.append(res2[2])

                cv2.aruco.drawDetectedMarkers(gray,res[0],res[1])
            decimator+=1
            output.truncate(0)

imsize = gray.shape

print("Press enter to start calibration...")
input()

cal = cv2.aruco.calibrateCameraCharuco(allCorners,allIds,board,imsize,None,None)
print("Calibration successfull : ")
print(cal)