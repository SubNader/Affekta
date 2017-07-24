import os
import shutil
import glob
from shutil import copyfile

# Define datasets directories
directories = ["faces_dataset", "sorted_dataset"]

# Define emotions
emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]

print "           __  __     _    _        \n    /\\    / _|/ _|   | |  | |       \n   /  \\  | |_| |_ ___| | _| |_ __ _ \n  / /\\ \\ |  _|  _/ _ \\ |/ / __/ _` |\n / ____ \\| | | ||  __/   <| || (_| |\n/_/    \\_\\_| |_| \\___|_|\\_\\\\__\\__,_|\n"

# Remove any traces
for directory in directories:

	try:
		shutil.rmtree("datasets/" + directory)
	except:
		print("No trace for " + directory + " was found. Creating it..")
	os.mkdir("datasets/" + directory)
	
	# Create folder structure
	for emotion in emotions:
		os.mkdir("datasets/" + directory+'/'+emotion)

# Fetch emotions data
participants = glob.glob("datasets/emotions/emotions_data/*")

for x in participants:
	part = "%s" %x[-4:]
	for sessions in glob.glob("%s/*" %x):
		for files in glob.glob("%s/*" % sessions):
			current_session = files[37:-30]
			file = open(files, 'r')
			emotion = int(float(file.readline()))
			sourcefile_neutral = sorted(glob.glob("datasets/emotions/emotions_images/%s/%s/*" %(part, current_session)))[0]
			sourcefile_emotion = sorted(glob.glob("datasets/emotions/emotions_images/%s/%s/*" %(part, current_session)))[-1]
			dest_neutral = "datasets/sorted_dataset/neutral/%s" %sourcefile_neutral[45:]
			dest_emotion = "datasets/sorted_dataset/%s/%s" %(emotions[emotion], sourcefile_emotion[45:])
			copyfile(sourcefile_neutral, dest_neutral)
			copyfile(sourcefile_emotion, dest_emotion)
