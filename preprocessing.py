import numpy as np
import cv2

path = None
frame = cv2.imread('a.jpg')
cv2.imshow('Input', frame)

resized = cv2.resize(frame, (256,256), interpolation = cv2.INTER_AREA)
# r_frame, g_frame, b_frame = cv2.split(frame)

# r_eq = cv2.equalizeHist(r_frame)
# g_eq = cv2.equalizeHist(g_frame)
# b_eq = cv2.equalizeHist(b_frame)

# equ = cv2.merge((r_eq, g_eq, b_eq))
#cv2.imshow('Equalized', equ)

grayscale = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Grayscale', grayscale)

blur = cv2.GaussianBlur(grayscale, (3,3), 3)
#cv2.imshow('Blur', blur)

canny  = cv2.Canny(blur, 50, 100, 3)
#cv2.imshow('Canny', canny)

cv2.imshow('Processed image (Edge detection)', canny)

th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
#cv2.imshow('Adaptive Threshold', th3)

ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cv2.imshow('Processed image (Thresholding)', res)

cv2.waitKey(0)