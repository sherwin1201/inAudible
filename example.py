from unittest import result
from rembg.bg import remove
import numpy as np
import io
from PIL import Image
from PIL import ImageFile
import cv2

input_path = 'G17.jpg'
output_path = 'out.png'

# Uncomment the following line if working with trucated image formats (ex. JPEG / JPG)
ImageFile.LOAD_TRUNCATED_IMAGES = True

# f = np.fromfile(input_path)
# print(f)

f = cv2.imread("G17.jpg")
result = remove(f)
print(result)

img = Image.open(io.BytesIO(result)).convert("RGBA")

# img.save(output_path)