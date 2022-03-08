from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout

SIZE = 256
DATASET_DIRECTORY = "dataset"
CATEGORIES = 37
BATCH_SIZE = 16

train_gen = ImageDataGenerator(rescale=1.0/255, 
                                shear_range=0.2, 
                                zoom_range=0.2, 
                                horizontal_flip=True,)
test_gen = ImageDataGenerator(rescale=1.0/255,)

training_set = train_gen.flow_from_directory(DATASET_DIRECTORY+'/train', 
                                            batch_size=BATCH_SIZE,
                                            target_size=(SIZE,SIZE),
                                            color_mode='grayscale',
                                            class_mode='categorical',)

validation_set = test_gen.flow_from_directory(DATASET_DIRECTORY+'/test', 
                                            target_size=(SIZE,SIZE),
                                            batch_size=BATCH_SIZE,
                                            color_mode='grayscale',
                                            class_mode='categorical',)                                            

def build_model():
    model = Sequential()
    model.add(Conv2D(32,kernel_size=(3,3),activation='relu',input_shape=(SIZE, SIZE, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())

    model.add(Dense(units=128, activation='relu'))
    model.add(Dropout(0.40))
    model.add(Dense(units=96, activation='relu'))
    model.add(Dropout(0.40))
    model.add(Dense(units=64, activation='relu'))
    model.add(Dense(units=CATEGORIES, activation='softmax'))
    model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=['accuracy'])
    return model


model = build_model()
model.fit_generator(training_set,
                    validation_data=validation_set,
                    steps_per_epoch = training_set.n//training_set.batch_size,
                    validation_steps = validation_set.n//validation_set.batch_size,
                    epochs=10)

model.summary()
model.save('models/test_model_4')