import csv
import cv2
import numpy as np

# This is the correction made to the left and right camera images
correction = 0.1
lines = []
print("Reading Driving Log...")
# The log of the capture is loaded to be processed
with open('./CarData/driving_log.csv') as csvfile:
	reader = csv.reader(csvfile)
	for line in reader:
		lines.append(line)
print("Driving Log Read.")

print("Loading images...")
# Based on the log, the images are loaded in memory
images = []
measurements = []
for line in lines:
	for cam in range(3):
		current_path = line[cam]
		image = cv2.imread(current_path)
		images.append(image)
		# Based on the file loaded, the steering is corrected
		if cam == 0:
			measurement = float(line[3])
		elif cam == 1:
			measurement = float(line[3])+correction
		else:
			measurement = float(line[3])-correction
		measurements.append(measurement)
print("Images Loaded.")

X_train = np.array(images)
y_train = np.array(measurements)

print("Loading Libraries...")
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D, Dropout
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D

print("Assembling network")
# The model is assembled
model = Sequential()
model.add(Lambda(lambda x: x / 255.0 - 0.5, input_shape = (160,320,3)))
model.add(Cropping2D(cropping = ((70,25),(0,0))))
model.add(Convolution2D(24,5,5,subsample = (2,2), activation ="relu"))
model.add(Convolution2D(36,5,5,subsample = (2,2), activation ="relu"))
model.add(Convolution2D(48,5,5,subsample = (2,2), activation ="relu"))
model.add(Convolution2D(64,3,3, activation ="relu"))
model.add(Convolution2D(64,3,3, activation ="tanh"))
model.add(Flatten())
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))
print("Network Assembled")

print("Trainning Network")
# The network is trained
model.compile(loss = 'mse', optimizer ='adam')
model.fit(X_train, y_train, validation_split = 0.3, shuffle = True, nb_epoch=30)

# And saved
model.save('model_alpha.h5')
print('Model Saved')

