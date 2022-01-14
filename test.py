from keras import models
from keras.preprocessing.image import ImageDataGenerator, load_img
from keras_preprocessing import image
from keras.models import load_model
import numpy as np
import os
import cv2
from numpy.core.numeric import NaN

SIZE = 128
TEST_DIR = "dataset/asl_alphabet_test/asl_alphabet_test"

model = load_model("models/test_model_3")
train_gen = ImageDataGenerator(rescale=1.0/255, 
                                shear_range=0.2, 
                                zoom_range=0.2, 
                                horizontal_flip=True)

# valid_generator = train_gen.flow_from_directory('dataset/asl_alphabet_train/asl_alphabet_train', 
#                                             target_size=(SIZE,SIZE),
#                                             batch_size=10,
#                                             color_mode='grayscale',
#                                             class_mode='categorical')

# print(valid_generator.class_indices)

test_gen = ImageDataGenerator(rescale=1.0/255)

test_set = test_gen.flow_from_directory('dataset/asl_alphabet_test/', 
                                            target_size=(SIZE,SIZE),
                                            batch_size=10,
                                            color_mode='grayscale',
                                            class_mode='categorical')


# for i in os.listdir(TEST_DIR):
#     img = image.load_img(TEST_DIR+"//"+i, target_size=(SIZE,SIZE), color_mode='grayscale')
#     X = np.expand_dims(image.img_to_array(img), axis = 0)
#     images = np.vstack([X])

labels = np.empty(29, dtype=object)
c = 'A'
for i in range(29):
    if i < 26:
        labels[i] = c
        c = chr(ord(c) + 1)
    if i == 26:
        labels[i] = 'del'
    if i == 27:
        labels[i] = 'nothing'
    if i == 28:
        labels[i] = 'space'

input = cv2.imread("dataset/asl_alphabet_test/asl_alphabet_test/X_test.jpg", 0)
test_image = cv2.resize(input, (SIZE,SIZE))
result = model.predict_generator(test_image.reshape(1, SIZE, SIZE, 1))
y_classes = result.argmax(axis=-1)
text = "Predicted sign: "+labels[y_classes[0]] 
result = cv2.resize(input, (SIZE*2, SIZE*2), interpolation = cv2.INTER_AREA)
result = cv2.rectangle(result, (0,220),(result.shape[0],result.shape[0]), (255, 0, 0), -1 )
result = cv2.putText(result, text, (10,240), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2, cv2.LINE_AA)
cv2.imshow('Predicted Image', result)
cv2.waitKey(0)
print(labels[y_classes[0]])

# predict=model.predict_generator(test_set)
# y_classes = predict.argmax(axis=-1)


# for i in y_classes:
#     print(labels[i])
