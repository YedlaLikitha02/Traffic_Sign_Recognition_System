🚦 Traffic Sign Recognition System
📌 Overview

This project is a Traffic Sign Recognition System built using Convolutional Neural Networks (CNN).
It classifies traffic signs from images and displays the predicted sign along with a confidence score using a Tkinter GUI.

📂 Project Structure
Traffic_Sign_Recognition_System/
│
├── traffic_sign.py        # Train the CNN model
├── gui.py                 # GUI to test the trained model
├── traffic_classifier.h5  # Saved trained model
├── requirements.txt
└── README.md
🛠 Technologies Used

Python

TensorFlow / Keras

OpenCV

NumPy

Tkinter

PIL

⚙️ How It Works
1️⃣ Model Training (traffic_sign.py)

Loads traffic sign dataset (GTSRB)

Resizes images to 30×30 pixels

Normalizes pixel values

Trains a CNN model

Saves the trained model as:

traffic_classifier.h5
2️⃣ GUI Testing (gui.py)

Loads the saved model (traffic_classifier.h5)

Allows user to upload an image

Preprocesses image

Predicts traffic sign

Displays:

Traffic sign name

Confidence score

▶️ How to Run the Project
Step 1: Install Requirements
pip install -r requirements.txt
Step 2: Train the Model
python traffic_sign.py

This will generate:

traffic_classifier.h5
Step 3: Run GUI
python gui.py

Upload an image and click Classify Image.

✅ Features

44-class traffic sign classification

Confidence score display

User-friendly GUI

Deep learning based model

📊 Applications

Autonomous vehicles

Driver assistance systems

Smart traffic management

Road safety systems

👩‍💻 Author

Yedla Likitha
Information Technology
MVSR Engineering College
