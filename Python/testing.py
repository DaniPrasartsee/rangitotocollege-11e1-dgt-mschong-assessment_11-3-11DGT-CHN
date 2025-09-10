from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("test")
root.iconbitmap('images/tkinter.ico')
root.geometry('600x400')

chicken = Image.open('images/chicken.jpg')
chicken = ImageTk.PhotoImage(chicken)

my_label = Label(root, image=chicken)
my_label.pack(pady_20)

root.mainloop()