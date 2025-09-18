import tkinter as tk

def create_new_window():
    drawing = False
    last_x, last_y = None, None
    pen_color = 'black'

    def start(event):
        nonlocal drawing, last_x, last_y
        drawing = True
        last_x, last_y = event.x, event.y

    def stop(event):
        nonlocal drawing
        drawing = False

    def draw(event):
        nonlocal last_x, last_y
        if drawing:
            x, y = event.x, event.y
            can.create_line(last_x, last_y, x, y, fill=pen_color, width=2)
            last_x, last_y = x, y

    def changec(newc):
        nonlocal pen_color
        pen_color = newc

    win = tk.Toplevel()
    win.title("Paint")

    can = tk.Canvas(win, width=400, height=300, bg="#E8D9CD")
    can.pack()

    colors = ["black", "#E8D9CD", "red", "blue"]
    for color in colors:
        tk.Button(win, text=color.capitalize(), bg=color,
                  command=lambda c=color: changec(c)).pack(side=tk.LEFT)

    can.bind("<Button-1>", start)
    can.bind("<ButtonRelease-1>", stop)
    can.bind("<B1-Motion>", draw)

    root.mainloop()