import tkinter as tk
import paint
import pong
import jumpgame




def open_paint():
    paint.create_new_window()

def open_pong():
    pong.create_new_window()

def open_jumpgame():
    jumpgame.create_new_window()

root = tk.Tk()
root.config(height=500, width=500, bg="#E8D9CD")
root.title("Menu")
root.geometry("400x400")

tk.Button(root, text="Paint", height=5, width=20,
          bg="#BBA58F", command=open_paint).pack(pady=10)

tk.Button(root, text="Pong", height=5, width=20,
          bg="#8FBBA5", command=open_pong).pack(pady=10)

tk.Button(root, text="Jump Game", height=5, width=20,
          bg="#959D90", command=open_jumpgame).pack(pady=10)

root.mainloop()


