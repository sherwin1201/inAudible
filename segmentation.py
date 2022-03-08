import io
import cv2
import numpy as np
from rembg.bg import remove
from PIL import Image
from PIL import ImageFile

def removebg(input_path):
    # Uncomment the following line if working with trucated image formats (ex. JPEG / JPG)
    ImageFile.LOAD_TRUNCATED_IMAGES = True

    f = np.fromfile(input_path)
    result = remove(f)
    print(f)
    img = Image.open(io.BytesIO(result)).convert("RGBA")
    # img.save(output_path)
    return img

def segment(frame):
    blur = cv2.GaussianBlur(frame, (5,5), 2)

    # canny  = cv2.Canny(blur, 50, 100, 3)

    th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    return res

input_path = "data/A/A0.jpg"
img_wobg = removebg(input_path)

frame = cv2.imread("out.png")
out = segment(frame)
cv2.imshow('Output', out)
cv2.waitKey(0)