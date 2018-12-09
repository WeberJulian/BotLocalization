from picamera.array import PiRGBArray
from picamera import PiCamera
import picamera
import cv2

CALIBRATION_FRAMES = int(input("How many frames do you want ?"))

print("Press enter to start capture...")
input()

#Start capturing images for calibration
with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as output:
        for i in range(CALIBRATION_FRAMES):
            print("frame " + str(i))
            camera.capture(output, 'rgb')
            image = output.array
            cv2.imwrite('calib_images/calib' + str(i) + '.jpg',image)
            output.truncate(0)
            print("Press to capture next image...")
            input()
            
print("Finished, captured " + str(CALIBRATION_FRAMES) + " frames in /")
