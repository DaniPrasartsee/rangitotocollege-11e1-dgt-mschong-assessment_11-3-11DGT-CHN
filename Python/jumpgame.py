import tkinter as tk
import random

class Player:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = 30
        self.height = 50
        self.player_id = canvas.create_rectangle(x, y, x + self.width, y + self.height, fill="blue")
        self.gravity = 0.4
        self.vertical_velocity = 0
        self.fast_fall = False  # whether the player is holding down

    def apply_gravity(self):
        # use stronger gravity when fast falling
        effective_gravity = self.gravity * (3 if self.fast_fall else 1)
        self.vertical_velocity += effective_gravity
        self.y += self.vertical_velocity
        self.canvas.coords(self.player_id, self.x, self.y, self.x + self.width, self.y + self.height)

    def jump(self):
        # jump only when on ground (no double jump)
        if abs(self.vertical_velocity) < 1e-6:
            self.vertical_velocity = -10

    def get_coords(self):
        return self.canvas.coords(self.player_id)


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
        x1, y1, x2, y2 = self.get_coords()
        return x2 < 0

    def destroy(self):
        self.canvas.delete(self.id)


class Game:
    def __init__(self, root, parent_window):
        self.root = root
        self.parent_window = parent_window
        self.canvas = tk.Canvas(root, width=800, height=600, bg="#BBA58F")
        self.canvas.pack()
        self.platform = self.canvas.create_rectangle(0, 550, 3000, 850, fill="#76593C")

        self.player = Player(self.canvas, 100, 500)
        self.obstacles = []
        self.obstacle_speed = -5
        self.spawn_interval = 2000
        self.game_over = False
        self.replay_button = None

        # key bindings for jumping and fast drop
        root.bind("<space>", self.handle_jump)
        root.bind("<KeyPress-w>", self.handle_jump)
        root.bind("<KeyPress-Up>", self.handle_jump)
        root.bind("<KeyPress-s>", self.handle_fastfall_press)
        root.bind("<KeyPress-Down>", self.handle_fastfall_press)
        root.bind("<KeyRelease-s>", self.handle_fastfall_release)
        root.bind("<KeyRelease-Down>", self.handle_fastfall_release)

        self.schedule_spawn()
        self.update_game()

    def handle_jump(self, event):
        if not self.game_over:
            self.player.jump()

    def handle_fastfall_press(self, event):
        if not self.game_over:
            self.player.fast_fall = True

    def handle_fastfall_release(self, event):
        self.player.fast_fall = False

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

        # landing logic
        if (player_coords[3] >= py1 and
            player_coords[2] > platform_coords[0] and
            player_coords[0] < platform_coords[2] and
            self.player.vertical_velocity > 0):
            self.player.y = py1 - self.player.height
            self.player.vertical_velocity = 0
            self.canvas.coords(self.player.player_id,
                               self.player.x, self.player.y,
                               self.player.x + self.player.width, self.player.y + self.player.height)

        # move obstacles
        for obs in list(self.obstacles):
            obs.move(self.obstacle_speed)
            if obs.off_left():
                obs.destroy()
                self.obstacles.remove(obs)

        # check collision
        pcoords = player_coords
        for obs in self.obstacles:
            ocoords = obs.get_coords()
            if (pcoords[2] > ocoords[0] and
                pcoords[0] < ocoords[2] and
                pcoords[3] > ocoords[1] and
                pcoords[1] < ocoords[3]):
                self.end_game()
                return

        self.root.after(16, self.update_game)

    def end_game(self):
        self.game_over = True
        self.canvas.create_text(400, 250, text="Game Over!", font=("Arial", 36), fill="black")
        self.replay_button = tk.Button(self.root, text="Restart", font=("Arial", 18),
                                       bg="#BBA58F", command=self.restart_game)
        self.replay_button.place(x=350, y=320)

    def restart_game(self):
        # close current window and open new one
        self.root.destroy()
        create_new_window()


def create_new_window():
    win = tk.Toplevel()
    win.title("Jump Game")
    Game(win, win)
