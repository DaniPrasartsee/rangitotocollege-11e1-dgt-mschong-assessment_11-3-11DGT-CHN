import tkinter as tk #i hate using this form of tkinter but its the only way i make the buttons work
#global values
drawing = False
last_x, last_y = None, None
pen_color = 'black'

def start(event):
    global drawing
    drawing = True
    global last_x, last_y
    last_x, last_y = event.x, event.y

def stop(event):
    global drawing
    drawing = False
def draw(event):
    global last_x, last_y
    
    if drawing:
        x, y = event.x, event.y
        can.create_line(last_x, last_y, event.x, event.y, fill=pen_color, width=2)
        last_x, last_y = x, y
def changec(newc):
    global pen_color
    pen_color = newc

root = tk.Tk()
root.title("Paint")

can = tk.Canvas(root, width=400, height=300, bg="white")
can.pack()

colors = ["black", "white"]

color_buttons = []
for color in colors:
    color_buttons.append(tk.Button(root, text=color.capitalize(), bg=color, command=lambda c=color: changec(c)))
    color_buttons[-1].pack(side=tk.LEFT)

can.bind("<Button-1>", start)
can.bind("<ButtonRelease-1>", stop)
can.bind("<B1-Motion>", draw)

root.mainloop()