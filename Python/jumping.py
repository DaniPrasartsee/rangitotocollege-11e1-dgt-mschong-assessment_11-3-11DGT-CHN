
import tkinter as tk

class Player:
    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y

        self.player_id = canvas.create_rectangle(x, y, width = 30, height = 30, fill="blue")
        self.gravity = 0.5
        self.vertical_velocity = 0
    def apply_gravity(self):
        self.vertical_velocity += self.gravity
        self.y += self.vertical_velocity
        self.canvas.coords(self.player_id, self.x, self.y, self.x + self.width, self.y + self.height)
    def jump(self):
        self.vertical_velocity = -10
class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()
        


        self.platform = self.canvas.create_rectangle(0, 550, 3000,850, fill="green")


root = tk.Tk()
game = Game(root)
root.mainloop()



