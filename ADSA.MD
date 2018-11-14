# ADSA

## OBJECTIVE

Beeing able to send the two robots their position and the position of their ennemies in real time using cameras and wifi connections.

## ROADMAP

1. Compile all the dependancies nedded for ARMv7 (OpenCV, Node.js, ...)
2. Use a simple preset to benchmark the diffrent plafomrs (number of frame per seconds)
3. Experiment with the camera, try to send a video feed from slave to master
4. Learn to recognize et position in 3D, printed QRcodes with OpenCV and ArcUco
4. Implement some kind of syncronysation system so that slaves and master share the same time (essential for localisation)
5. Benchmark the diffrents implementations to see which one is preferable
6. Implement some kind of vizualtisation interface to see robots movments in real time (three.js ?) 
