import tkinter as tk

# Global variables to track drawing state
drawing = False
last_x, last_y = None, None
pen_color = "black"

def start_drawing(event):
    global drawing
    drawing = True
    global last_x, last_y
    last_x, last_y = event.x, event.y

def stop_drawing(event):
    global drawing
    drawing = False

def draw(event):
    global last_x, last_y

    if drawing:
        x, y = event.x, event.y
        canvas.create_line((last_x, last_y, x, y), fill=pen_color, width=2)
        last_x, last_y = x, y

def change_color(new_color):
    global pen_color
    pen_color = new_color

root = tk.Tk()
root.title("Paint Application")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

colors = ["red", "green", "blue", "black", "orange", "pink"]

color_buttons = []
for color in colors:
    color_buttons.append(tk.Button(root, text=color.capitalize(), bg=color, command=lambda c=color: change_color(c)))
    color_buttons[-1].pack(side=tk.LEFT)

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<ButtonRelease-1>", stop_drawing)
canvas.bind("<B1-Motion>", draw)

root.mainloop()