import tkinter as tk
import random

WIDTH = 700
HEIGHT = 560
PIECE_SIZE = 20
BASE_SNAKE_LENGTH = 2
SPEED = 75

def create_snake():
    for i in range(BASE_SNAKE_LENGTH):
        piece = game_board.create_rectangle(i * PIECE_SIZE, 0, (i + 1) * PIECE_SIZE, PIECE_SIZE, fill="green")
        snake_piece.append(piece)

def move_snake():
    x, y = get_direction_coords()
    head_coords = game_board.coords(snake_piece[0])
    new_coords = [head_coords[0] + x, head_coords[1] + y, head_coords[2] + x, head_coords[3] + y]

    new_segment = game_board.create_rectangle(new_coords, fill="green")

    snake_piece.insert(0, new_segment)
    game_board.delete(snake_piece[-1])
    snake_piece.pop()

def get_direction_coords():
    if direction == "Up":
        return 0, -PIECE_SIZE
    elif direction == "Down":
        return 0, PIECE_SIZE
    elif direction == "Left":
        return -PIECE_SIZE, 0
    elif direction == "Right":
        return PIECE_SIZE, 0
    else:
        return 0, 0

def up_snake():
    tail_coords = game_board.coords(snake_piece[-1])

    new_segment = game_board.create_rectangle(tail_coords, fill="green")
    snake_piece.append(new_segment)

def change_direction(new_direction):
    global direction

    if direction == "Up" and new_direction != "Down":
        direction = new_direction
    elif direction == "Down" and new_direction != "Up":
        direction = new_direction
    elif direction == "Left" and new_direction != "Right":
        direction = new_direction
    elif direction == "Right" and new_direction != "Left":
        direction = new_direction

def random_food():
    global food
    if food is not None:
        game_board.delete(food)

    while True:
        x = random.randint(0, (WIDTH - PIECE_SIZE) // PIECE_SIZE) * PIECE_SIZE
        y = random.randint(0, (HEIGHT - PIECE_SIZE) // PIECE_SIZE) * PIECE_SIZE

        food_coords = [x, y, x + PIECE_SIZE, y + PIECE_SIZE]
        food_collision = False

        for segment in snake_piece:
            segment_coords = game_board.coords(segment)
            if segment_coords == food_coords:
                food_collision = True
                break

        if not food_collision:
            break

    food = game_board.create_oval(x, y, x + PIECE_SIZE, y + PIECE_SIZE, fill="yellow")

def check_food_collision():
    if game_board.coords(snake_piece[0]) == game_board.coords(food):
        update_score()
        return True
    return False

def check_collision():
    head_coords = game_board.coords(snake_piece[0])

    if head_coords[0] < 0 or head_coords[2] > WIDTH or head_coords[1] < 0 or head_coords[3] > HEIGHT:
        return True

    for segment in snake_piece[1:]:
        if game_board.coords(segment) == head_coords:
            return True
    return False

def update_score():
    global score

    if check_food_collision:
        score += 1
        game_score.delete("game_score")
        game_score.create_text(70, 100/2, text="Score: " + str(score), fill="yellow", font=("Press Start 2P", 10), tags="game_score")

def func_restart_game():
    root.destroy()
    fast_game()

def end_game():

    if not check_collision():
        move_snake()
        if check_food_collision():
            up_snake()
            random_food()
        root.after(SPEED, end_game)
    else:
        game_board.create_text(WIDTH / 2, HEIGHT / 2, text="Game Over", fill="red", font=("Press Start 2P", 24))

        for segment in snake_piece:
            game_board.itemconfig(segment, fill="red")

        restart_game = tk.Label(root, bg="green", fg="yellow", text="Restart", font=("Press Start 2P", 20), cursor="hand2")
        restart_game.pack(pady=20)
        restart_game.bind("<Enter>", lambda event, label=restart_game: on_enter(event, label))
        restart_game.bind("<Leave>", lambda event, label=restart_game: on_leave(event, label))
        restart_game.bind("<Button-1>", lambda event: func_restart_game())

        stop_game = tk.Label(root, bg="green", fg="yellow", text="Quitter", font=("Press Start 2P", 20), cursor="hand2")
        stop_game.pack()
        stop_game.bind("<Enter>", lambda event, label=stop_game: on_enter(event, label))
        stop_game.bind("<Leave>", lambda event, label=stop_game: on_leave(event, label))
        stop_game.bind("<Button-1>", lambda event: func_quit_game())

        game_board.delete(food)

def press_key(event):
    change_direction(event.keysym)

def on_enter(event, label):
    label.config(fg="#B8860B")

def on_leave(event, label):
    label.config(fg="yellow")

def func_quit_game():
    root.destroy()

def fast_game():
    global food, snake_piece, direction, score, root, game_board, game_score

    snake_piece = []
    direction = "Right"
    food = None
    score = 0

    root = tk.Tk()
    root.title("Fast mode Snake Game")
    root.attributes('-fullscreen', True)
    root.resizable(False, False)
    root.config(bg="green")

    game_score = tk.Canvas(root, width=WIDTH, height=100, bg="black")
    game_score.pack()
    game_board = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
    game_board.pack()

    create_snake()
    random_food()

    root.bind("<KeyPress>", press_key)

    game_score.create_text(70, 100 / 2, text="Score: " + str(score), fill="yellow", font=("Press Start 2P", 10), tags="game_score")

    end_game()

    root.mainloop()
