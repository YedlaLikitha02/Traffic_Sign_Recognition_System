🚦 Traffic Sign Recognition System

A deep learning–based Traffic Sign Recognition System built using Convolutional Neural Networks (CNN).
This project classifies traffic signs from images and displays the predicted sign along with a confidence score using a simple Tkinter GUI.

📌 Project Overview

Traffic sign recognition is an important component of intelligent transportation systems and autonomous vehicles.
This project uses a CNN model to automatically recognize and classify traffic signs into 44 different categories.

The system consists of:

A training script to train the CNN model

A GUI application to test the trained model

📂 Project Structure
Traffic_Sign_Recognition_System/
│
├── traffic_sign.py        # CNN model training
├── gui.py                 # GUI for testing the model
├── traffic_classifier.h5  # Saved trained model
├── requirements.txt
└── README.md
🛠 Technologies Used

Python

TensorFlow / Keras

OpenCV

NumPy

Tkinter

PIL (Python Imaging Library)

⚙️ How the System Works
1️⃣ Model Training (traffic_sign.py)

Loads traffic sign images (GTSRB dataset)

Resizes images to 30×30 pixels

Normalizes pixel values (0–255 → 0–1)

Trains a Convolutional Neural Network

Saves the trained model as traffic_classifier.h5

2️⃣ GUI Application (gui.py)

Loads the trained model

Allows users to upload an image

Preprocesses the image

Predicts the traffic sign

Displays:

Predicted traffic sign name

Confidence percentage

▶️ How to Run the Project
Step 1: Install Dependencies
pip install -r requirements.txt
Step 2: Train the Model
python traffic_sign.py

This will generate the trained model file:

traffic_classifier.h5
Step 3: Run the GUI
python gui.py

Upload a traffic sign image and click Classify Image to see the prediction.

✅ Features

✔ 44-class traffic sign classification
✔ Confidence score display
✔ User-friendly graphical interface
✔ Deep learning–based prediction
✔ Image preprocessing using OpenCV

📊 Applications

Autonomous vehicles

Advanced Driver Assistance Systems (ADAS)

Smart traffic management

Road safety monitoring

Driver education tools

🎯 Conclusion

The system successfully classifies traffic signs using a CNN-based approach.
It demonstrates how deep learning can improve traffic sign recognition accuracy and reduce human error in real-world driving scenarios.

👩‍💻 Author

Yedla Likitha
Department of Information Technology
MVSR Engineering College
