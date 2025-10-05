from tkinter import *
from PIL import Image, Image

root = Tk()
root.title("cool")
root.iconbitmap('image/tkinter.ico')
root.geometry('600x400')

c = Image.open("C:\Users\196615\rangitotocollege-11e1-dgt-mschong-assessment_11-3-11DGT-CHN\Python\chicken.png")
c = ImageTk.PhotoImage(c)

label = Label(root, image=c)
label.pack(pady=2)