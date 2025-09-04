import tkinter as tk
from tkinter import ttk
import paint # Import the module containing your new window's code

def open_new_window():
    """Function to open the new window."""
    paint.create_new_window(root) # Pass the root window as master if needed

# Main window setup
root = tk.Tk()
root.title("Main Application")
root.geometry("400x300")

# Button to open new window
open_button = ttk.Button(root, text="Open New Window", command=open_new_window)
open_button.pack(pady=20)

root.mainloop()