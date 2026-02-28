import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
import os
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout
from sklearn.metrics import accuracy_score


data = []
labels = []
classes = 45
cur_path = os.getcwd()


for i in range(classes):
    path = os.path.join(cur_path, 'archive', 'Train', str(i))
    images = os.listdir(path)

    for img_name in images:
        try:
            image = cv2.imread(os.path.join(path, img_name))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (30, 30))
            image = image / 255.0

            data.append(image)
            labels.append(i)

        except:
            print("Error loading image")

data = np.array(data)
labels = np.array(labels)

print("Dataset Loaded")
print("Data shape:", data.shape)
print("Labels shape:", labels.shape)


X_train, X_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.2, random_state=42)

y_train = to_categorical(y_train, classes)
y_test = to_categorical(y_test, classes)

model = Sequential()

model.add(Conv2D(32, (5,5), activation='relu', input_shape=(30,30,3)))
model.add(Conv2D(32, (5,5), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3,3), activation='relu'))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(classes, activation='softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

epochs = 15

history = model.fit(
    X_train, y_train,
    batch_size=32,
    epochs=epochs,
    validation_data=(X_test, y_test)
)

model.save("traffic_classifier.h5")
print("Model saved successfully!")


plt.figure()
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()


print("Evaluating on Test dataset...")

test_df = pd.read_csv('archive/Test.csv')
labels = test_df["ClassId"].values
imgs = test_df["Path"].values

test_data = []

for img in imgs:
    image_path = os.path.join(cur_path, 'archive', img)
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (30,30))
    image = image / 255.0
    test_data.append(image)

X_test = np.array(test_data)

pred = np.argmax(model.predict(X_test), axis=1)

print("Test Accuracy:", accuracy_score(labels, pred))
