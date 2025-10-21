import tkinter as tk

def create_new_window(): #makes it so if i press the button from the menu itll launch
    drawing = False #if true, draws
    last_x, last_y = None, None
    pen_color = 'black'


    def start(event): 
        nonlocal drawing, last_x, last_y
        drawing = True #finds coords of mouse and draws
        last_x, last_y = event.x, event.y

    def stop(event): #stops drawing
        nonlocal drawing
        drawing = False

    def draw(event): 
        nonlocal last_x, last_y
        if drawing:
            x, y = event.x, event.y
            can.create_line(last_x, last_y, x, y, fill=pen_color, width=2) #actually placing down the line where drawing is true (where mouse is)
            last_x, last_y = x, y

    def changec(newc): 
        nonlocal pen_color
        pen_color = newc

  
    win = tk.Toplevel() #root and title
    win.title("Paint")

    can = tk.Canvas(win, width=1000, height=500, bg="#E8D9CD") #canvas, MAYBE ill find a way to allow user to change color of canvas
    can.pack()

    # new labeled buttons
    color_options = {
        "pen": "black",
        "eraser": "#E8D9CD",
        "red": "red",
        "blue": "blue",
        "bright green": "#00FF55",
        "yellow": "yellow",
        "evil yellow": "purple",
        "richard watterson": "#f9b6ba"
    }
    for label, color_code in color_options.items(): #buttons that will change pen color
        btn = tk.Button(win, text=label, bg=color_code,
                        command=lambda c=color_code: changec(c))
        btn.pack(side=tk.LEFT)




    can.bind("<Button-1>", start) #binds drawing to mouse clicks and holds
    can.bind("<ButtonRelease-1>", stop)
    can.bind("<B1-Motion>", draw)
