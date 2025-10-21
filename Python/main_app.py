import tkinter as tk #imports the other codes
import paint
import pong
import jumpgame

def open_paint(): #these functions just make it so itll run create_new_window in the other codes
    paint.create_new_window()

def open_pong():
    pong.create_new_window()

def open_jumpgame():
    jumpgame.create_new_window()



root = tk.Tk()
root.config(height=500, width=500, bg="#E8D9CD") #root/background configurations
root.title("GAME MENU")
root.geometry("400x400")

title_frame = tk.Frame(root, bg="#BBA58F", bd=3, relief="ridge") 
title_frame.pack(pady=15, padx=20, fill="x")
title_label = tk.Label(
    title_frame,
    text="calm luh games",
    bg="#BBA58F",
    fg="#6F655D",
    font=("Arial", 20, "bold")
)


title_label.pack(pady=5)
#array of buttons that will send a message to other code pieces to open 
tk.Button(root, text="chill painting", height=5, width=20, 
          bg="#BBA58F", command=open_paint).pack(pady=10)

tk.Button(root, text="calm luh pong", height=5, width=20,
          bg="#8FBBA5", command=open_pong).pack(pady=10)

tk.Button(root, text="calm luh jumping", height=5, width=20,
          bg="#959D90", command=open_jumpgame).pack(pady=10)







root.mainloop()



