
import tkinter as tk


root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

shape = canvas.create_rectangle(50, 50, 100, 100, fill="red")

def moveup(event):
    canvas.move(shape, 0, -10)
def movedown(event):
    canvas.move(shape, 0, 10)

root.bind("<Up>", moveup)
root.bind("<Down>", movedown)






root.mainloop()
