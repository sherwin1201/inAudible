import numpy as np
import cv2
import os

def preprocess(frame):
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(grayscale, (5,5), 2)

    # canny  = cv2.Canny(blur, 50, 100, 3)

    th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    resized = cv2.resize(res, (256,256), interpolation = cv2.INTER_AREA)

    return resized

if not os.path.exists('preprocessed'):
    os.makedirs('preprocessed')

for i in os.listdir("data/"):
    for j in os.listdir("data/"+i):
        img = cv2.imread("data/"+i+"/"+j)
        preprocessed_img = preprocess(img)
        if not os.path.exists('preprocessed/'+i):
            os.makedirs("preprocessed/"+i)
        cv2.imwrite("preprocessed/"+i+"/"+j, preprocessed_img)