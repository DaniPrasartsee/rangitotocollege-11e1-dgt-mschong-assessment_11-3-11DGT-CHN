import tkinter as tk
from tkinter import PhotoImage

app = tk.Tk()

image_file = PhotoImage(file="C:\Users\dani_\rangitotocollege-11e1-dgt-mschong-assessment_11-3-11DGT-CHN\Python\chicken.png")
image_file = image_file.subsample(2,2)
image = tk.Label(app, image=image_file)
image.pack()

app.mainloop()