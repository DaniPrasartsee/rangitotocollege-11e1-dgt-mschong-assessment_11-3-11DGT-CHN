
import tkinter as tk

class Player:
    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y

        self.player_id = canvas.create_rectangle(x, y, width = 30, height = 30, fill="blue")

class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()
        


        self.platform = self.canvas.create_rectangle(0, 550, 3000,850, fill="white")


root = tk.Tk()
game = Game(root)
root.mainloop()



