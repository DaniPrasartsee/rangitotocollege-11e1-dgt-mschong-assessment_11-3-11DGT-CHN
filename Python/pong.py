import tkinter as tk
import random

class PongGame:
    def __init__(self, root, parent_window): 
        self.root = root
        self.parent_window = parent_window
        self.root.title("calm luh pong")
        self.canvas = tk.Canvas(root, width=800, height=500, bg="#BBA58F")
        self.canvas.pack()


        # paddle setup
        self.paddle_speed = 10
        self.paddle_width = 15
        self.paddle_height = 100
        self.left_paddle = self.canvas.create_rectangle(20, 200, 35, 300, fill="white")
        self.right_paddle = self.canvas.create_rectangle(765, 200, 780, 300, fill="white")

        # ball setup
        self.ball = self.canvas.create_oval(390, 240, 410, 260, fill="white")
        self.ball_dx = random.choice([-6, 6])
        self.ball_dy = random.choice([-4, 4])
        self.ball_speed_multiplier = 1.05
        self.max_ball_speed = 20

        # Sscore setup
        self.left_score = 0
        self.right_score = 0
        self.score_text = self.canvas.create_text(400, 50, text="0 : 0", font=("Arial", 32), fill="white")

        # smooth key pressing
        self.keys_pressed = set()
        root.bind("<KeyPress>", self.key_press)
        root.bind("<KeyRelease>", self.key_release)

        # status
        self.running = True
        self.update_game()

    def key_press(self, event):
        self.keys_pressed.add(event.keysym)

    def key_release(self, event):
        if event.keysym in self.keys_pressed:
            self.keys_pressed.remove(event.keysym)

    def move_paddles(self):
        if not self.running:
            return
        # left paddle binds
        if "w" in self.keys_pressed:
            self.move_paddle(self.left_paddle, -self.paddle_speed)
        if "s" in self.keys_pressed:
            self.move_paddle(self.left_paddle, self.paddle_speed)

        # right paddle binds
        if "Up" in self.keys_pressed:
            self.move_paddle(self.right_paddle, -self.paddle_speed)
        if "Down" in self.keys_pressed:
            self.move_paddle(self.right_paddle, self.paddle_speed)

    def move_paddle(self, paddle, dy):
        coords = self.canvas.coords(paddle)
        if coords[1] + dy >= 0 and coords[3] + dy <= 500:
            self.canvas.move(paddle, 0, dy)

    def update_game(self): #physics and stuff on ball and paddle
        if not self.running:
            return

        self.move_paddles()
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        bx1, by1, bx2, by2 = self.canvas.coords(self.ball)

        if by1 <= 0 or by2 >= 500:
            self.ball_dy *= -1

        if self.check_collision(self.left_paddle):
            self.ball_dx = abs(self.ball_dx)
            self.increase_speed()

        elif self.check_collision(self.right_paddle):
            self.ball_dx = -abs(self.ball_dx)
            self.increase_speed()

        # scoring
        if bx1 <= 0:
            self.right_score += 1
            self.update_score()
            self.reset_ball(direction=1)
        elif bx2 >= 800:
            self.left_score += 1
            self.update_score()
            self.reset_ball(direction=-1)

        # win
        if self.left_score >= 10 or self.right_score >= 10:
            self.game_over()
            return

        self.root.after(16, self.update_game)  # smooth 60fps updates

    def check_collision(self, paddle):
        bx1, by1, bx2, by2 = self.canvas.coords(self.ball)
        px1, py1, px2, py2 = self.canvas.coords(paddle)
        return bx2 > px1 and bx1 < px2 and by2 > py1 and by1 < py2

    def increase_speed(self):
        self.ball_dx *= self.ball_speed_multiplier
        self.ball_dy *= self.ball_speed_multiplier
        # speed cap so the ball doesnt end up resetting the universe
        self.ball_dx = max(-self.max_ball_speed, min(self.ball_dx, self.max_ball_speed))
        self.ball_dy = max(-self.max_ball_speed, min(self.ball_dy, self.max_ball_speed))

    def reset_ball(self, direction): 
        self.canvas.coords(self.ball, 390, 240, 410, 260)
        self.ball_dx = direction * random.choice([6, 7])
        self.ball_dy = random.choice([-4, 4])

    def update_score(self):
        self.canvas.itemconfig(self.score_text, text=f"{self.left_score} : {self.right_score}")

    def game_over(self):
        self.running = False
        winner = "Left Player" if self.left_score >= 5 else "Right Player"
        self.canvas.create_text(400, 250, text=f"{winner} wins", font=("Arial", 36), fill="yellow")

        restart_btn = tk.Button(self.root, text="restart", font=("Arial", 16),
                                bg="#444", fg="white", command=self.restart_game)
        restart_btn.place(x=350, y=300)

    def restart_game(self): #restart mech from jumpgame
        self.root.destroy()
        create_new_window()


def create_new_window():
    win = tk.Toplevel()
    PongGame(win, win)
