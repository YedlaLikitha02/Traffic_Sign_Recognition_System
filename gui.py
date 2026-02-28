from tkinter import filedialog
from tkinter import *
import cv2
import numpy as np
from keras.models import load_model
from PIL import Image, ImageTk

model = load_model('traffic_classifier.h5')
print(model.output_shape)

classes = {
    0:'Speed limit (20km/h)', 1:'Speed limit (30km/h)', 2:'Speed limit (50km/h)',
    3:'Speed limit (60km/h)', 4:'Speed limit (70km/h)', 5:'Speed limit (80km/h)',
    6:'End of speed limit (80km/h)', 7:'Speed limit (100km/h)', 8:'Speed limit (120km/h)',
    9:'No passing', 10:'No passing veh > 3.5 tons', 11:'Right-of-way at intersection',
    12:'Priority road', 13:'Yield', 14:'Stop', 15:'No vehicles', 16:'Veh > 3.5 tons prohibited',
    17:'No entry', 18:'General caution', 19:'Dangerous curve left', 20:'Dangerous curve right',
    21:'Double curve', 22:'Bumpy road', 23:'Slippery road', 24:'Road narrows on the right',
    25:'Road work', 26:'Traffic signals', 27:'Pedestrians', 28:'Children crossing',
    29:'Bicycles crossing', 30:'Beware of ice/snow', 31:'Wild animals crossing',
    32:'End speed + passing limits', 33:'Turn right ahead', 34:'Turn left ahead',
    35:'Ahead only', 36:'Go straight or right', 37:'Go straight or left', 38:'Keep right',
    39:'Keep left', 40:'Roundabout mandatory', 41:'End of no passing',
    42:'End no passing veh > 3.5 tons', 43:'No Parking', 44:'Unknown/Invalid Sign'
}

top = Tk()
top.geometry('800x600')
top.title('Traffic Sign Recognition')
top.configure(background='#CDCDCD')

label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)


def classify(file_path):
    image = cv2.imread(file_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (30, 30))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    preds = model.predict(image)
    pred = np.argmax(preds, axis=1)[0]
    confidence = float(preds[0][pred]) * 100
    sign = classes[pred]

    label.configure(
        foreground='#011638',
        text=f"{sign}\nConfidence: {confidence:.2f}%"
    )

def upload_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    uploaded = cv2.imread(file_path)
    uploaded = cv2.cvtColor(uploaded, cv2.COLOR_BGR2RGB)
    uploaded = cv2.resize(uploaded, (200, 200))

    img = ImageTk.PhotoImage(Image.fromarray(uploaded))

    sign_image.configure(image=img)
    sign_image.image = img
    label.configure(text='')

    classify_button = Button(
        top,
        text="Classify Image",
        command=lambda: classify(file_path),
        padx=10,
        pady=5
    )
    classify_button.configure(background='#364156', foreground='white')
    classify_button.place(relx=0.79, rely=0.46)

upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white')
upload.pack(side=BOTTOM, pady=50)

sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)

heading = Label(top, text="Know Your Traffic Sign", pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()

top.mainloop()
