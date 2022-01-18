import numpy as np
import cv2

def preprocess(frame):
    resized = cv2.resize(frame, (256,256), interpolation = cv2.INTER_AREA)

    grayscale = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    #blur = cv2.GaussianBlur(grayscale, (5,5), 2)

    # canny  = cv2.Canny(blur, 50, 100, 3)

    # th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    return grayscale