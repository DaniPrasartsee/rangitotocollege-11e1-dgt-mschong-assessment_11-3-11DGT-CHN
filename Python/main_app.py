import tkinter as tk
from tkinter import ttk
import paint
#import jumping

def open_new_window_from_module():
    paint.create_new_window()
def open_new_window_from_module2():
    jumping.create_new_window()

root = tk.Tk()
root.config(height = 500, width = 500, bg = "#E8D9CD")
root.title("Menu")
root.geometry("400x300")

#open_button = tk.Button(root, text="Paint", height = 10, width = 50, bg = "#BBA58F", command=open_new_window_from_module)
#open_button.pack(pady=20)
#open_button2 = tk.Button(root, text="Jumping", height = 10, width = 50, bg = "#959D90", command=open_new_window_from_module2)
#open_button2.pack(pady=20)

#root.mainloop()