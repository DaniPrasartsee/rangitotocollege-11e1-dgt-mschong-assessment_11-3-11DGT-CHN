from tkinter import *

root = Tk()

photo = PhotoImage(file="chicken.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()