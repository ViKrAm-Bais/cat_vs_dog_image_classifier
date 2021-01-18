from tkinter import *
from PIL import Image,ImageTk
import os
from tkinter import filedialog
import glob
import pickle
import math
import tensorflow as tf
import numpy as np
import cv2

blue1 = "#d3e7ee"
blue2 = "#abd1dc"
blue3 = "#7097a8"
blue4 = "#5b84c4"
fln=""
re_st="result"

root = Tk()
root.geometry("1920x1080")
frame0 = Frame(root)                                                          #frame0
frame0.pack(side=TOP, pady=0)

frame1 = Frame(root, borderwidth=4)                                          #frame1
frame1.pack(side=LEFT, pady=0, padx=300)
heading = Label(frame0,text="Image Classifier",fg="black",font="arial 50 bold",pady=10)
heading.pack()
def sig(val):
    return 1/(1+math.exp(-val))
def prediction():
    new_model = tf.keras.models.load_model('my_model_100.h5')
    img = cv2.imread(fln)
    img = cv2.resize(img, (150,150))
    res = new_model.predict(np.array([img]) / 255)
    global re_st
    if(res[0][0]>res[0][1]):
        kk = sig(res[0][0])
        kkk = sig(res[0][1])
        re_st = "Cat "#+str(round(kk*100,2))+" "+str(round(kkk*100,2))
    else:
        kk = sig(res[0][0])
        kkk = sig(res[0][1])
        re_st = "Dog "#+str(round(kk*100,2))+" "+str(round(kkk*100,2))
    #e1.update()
    e1.configure(text=re_st)
    e1.delete(0,END)
    e1.insert(0,re_st)
    return

def update_image():
    global fln
    global photo
    fln = filedialog.askopenfilename(initialdir=os.getcwd(),
                                     title="Select Image File",
                                     filetypes=(("JPG File", "*.jpg"),
                                                ("PNG File", "*.png"),
                                                ("JPEG File", "*.jpeg"),
                                                ("All Files", "*.*")))
    re_st = "result"
    e1.configure(text=re_st)
    e1.delete(0, END)
    e1.insert(0, re_st)
    image = Image.open(fln)
    image = image.resize((500, 500))
    photo = ImageTk.PhotoImage(image)
    photo_l.update()
    photo_l.configure(image=photo)
    photo_l.image = photo
    return

image  = Image.open("upload.jpg")
image = image.resize((500,500))
photo = ImageTk.PhotoImage(image)
photo_l = Label(frame1,image=photo, )
photo_l.pack(pady =0)

frame2 = Frame(root, borderwidth=1 )                                     #frame2
frame2.pack(side=LEFT, pady=0, padx=100)

b0 = Button(frame2, fg="white",bg=blue3, text="Exit", font="arial 20 bold",padx=10,pady=8,command=lambda: exit())
b0.pack(side = BOTTOM,pady=20)
b1 = Button(frame2, fg="white",bg=blue3, text="Predict", font="arial 20 bold",padx=10,pady=8, command=prediction)
b1.pack(side = BOTTOM, pady=20)
b2 = Button(frame2, fg="white",bg=blue3, text="Browse Image", font="arial 20 bold",bd=1,padx=10,pady=8, command=update_image)
b2.pack(side = BOTTOM,pady=20)

e1 = Entry(frame2, fg="white",bg=blue3, font="arial 20 italic")
e1.pack(side = BOTTOM,pady=20)
e1.insert(0,re_st)

root.mainloop()
