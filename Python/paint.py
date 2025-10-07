import tkinter as tk

def create_new_window(): #creates new window from menu
    drawing = False #detects if drawing
    last_x, last_y = None, None
    pen_color = 'black'

    def start(event):
        nonlocal drawing, last_x, last_y #coordinates of mouse
        drawing = True #makes drawing true
        last_x, last_y = event.x, event.y 

    def stop(event):
        nonlocal drawing #stops drawing 
        drawing = False

    def draw(event):
        nonlocal last_x, last_y #actually places down lines and stuff at coordinates if drawing is on/true
        if drawing:
            x, y = event.x, event.y
            can.create_line(last_x, last_y, x, y, fill=pen_color, width=2)
            last_x, last_y = x, y

    def changec(newc):
        nonlocal pen_color
        pen_color = newc

    win = tk.Toplevel()
    win.title("Paint")

    can = tk.Canvas(win, width=1000, height=500, bg="#E8D9CD")
    can.pack()

    colors = ["black", "#E8D9CD", "red", "blue"] #button to change colors 
    for color in colors:
        tk.Button(win, text=color.capitalize(), bg=color,
                  command=lambda c=color: changec(c)).pack(side=tk.LEFT)

    can.bind("<Button-1>", start) #mouse held bind
    can.bind("<ButtonRelease-1>", stop) #mouse let go bind
    can.bind("<B1-Motion>", draw) #mouse movement bind

    root.mainloop()