import tkinter as tk
root = tk.Tk()
root.config(bg = 'black')
root.title("Game Menu")

def paint_open():
    painter = tk.Toplevel(root)
    
button1 = tk.Button(root, text="test", width=25, height=20, command= )
button1.config (bg = 'black', fg = 'white')
button1.place(x = 100, y = 100)


button2 = Button(root, text="test2", width=25, height=20)
button2.config (bg = 'black', fg = 'white')
button2.place(x = 330, y = 100)


button3 = Button(root, text="test3", width=25, height=20)
button3.config (bg = 'black', fg = 'white')
button3.place(x = 660, y = 100)


root.mainloop()
