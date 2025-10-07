from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("cool")
root.iconbitmap('image/tkinter.ico')
root.geometry('600x400')

c = Image.open("python/images/chicken.png")
c = ImageTk.PhotoImage(c)

label = Label(root, image=c)
label.pack(pady=2)

root.mainloop()