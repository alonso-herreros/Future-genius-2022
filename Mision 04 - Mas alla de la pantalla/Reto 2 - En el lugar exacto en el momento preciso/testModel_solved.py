from os.path import join, dirname
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow import keras as kr


# Define global variables
backgroundImg = plt.imread(join(dirname(__file__), "granCanariaVistaAerea.jpg"))


# Load neural network model
print('Loading artificial neural network model...')
model = kr.models.load_model(join(dirname(__file__), 'model.h5'))


# Define function to classify a new sample using the trained model
def classify(Xnew, model):
    Ynew = model.predict(Xnew)
    Ynew = Ynew.flatten()
    for i in range(len(Ynew)):
        if Ynew[i] > 0.5:
            Ynew[i] = 1
        else:
            Ynew[i] = 0
    return Ynew


# Load test data
print('Loading test data...')
test_positions = []

with open(join(dirname(__file__), 'test_set.csv'), 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)  # skip the headers
    for line in csv_reader:
        x = float(line[0])
        y = float(line[1])
        test_positions.append([x, y])
test_positions = np.array(test_positions)


# Show test data
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("test data")
ax.imshow(backgroundImg, extent=[-63, 63, -36, 36])
ax.scatter(test_positions[:, 0], test_positions[:, 1], s=20, c="skyblue")
#plt.show()


# Classify test data using neural network model
print('Classifying test data...')
predicted_labels = classify(test_positions, model)


# Visualize classified test data by the model
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("classified test data by the model")
ax.imshow(backgroundImg, extent=[-63, 63, -36, 36])
ax.scatter(test_positions[predicted_labels == 0, 0], test_positions[predicted_labels == 0, 1], s=20, color="skyblue")
ax.scatter(test_positions[predicted_labels == 1, 0], test_positions[predicted_labels == 1, 1], s=20, color="salmon")
#plt.show()


# Load classified test data by a human
print('Loading test data classification by a human...')
test_set_labels = []

with open(join(dirname(__file__), 'test_set_labels.csv'), 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)  # skip the headers
    for line in csv_reader:
        label = float(line[0])
        test_set_labels.append(label)
test_set_labels = np.array(test_set_labels)


# Calculate success rate
print('Comparing model predictions with human classification...')
#########################################################################
successes = 0
for i in range(len(predicted_labels)):
    successes += 1 if predicted_labels[i] == test_set_labels[i] else 0
print(successes, "/", len(predicted_labels))

success_rate = successes / len(predicted_labels)
#########################################################################


success_rate = "{:.2f}".format(success_rate*100)
print(f'Success rate: {success_rate}%')
