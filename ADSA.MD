# ADSA

## OBJECTIVE

Beeing able to send the two robots their position and the position of their ennemies in real time using cameras and wifi connections.

## ROADMAP

- [X] 1) Compile all the dependancies nedded for ARMv7 (OpenCV, Node.js, ...)
- [X] 2) Use a simple preset to benchmark the diffrent plafomrs (number of frame per seconds)
- [ ] 3) Experiment with video feeds and calibrate the camera (distortion matrix)
- [ ] 4) Learn to recognize and calculate 3D position of printed QRcodes with OpenCV and ArcUco
- [ ] 5) Implement the physical solution on a reproduction of the official competition's Arena
- [ ] 6) Deduce the position of all the robots
- [ ] 7) Implement some kind of syncronysation system so that slaves and master share the same time
- [ ] 8) Benchmark the diffrents implementations to see which one is preferable
- [ ] 9) Implement some kind of vizualtisation interface to see robots movments in real time (three.js ?)
- [ ] 10) Setup the live comunication with the robots

## Work done :

1) The openCV library is compiled and usable on the Raspery Pi
2) Benchmark is fonctionnal and the results are available here [*Benchmarks*](https://github.com/WeberJulian/BotLocalization/blob/master/benchmark/benchmarks.md)
