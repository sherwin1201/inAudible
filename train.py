from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout

SIZE = 128
train_gen = ImageDataGenerator(rescale=1.0/255, 
                                shear_range=0.2, 
                                zoom_range=0.2, 
                                horizontal_flip=True,
                                validation_split=0.2)
test_gen = ImageDataGenerator(rescale=1.0/255,
                                validation_split=0.2)

training_set = train_gen.flow_from_directory('dataset/asl_alphabet_train/asl_alphabet_train', 
                                            batch_size=32,
                                            target_size=(SIZE,SIZE),
                                            color_mode='grayscale',
                                            class_mode='categorical',
                                            subset='training')

validation_set = test_gen.flow_from_directory('dataset/asl_alphabet_train/asl_alphabet_train', 
                                            target_size=(SIZE,SIZE),
                                            batch_size=32,
                                            color_mode='grayscale',
                                            class_mode='categorical',
                                            subset='validation')                                            

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
    model.add(Dense(units=29, activation='softmax'))
    model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=['accuracy'])
    return model


model = build_model()
model.fit_generator(training_set,
                    validation_data=validation_set,
                    steps_per_epoch = training_set.n//training_set.batch_size,
                    validation_steps = validation_set.n//validation_set.batch_size,
                    epochs=5)

model.summary()
model.save('models/test_model_3')