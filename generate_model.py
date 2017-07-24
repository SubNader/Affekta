import cv2
import glob
import random
import numpy as np
import datetime

print "           __  __     _    _        \n    /\\    / _|/ _|   | |  | |       \n   /  \\  | |_| |_ ___| | _| |_ __ _ \n  / /\\ \\ |  _|  _/ _ \\ |/ / __/ _` |\n / ____ \\| | | ||  __/   <| || (_| |\n/_/    \\_\\_| |_| \\___|_|\\_\\\\__\\__,_|\n"

# Types of emotions
emotions = ["neutral", "anger", "disgust", "happy", "surprise"]

# Create classifer
fisher_classifier = cv2.createFisherFaceRecognizer() 

data = {}

# Read, shuffle and split files into two portions (training and prediction)
def get_files(emotion,training_percentage):
    files = glob.glob("datasets/faces_dataset/%s/*" %emotion)
    random.shuffle(files)
    training = files[:int(len(files)*training_percentage)]
    prediction = files[-int(len(files)*(1-training_percentage)):]
    return training, prediction

# Create sets
def make_sets():
    training_data = []
    training_labels = []
    prediction_data = []
    prediction_labels = []
    for emotion in emotions:
        training, prediction = get_files(emotion,0.95)
        
	# Create training set and its labels set
        for item in training:
	    # Read image, convert it to grayscale then append it to its set
            image = cv2.imread(item)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            training_data.append(gray)
	    # Fetch the image's label and append it to the labels set
            training_labels.append(emotions.index(emotion))
	
	# Create prediction set and its labels set
        for item in prediction:
	    # Read image, convert it to grayscale then append it to its set
	    image = cv2.imread(item)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            prediction_data.append(gray)
	    # Fetch the image's label and append it to the labels set
            prediction_labels.append(emotions.index(emotion))

    return training_data, training_labels, prediction_data, prediction_labels

def run_recognizer():
    training_data, training_labels, prediction_data, prediction_labels = make_sets()
    
    print "\nSize of the training set:",len(training_labels)," images","\n\nTraining the Fisher face classifier on the dataset.."
    
    # Train
    fisher_classifier.train(training_data, np.asarray(training_labels))

    print "Done with training\n\nTrying to predict the test set.."
    cnt = 0
    correct = 0
    incorrect = 0
    for image in prediction_data:
        pred, conf = fisher_classifier.predict(image)
        if pred == prediction_labels[cnt]:
            correct += 1
            cnt += 1
        else:
            incorrect += 1
            cnt += 1
    print "Done with prediction"
    
    # Save model
    model_name = ('models/model_{:%Y-%m-%d-%H-%M-%S}_'.format(datetime.datetime.now())) + str(((100*correct)/(correct + incorrect))) + ".xml"
    fisher_classifier.save(model_name)
    return ((100*correct)/(correct + incorrect))

# Run, run, run!
scores = []
for i in range(0,1):
    correct = run_recognizer()
    print "\nResult: Recognized ", correct, " percent of the emotions correctly!\n\n" + '-'*60
