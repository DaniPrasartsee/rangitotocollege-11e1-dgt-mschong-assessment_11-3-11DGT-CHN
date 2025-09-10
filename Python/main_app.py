import tkinter as tk
from tkinter import ttk
import paint
import jumping

def open_new_window_from_module():
    paint.create_new_window()
def open_new_window_from_module2():
    jumping.create_new_window()

root = tk.Tk()
root.title("Menu")
root.geometry("400x300")

open_button = ttk.Button(root, text="Paint", command=open_new_window_from_module)
open_button.pack(pady=20)
open_button2 = ttk.Button(root, text="Jumping", command=open_new_window_from_module2)
open_button2.pack(pady=20)

root.mainloop()