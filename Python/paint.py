from tkinter import *


root = Tk()
canvas_height=2000
canvas_width=1500
c = Canvas(root, width=1500, height=2000)
c.pack()


def start(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y
c.bind("<Button-1>", start)


y = int(canvas_height / 2)
def draw(event):
    global last_x, last_y
    c.create_line(last_x, last_y, event.x, event.y, fill="black", width=2)
    last_x, last_y = event.x, event.y

def on_button_click():
    c.create_line(last_x, last_y, event.x, event.y, fill="white", width=4)
    last_x, last_y = event.x, event.y

switch = Button(root, text="tool", width=15, height=15, command=on_button_click)
switch.config (bg = 'black', fg = 'white')
switch.pack






c.bind("<B1-Motion>", draw)
















root.mainloop()