
import tkinter as tk

class Player:
    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 50
        self.player_id = canvas.create_rectangle(x, y, x + self.width, y + self.height, fill="blue")
        
        self.gravity = 0.5 #gravity level
        self.vertical_velocity = 0
    def apply_gravity(self): #gravity formula i had to google
        self.vertical_velocity += self.gravity
        self.y += self.vertical_velocity
        self.canvas.coords(self.player_id, self.x, self.y, self.x + self.width, self.y + self.height)
    def jump(self):
        self.vertical_velocity = -10 #changes velocity so char goes up or smthn
class Game:
    def handle_jump(self, event):
        self.player.jump()
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg="light blue")
        self.canvas.pack()
        
        self.player = Player(self.canvas, 100, 500)

        self.platform = self.canvas.create_rectangle(0, 550, 3000,850, fill="light green")
        self.root.bind("<space>", self.handle_jump) 



root = tk.Tk()
game = Game(root)
root.mainloop()



