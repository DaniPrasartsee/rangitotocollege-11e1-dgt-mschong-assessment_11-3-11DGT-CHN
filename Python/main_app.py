import tkinter as tk
from tkinter import ttk
import paint
import pong

def open_new_window_from_module():
    paint.create_new_window()

root = tk.Tk()
root.config(height=500, width=500, bg="#E8D9CD")
root.title("Menu")
root.geometry("400x300")

open_button = tk.Button(root, text="Paint", height=5, width=20,
                        bg="#BBA58F", command=open_new_window_from_module)
open_button.pack(pady=20)

pong_button = tk.Button(root, text="Pong", height=5, width=20,
                        bg="#8FBBA5", command=pong.create_new_window)
pong_button.pack(pady=20)



root.mainloop()
