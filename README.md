# Affekta
Real-time emotion recognition using facial expressions

## Requirements
- Python
- OpenCV
- A facial expressions dataset (or use the default pretrained model)

## Running Affekta
To run Affekta, browse to its main directory via the terminal and run ```affekta.py``` in sudo mode.

Unless altered, Affekta will use the pretrained model (default-model.xml) which was trained using the _Cohn-Kanade AU-Coded Expression Database_.

## Training your own model
- Move your facial expressions image data to ```datasets/emotions/emotions_images```
- Move the corresponding emotions data to ```datasets/emotions/emotions_data```
- Run ```create_project.py``` to create the project structure
- Run ```extract_faces.py``` to preprocess and extract faces from your image data
- Run ```generate_model.py``` to train your model (saved to the ```models``` directory)

## Using your own model
To use your own  model, rename your model to ```defaul-model.xml```, or alter the predefined model name in ```affekta.py```.

## Credits
This project is inspired by and based on the great work by _Paul Van Gent_.
