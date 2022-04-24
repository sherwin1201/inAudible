import cv2
from pymysql import NULL
from sklearn import preprocessing
from preprocessing import preprocess
from keras.models import load_model

model = load_model("models/test_model_5")

SIZE = 256
def getLetter(result):
    classLabels = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: '10',
        11: 'A',
        12: 'B',
        13: 'V',
        14: 'D',
        15: 'E',
        16: 'F',
        17: 'G',
        18: 'H',
        19: 'I',
        20: 'J',
        21: 'K',
        22: 'L',
        23: 'M',
        24: 'N',
        25: 'O',
        26: 'P',
        27: 'Q',
        28: 'R',
        29: 'S',
        30: 'T',
        31: 'U',
        32: 'V',
        33: 'W',
        34: 'X',
        35: 'Y',
        36: 'Z'
    }

    try:
        res = int(result)
        return classLabels[res]
    except:
        return "Error"

cap = cv2.VideoCapture(0)

c = 0
word = ""
prev_r = NULL
while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    #Coordinates of the ROI
    x1 = int(0.5*frame.shape[0]-20)     #220
    y1 = 10                             #10
    x2 = frame.shape[1]-20              #620
    y2 = int(0.5*frame.shape[1]+100)    #420

    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)

    roi = frame[y1:y2, x1:x2]
    cv2.imshow('roi', roi)
    roi = preprocess(roi)
    
    cv2.imshow('preprocessed roi', roi)
    copy = frame.copy()
    cv2.rectangle(copy, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)

    roi = roi.reshape(1,SIZE,SIZE,1)

    result = model.predict_generator(roi)
    # print(result)
    y_classes = result.argmax(axis=-1)
    r = y_classes[0]

    # print(c)
    # print(r, prev_r)

    if c == 0:
        prev_r = r
        c += 1
    else:
        if prev_r == r:
            c += 1
        else:
            c = 0

    letter  = getLetter(r)

    if c == 15:
        word = word + letter
        c = 0

    cv2.putText(copy, "Character "+letter, (100,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    cv2.putText(copy, "Word "+word, (100,400), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    cv2.imshow('frame', copy)

    k = cv2.waitKey(1)
    if k == 8:
        word = word[:-1]

    if k == 13:
        break

cap.release()
cv2.destroyAllWindows()