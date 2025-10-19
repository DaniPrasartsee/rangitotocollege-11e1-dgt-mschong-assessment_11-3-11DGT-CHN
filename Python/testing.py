from tkinter import *
from tkinter import PhotoImage

app = Tk()

image_file =PhotoImage(file="chicken.png")
image_label = Label(app, image=image_file)
image_label.image = image_file
image_label.pack()
app.mainloop()