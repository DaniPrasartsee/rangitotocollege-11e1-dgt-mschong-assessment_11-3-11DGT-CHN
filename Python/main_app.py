import tkinter as tk
from tkinter import ttk
import paint # Import the module containing the new window function

def open_new_window_from_module():
    """Function to open the new window defined in another module."""
    paint.create_new_window()

# Create the main window
root = tk.Tk()
root.title("Main Application")
root.geometry("400x300")

# Create a button to open the new window
open_button = ttk.Button(root, text="Open New Window", command=open_new_window_from_module)
open_button.pack(pady=20)

root.mainloop()