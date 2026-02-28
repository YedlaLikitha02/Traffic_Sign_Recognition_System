🚦 Traffic Sign Recognition System Using CNN
📘 Project Overview

This project is a deep learning–based Traffic Sign Recognition System that automatically detects and classifies traffic signs from images.

It uses a Convolutional Neural Network (CNN) model for accurate classification and provides a user-friendly GUI built with Tkinter to upload and test images.

The system predicts the traffic sign class and displays the confidence score.

🚀 Features at a Glance

🧠 CNN-Based Classification – 44 traffic sign classes using deep learning
🖼 Image Preprocessing – Resizing and normalization using OpenCV
🖥 Tkinter GUI – Upload and classify images easily
📊 Confidence Score – Displays prediction accuracy percentage
💾 Model Saving – Trained model saved as .h5 file

🧩 System Modules
1️⃣ Model Training Module (traffic_sign.py)

Loads traffic sign dataset (GTSRB)

Resizes images to 30×30 pixels

Normalizes pixel values (0–255 → 0–1)

Trains a CNN model using TensorFlow/Keras

Saves trained model as:

traffic_classifier.h5
2️⃣ GUI Prediction Module (gui.py)

Loads the saved model

Allows users to upload traffic sign images

Preprocesses image before prediction

Predicts traffic sign class

Displays:

Traffic sign name

Confidence percentage

🧰 Tech Stack
Layer	Technologies Used
Programming	Python
Deep Learning	TensorFlow, Keras
Image Processing	OpenCV, NumPy
GUI	Tkinter
Image Handling	PIL
⚙️ Installation & Setup
🔧 Prerequisites

Python 3.x

pip

🪜 Steps to Run
1️⃣ Clone the Repository
git clone https://github.com/YedlaLikitha02/Traffic_Sign_Recognition_System.git
cd Traffic_Sign_Recognition_System
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Train the Model
python traffic_sign.py

This generates:

traffic_classifier.h5
4️⃣ Run the GUI
python gui.py

Upload a traffic sign image and click Classify Image to view prediction.

🧾 Outputs / Results
Module	Description
CNN Model	Accurately classifies 44 traffic sign categories
GUI	Displays predicted sign and confidence score
Preprocessing	Improves accuracy using normalization and resizing
🎯 Applications

🚗 Autonomous Vehicles

🚦 Advanced Driver Assistance Systems (ADAS)

🛣 Road Safety Monitoring

🏙 Smart Traffic Systems

📚 Driver Education Systems

🏁 Conclusion

The CNN-based traffic sign recognition system successfully classifies traffic signs with high accuracy.

By combining deep learning and a simple GUI interface, the project demonstrates how AI can enhance road safety and intelligent transportation systems.

👩‍💻 Author

Yedla Likitha
Department of Information Technology
MVSR Engineering College
