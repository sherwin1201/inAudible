import os
import numpy as np 
import shutil

DATA_DIRECTORY = "data/"

for i in os.listdir(DATA_DIRECTORY):
    if not os.path.exists('dataset/train/' + i):
        os.makedirs('dataset//train/' + i)

    if not os.path.exists('dataset//test/' + i):
        os.makedirs('dataset/test/' + i)

    source = DATA_DIRECTORY + '/' + i

    allFileNames = os.listdir(source)

    np.random.shuffle(allFileNames)

    test_ratio = 0.25

    train_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                                        [int(len(allFileNames)* (1 - test_ratio))])

    train_FileNames = [source+'/'+ name for name in train_FileNames.tolist()]
    test_FileNames = [source+'/' + name for name in test_FileNames.tolist()]

    for name in train_FileNames:
        shutil.copy(name, 'dataset/train/' + i)

    for name in test_FileNames:
        shutil.copy(name, 'dataset/test/' + i)