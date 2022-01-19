from tkinter import *
from PIL import ImageTk, Image
root=Tk()
path1 ="images/theaters/pvr.png"

path2="images/theaters/inox.png"

path3="images/theaters/rohini.png"

image1 = Image.open(path1)
#Create an object of tkinter ImageTk
image1 = image1.resize((150,150), Image.ANTIALIAS)
my_img1 = ImageTk.PhotoImage(image1)

image2 = Image.open(path2)
#Create an object of tkinter ImageTk
image2 = image2.resize((150,150), Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(image2)

image3 = Image.open(path3)
#Create an object of tkinter ImageTk
image3 = image3.resize((150,150), Image.ANTIALIAS)
my_img3 = ImageTk.PhotoImage(image3)

images_frame=Frame(root,bd=2)
#Create a Label Widget to display the text or Image
label1 = Label(images_frame,image = my_img1).grid(row=0,column=0)

label2 = Label(images_frame,text="PVR").grid(row=0,column=2)

label3 = Label(images_frame,image = my_img2).grid(row=1,column=0)
label4 = Label(images_frame,text="INOX").grid(row=1,column=1)

label5 = Label(images_frame,image = my_img3).grid(row=2,column=0)
label6 = Label(images_frame,text="Rohini").grid(row=2,column=1)

images_frame.pack(padx=100,pady=100)
root.mainloop()