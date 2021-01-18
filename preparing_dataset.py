import numpy as np
import cv2
import os
import random
import matplotlib.pyplot as plt
import pickle
#DIRECTORY = "/home/vikram/Documents/minor_project/train"
DIRECTORY = "/home/vikram/Documents/datasets/kagglecatsanddogs/train"

CATEGORIES = ['Cat', 'Dog']
train_data = []
for category in CATEGORIES:
    folder = os.path.join(DIRECTORY, category)
    label = CATEGORIES.index(category)
    for img in os.listdir(folder):
        img_path = os.path.join(folder, img)
        img_arr = cv2.imread(img_path)
        img_arr = cv2.resize(img_arr, (100,100))
        train_data.append([img_arr, label])
random.shuffle(train_data)
print(len(train_data))
x=[]
y=[]
for features, label in train_data:
    x.append(features)
    y.append(label)
x = np.array(x)
y = np.array(y)
print(len(x))
print(type(x))
pickle.dump(x, open('x.pkl', 'wb'))
pickle.dump(y, open('y.pkl', 'wb'))
print("Done!")