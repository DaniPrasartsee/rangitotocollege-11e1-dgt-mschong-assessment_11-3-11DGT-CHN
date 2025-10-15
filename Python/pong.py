import tkinter as tk

def create_new_window():
    drawing = False
    last_x, last_y = None, None
    pen_color = 'black'

    def start(event):
        nonlocal drawing, last_x, last_y
        drawing = True
        last_x, last_y = event.x, event.y

    def stop(event):
        nonlocal drawing
        drawing = False

    def draw(event):
        nonlocal last_x, last_y
        if drawing:
            x, y = event.x, event.y
            can.create_line(last_x, last_y, x, y, fill=pen_color, width=2)
            last_x, last_y = x, y

    def changec(newc):
        nonlocal pen_color
        pen_color = newc

  
    win = tk.Toplevel()
    win.title("Paint")

    can = tk.Canvas(win, width=1000, height=500, bg="#E8D9CD")
    can.pack()

    # new labeled buttons
    color_options = {
        "pen": "black",
        "eraser": "#E8D9CD",
        "red": "red",
        "blue": "blue"
    }
    for label, color_code in color_options.items():
        btn = tk.Button(win, text=label, bg=color_code,
                        command=lambda c=color_code: changec(c))
        btn.pack(side=tk.LEFT)

    can.bind("<Button-1>", start)
    can.bind("<ButtonRelease-1>", stop)
    can.bind("<B1-Motion>", draw)



import tkinter as tk
import random

def create_new_window():
    # makes game window 
    win = tk.Toplevel()
    win.title("Pong")
    win.config(bg="#222")
    win.resizable(False, False)

    # canvas
    WIDTH, HEIGHT = 800, 500
    canvas = tk.Canvas(win, width=WIDTH, height=HEIGHT, bg="black", highlightthickness=0)
    canvas.pack()

    # paddle and ball creation
    paddle_w, paddle_h = 15, 100
    ball_size = 20

    left_paddle = canvas.create_rectangle(30, HEIGHT/2 - paddle_h/2,
                                          30 + paddle_w, HEIGHT/2 + paddle_h/2,
                                          fill="white")

    right_paddle = canvas.create_rectangle(WIDTH - 30 - paddle_w, HEIGHT/2 - paddle_h/2,
                                           WIDTH - 30, HEIGHT/2 + paddle_h/2,
                                           fill="white")

    ball = canvas.create_oval(WIDTH/2 - ball_size/2, HEIGHT/2 - ball_size/2,
                              WIDTH/2 + ball_size/2, HEIGHT/2 + ball_size/2,
                              fill="white")

   
    ball_dx = random.choice([-4, 4])
    ball_dy = random.choice([-3, 3])
    left_speed = 0
    right_speed = 0
    score_left = 0
    score_right = 0

    score_text = canvas.create_text(WIDTH/2, 40, text="0   0", font=("Courier", 32), fill="white")

    # horrid movement logic system i just googled
    def move_paddles():
        canvas.move(left_paddle, 0, left_speed)
        canvas.move(right_paddle, 0, right_speed)
        # Keep paddles on screen
        for paddle in [left_paddle, right_paddle]:
            x1, y1, x2, y2 = canvas.coords(paddle)
            if y1 < 0:
                canvas.move(paddle, 0, -y1)
            elif y2 > HEIGHT:
                canvas.move(paddle, 0, HEIGHT - y2)

    def move_ball():
        nonlocal ball_dx, ball_dy, score_left, score_right
        canvas.move(ball, ball_dx, ball_dy)
        bx1, by1, bx2, by2 = canvas.coords(ball)

        # bounce and other stuff
        if by1 <= 0 or by2 >= HEIGHT:
            ball_dy *= -1

        if check_collision(ball, left_paddle) and ball_dx < 0:
            ball_dx *= -1
        elif check_collision(ball, right_paddle) and ball_dx > 0:
            ball_dx *= -1

        # score
        if bx1 <= 0:
            score_right += 1
            update_score()
            reset_ball()
        elif bx2 >= WIDTH:
            score_left += 1
            update_score()
            reset_ball()

    def check_collision(ball, paddle):
        bx1, by1, bx2, by2 = canvas.coords(ball)
        px1, py1, px2, py2 = canvas.coords(paddle)
        return (bx2 >= px1 and bx1 <= px2 and by2 >= py1 and by1 <= py2)

    def update_score():
        canvas.itemconfig(score_text, text=f"{score_left}   {score_right}")

    def reset_ball():
        nonlocal ball_dx, ball_dy
        canvas.coords(ball, WIDTH/2 - ball_size/2, HEIGHT/2 - ball_size/2,
                      WIDTH/2 + ball_size/2, HEIGHT/2 + ball_size/2)
        ball_dx = random.choice([-4, 4])
        ball_dy = random.choice([-3, 3])

    # binds
    def key_press(event):
        nonlocal left_speed, right_speed
        if event.keysym == "w":
            left_speed = -6
        elif event.keysym == "s":
            left_speed = 6
        elif event.keysym == "Up":
            right_speed = -6
        elif event.keysym == "Down":
            right_speed = 6

    def key_release(event):
        nonlocal left_speed, right_speed
        if event.keysym in ("w", "s"):
            left_speed = 0
        elif event.keysym in ("Up", "Down"):
            right_speed = 0

    win.bind("<KeyPress>", key_press)
    win.bind("<KeyRelease>", key_release)

    def game_loop():
        move_paddles()
        move_ball()
        win.after(16, game_loop)  # fps thing

    game_loop()
