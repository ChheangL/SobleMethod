from picamera import PiCamera
import numpy as np
import math
import cv2 as cv
from PIL import Image
import timeit


def main():
    #setting up pi camera 
    camera = PiCamera() #start the pi camera as camera
    camera.rotation = 180
    camera.resolution = (1280,720)
    camera.framerate=30
    camera.start_preview(alpha=200)
    camera.zoom = (0.0,0.5,1.0,0.5)

    #crop image
    src = np.empty((720,1280,3),dtype=np.uint8)
    camera.capture(src,format='rgb')
    dst = cv.Canny(src, 50, 200, None, 3)    
    cdstP = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)

    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)

    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)

if __name__ == "__main__":
    main()