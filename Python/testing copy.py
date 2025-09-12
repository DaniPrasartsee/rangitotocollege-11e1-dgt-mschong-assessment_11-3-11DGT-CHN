#NOT MY CODE. WILL NOT BE USING THIS. FOR REFERENCE
import tkinter as tk

class Player:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = 30
        self.height = 50
        self.player_id = canvas.create_rectangle(x, y, x + self.width, y + self.height, fill="blue")

        self.gravity = 1  # Adjust this value for stronger/weaker gravity
        self.vertical_velocity = 0

    def apply_gravity(self):
        self.vertical_velocity += self.gravity
        self.y += self.vertical_velocity
        self.canvas.coords(self.player_id, self.x, self.y, self.x + self.width, self.y + self.height)

    def jump(self):
        # Only allow jumping if on the ground or a platform (you'll need collision detection for this)
        # For now, a simple jump:
        self.vertical_velocity = -10 # Negative value to move upwards

class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg="lightblue")
        self.canvas.pack()

        self.player = Player(self.canvas, 100, 500)

        # Example platform (you'd have more sophisticated platform management)
        self.platform = self.canvas.create_rectangle(50, 550, 750, 580, fill="green")

        self.root.bind("<space>", self.handle_jump) # Bind spacebar for jumping

        self.update_game()

    def handle_jump(self, event):
        self.player.jump()

    def update_game(self):
        self.player.apply_gravity()

        # Collision detection with platforms (simplified example)
        player_coords = self.canvas.coords(self.player.player_id)
        platform_coords = self.canvas.coords(self.platform)

        # If player is above platform and falling, and collides with platform
        if player_coords[3] >= platform_coords[1] and \
           player_coords[2] > platform_coords[0] and \
           player_coords[0] < platform_coords[2] and \
           self.player.vertical_velocity > 0:
            self.player.y = platform_coords[1] - self.player.height
            self.player.vertical_velocity = 0 # Stop falling
            self.canvas.coords(self.player.player_id, self.player.x, self.player.y, self.player.x + self.player.width, self.player.y + self.player.height)


        self.root.after(16, self.update_game) # Call update_game roughly 60 times per second (1000/60 = 16.66)

root = tk.Tk()
game = Game(root)
root.mainloop()