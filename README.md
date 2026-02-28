
# 🚦 Traffic Sign Recognition System Using CNN

## 📘 Project Overview

This is an **intelligent deep learning application** that recognise and classifies **traffic signs from images**.
It provides accurate predictions using a **Convolutional Neural Network (CNN)** model along with a **confidence score display through a graphical user interface (GUI)**.

The system helps improve **road safety and intelligent transportation systems** by automating traffic sign recognition.

---

## 🚀 Features at a Glance

* 🧠 **CNN-Based Classification** – Classifies traffic signs into 44 categories.
* 🖼️ **Image Preprocessing (OpenCV)** – Resizes and normalizes images for better accuracy.
* 🖥️ **Graphical User Interface (Tkinter)** – Upload and classify traffic sign images easily.
* 📊 **Confidence Score Display** – Shows prediction probability percentage.
* 💾 **Model Saving (.h5 File)** – Stores trained model for future predictions.

---

## 🧩 System Modules

### 1️⃣ Model Training Module (`traffic_sign.py`)

* Loads traffic sign images from the **GTSRB dataset**.
* Resizes images to **30×30 pixels**.
* Normalizes pixel values (0–255 → 0–1).
* Builds and trains a **Convolutional Neural Network (CNN)**.
* Saves trained model as:

```bash
traffic_classifier.h5
```

---

### 2️⃣ GUI Prediction Module (`gui.py`)

* Loads the saved model.
* Allows users to upload traffic sign images.
* Preprocesses image before prediction.
* Predicts traffic sign class.
* Displays:

  * **Predicted traffic sign name**
  * **Confidence percentage**

---

## 🧰 Tech Stack

| Layer                | Technologies      |
| -------------------- | ----------------- |
| **Programming**      | Python            |
| **Deep Learning**    | TensorFlow, Keras |
| **Image Processing** | OpenCV, NumPy     |
| **GUI**              | Tkinter           |
| **Image Handling**   | PIL               |

---

## ⚙️ Installation & Setup

### 🔧 Prerequisites

* Python 3.x
* pip

---

### 🪜 Steps to Run

#### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/YedlaLikitha02/Traffic_Sign_Recognition_System.git
cd Traffic_Sign_Recognition_System
```

---

#### **2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

---

#### **3️⃣ Train the Model**

```bash
python traffic_sign.py
```

This will generate:

```bash
traffic_classifier.h5
```

---

#### **4️⃣ Run the GUI**

```bash
python gui.py
```

Upload a traffic sign image and click **Classify Image** to view prediction.

---

## 🧾 Outputs / Results

| Module            | Description                                  |
| ----------------- | -------------------------------------------- |
| **CNN Model**     | Classifies 44 traffic sign categories        |
| **GUI**           | Displays predicted sign and confidence score |
| **Preprocessing** | Improves accuracy using normalization        |

---

## 🏁 Conclusion

This project demonstrates how **deep learning and computer vision** can be used to automatically recognize traffic signs.
By combining **CNN models with a user-friendly GUI**, the system provides accurate classification and enhances road safety applications.

---

## 👩‍💻 Author

**Yedla Likitha**
* Department of Information Technology
* MVSR Engineering College
.
