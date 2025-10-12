import tkinter as tk
import random

class Player:
    def __init__(self, canvas, x, y):
        self.canvas = canvas  # Canvas
        self.x = x
        self.y = y
        self.width = 30
        self.height = 50
        self.player_id = canvas.create_rectangle(x, y, x + self.width, y + self.height, fill="blue")
        
        self.gravity = 0.4  # grav strength higher number = stronger gravity
        self.vertical_velocity = 0

    def apply_gravity(self):
        self.vertical_velocity += self.gravity
        self.y += self.vertical_velocity
        self.canvas.coords(self.player_id, self.x, self.y, self.x + self.width, self.y + self.height)

    def jump(self):
        # double jump prevention
        if abs(self.vertical_velocity) < 1e-6:
            self.vertical_velocity = -10

    def get_coords(self):
        return self.canvas.coords(self.player_id) #coordinates of playing of something (if overlaps with obstacle = lose)

class Obstacle:
    def __init__(self, canvas, x, y, width=30, height=50):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.id = canvas.create_rectangle(x, y, x + width, y + height, fill="red")

    def move(self, dx):
        self.x += dx
        self.canvas.move(self.id, dx, 0)

    def get_coords(self):
        return self.canvas.coords(self.id)

    def off_left(self):
        # check if the obstacle is entirely off the left side
        x1, y1, x2, y2 = self.get_coords()
        return x2 < 0

    def destroy(self):
        self.canvas.delete(self.id)

class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg="light blue")
        self.canvas.pack()
        self.player = Player(self.canvas, 100, 500)
        self.platform = self.canvas.create_rectangle(0, 550, 3000, 850, fill="light green")
        
        root.bind("<space>", self.handle_jump)

        self.obstacles = []
        self.obstacle_speed = -5 #change speed
        self.spawn_interval = 2000 #lower number = more obstacle spawns
        self.game_over = False
        self.schedule_spawn()
        self.update_game()

    def handle_jump(self, event):
        self.player.jump()

    def schedule_spawn(self):
        if not self.game_over:
            self.spawn_obstacle()
            self.root.after(self.spawn_interval, self.schedule_spawn)

    def spawn_obstacle(self):
        plat_coords = self.canvas.coords(self.platform)
        plat_top = plat_coords[1]
        h = random.randint(30, 80)
        w = random.randint(20, 50)
        x0 = 800
        y0 = plat_top - h
        obs = Obstacle(self.canvas, x0, y0, width=w, height=h)
        self.obstacles.append(obs)

    def update_game(self):
        if self.game_over:
            return

        self.player.apply_gravity()

        player_coords = self.player.get_coords()
        platform_coords = self.canvas.coords(self.platform)
        _, py1, _, py2 = platform_coords
        if (player_coords[3] >= py1 and
            player_coords[2] > platform_coords[0] and
            player_coords[0] < platform_coords[2] and
            self.player.vertical_velocity > 0):
            self.player.y = py1 - self.player.height
            self.player.vertical_velocity = 0
            self.canvas.coords(self.player.player_id,
                               self.player.x, self.player.y,
                               self.player.x + self.player.width, self.player.y + self.player.height)

        for obs in list(self.obstacles):
            obs.move(self.obstacle_speed)
            if obs.off_left():
                obs.destroy()
                self.obstacles.remove(obs)

        pcoords = player_coords
        for obs in self.obstacles:
            ocoords = obs.get_coords()
            if (pcoords[2] > ocoords[0] and
                pcoords[0] < ocoords[2] and
                pcoords[3] > ocoords[1] and
                pcoords[1] < ocoords[3]):
                self.end_game()
                break

        self.root.after(16, self.update_game)

    def end_game(self):
        self.game_over = True
        self.canvas.create_text(400, 300, text="bruh", font=("Arial", 36), fill="black")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("if you dont know how to braid hit that follow button lets go!!!")
    game = Game(root)
    root.mainloop()