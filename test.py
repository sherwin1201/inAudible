from keras.models import load_model
import numpy as np
import cv2
from preprocessing import preprocess

SIZE = 256
TEST_DIR = "dataset/test"

model = load_model("models/test_model_4")

# test_gen = ImageDataGenerator(rescale=1.0/255)
# test_set = test_gen.flow_from_directory('dataset/test/A', 
#                                             target_size=(SIZE,SIZE),
#                                             batch_size=10,
#                                             color_mode='grayscale',
#                                             class_mode='categorical')

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

input = cv2.imread("dataset/test/A/A4_36475b26-1541-40e4-b3fa-e444eeaec317.jpg", 0)
test_image = cv2.resize(input, (SIZE,SIZE))
# test_image = preprocess(input)

result = model.predict_generator(test_image.reshape(1, SIZE, SIZE, 1))
y_classes = result.argmax(axis=-1)
text = "Predicted sign: "+labels[y_classes[0]] 
result = cv2.resize(input, (SIZE*2, SIZE*2), interpolation = cv2.INTER_AREA)
result = cv2.rectangle(result, (0,420),(result.shape[0],result.shape[0]), (255, 0, 0), -1 )
result = cv2.putText(result, text, (10,480), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2, cv2.LINE_AA)
cv2.imshow('Predicted Image', input)
cv2.waitKey(0)
print(labels[y_classes[0]])



# predict=model.predict_generator(test_set)
# y_classes = predict.argmax(axis=-1)
# for i in y_classes:
#     print(labels[i])
