import tkinter as tk #I have no clue why but i wrote my code on another file and it didnt run so i pasted it here and it runs fine

class Player:
    def __init__(self, canvas, x, y):
        self.canvas = canvas  #Canvas
        self.x = x
        self.y = y
        self.width = 30
        self.height = 50
        self.player_id = canvas.create_rectangle(x, y, x + self.width, y + self.height, fill="blue") #Player
        
        self.gravity = 0.5 #Gravity (change number to change gravity strength)
        self.vertical_velocity = 0

    def apply_gravity(self):
        self.vertical_velocity += self.gravity
        self.y += self.vertical_velocity
        self.canvas.coords(self.player_id, self.x, self.y, self.x + self.width, self.y + self.height)

    def jump(self):
        # Prevents jumping on thin air n stuff
        if self.vertical_velocity == 0:
            self.vertical_velocity = -10

class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg="light blue")
        self.canvas.pack()
        
        self.player = Player(self.canvas, 100, 500)

        # Platform rectangle coordinates
        self.platform = self.canvas.create_rectangle(0, 550, 3000, 850, fill="light green")
        
        self.root.bind("<space>", self.handle_jump) 
        
        # Start the game loop
        self.update_game()

    def handle_jump(self, event):
        self.player.jump()

    def update_game(self):
        self.player.apply_gravity() #Applies gravity to player

        player_coords = self.canvas.coords(self.player.player_id)
        platform_coords = self.canvas.coords(self.platform)

        # Simple collision detection with platform (so the player doesn't just fall through the floor)
        if (player_coords[3] >= platform_coords[1] and
            player_coords[2] > platform_coords[0] and
            player_coords[0] < platform_coords[2] and
            self.player.vertical_velocity > 0):
            
            # Set player on top of platform and stop vertical velocity
            self.player.y = platform_coords[1] - self.player.height
            self.player.vertical_velocity = 0
            self.canvas.coords(self.player.player_id, self.player.x, self.player.y, self.player.x + self.player.width, self.player.y + self.player.height)

        # FPS thing i just took from another code I saw
        self.root.after(16, self.update_game)
class Obstacle:
    def __init__(self, canvas, x, y):
        self.canvas = canvas  #Canvas
        self.x = x
        self.y = y
        self.width = 30
        self.height = 50
        self.player_id = canvas.create_rectangle(x, y, x + self.width, y + self.height, fill="red") #Player

root = tk.Tk()
game = Game(root)
root.mainloop()
