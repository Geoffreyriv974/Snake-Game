import tkinter as tk
import random
from io import text_encoding

WIDTH = 500
HEIGHT = 500
PIECE_SIZE = 20
BASE_SNAKE_LENGTH = 2


def game():
    global food, snake_piece, direction, score

    snake_piece = []
    direction = "Right"
    food = None
    score = 0

    def create_snake():
        for i in range(BASE_SNAKE_LENGTH):
            piece = canvas.create_rectangle(i * PIECE_SIZE, 0, (i + 1) * PIECE_SIZE, PIECE_SIZE, fill="green")
            snake_piece.append(piece)

    def move_snake():
        x, y = get_direction_coords()
        head_coords = canvas.coords(snake_piece[0])
        new_coords = [head_coords[0] + x, head_coords[1] + y, head_coords[2] + x, head_coords[3] + y]

        new_segment = canvas.create_rectangle(new_coords, fill="green")


        snake_piece.insert(0, new_segment)
        canvas.delete(snake_piece[-1])
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

    def up_snake():
        tail_coords = canvas.coords(snake_piece[-1])

        new_segment = canvas.create_rectangle(tail_coords, fill="green")
        snake_piece.append(new_segment)

    def random_food():
        global food
        if food is not None:
            canvas.delete(food)
        x = random.randint(0, (WIDTH - PIECE_SIZE) // PIECE_SIZE) * PIECE_SIZE
        y = random.randint(0, (HEIGHT - PIECE_SIZE) // PIECE_SIZE) * PIECE_SIZE
        food = canvas.create_oval(x, y, x + PIECE_SIZE, y + PIECE_SIZE, fill="red")

    def check_food_collision():
        if canvas.coords(snake_piece[0]) == canvas.coords(food):
            update_score()
            return True
        return False

    def check_collision():
        head_coords = canvas.coords(snake_piece[0])

        if head_coords[0] < 0 or head_coords[2] > WIDTH or head_coords[1] < 0 or head_coords[3] > HEIGHT:
            return True

        for segment in snake_piece[1:]:
            if canvas.coords(segment) == head_coords:
                return True
        return False

    def update_score():
        global score
        if check_food_collision:
            score += 10
            print(f"Score: {score}")

    def restart_game():
        root.destroy()
        game()

    def end_game():
        if not check_collision():
            move_snake()
            if check_food_collision():
                up_snake()
                random_food()
            root.after(150, end_game)
        else:
            canvas.create_text(WIDTH / 2, HEIGHT / 2, text="Game Over", fill="red", font=("Arial", 24))
            canvas.create_text(WIDTH / 2, HEIGHT / 1.5, text="Score: " + str(score), fill="blue", font=("Arial", 24))
            btn_restart = tk.Button(root, bg="green", fg="white", text="Restart", font=("Arial, 15"), cursor="hand2", command=restart_game)
            btn_restart.pack()
            canvas.delete(food)


    def press_key(event):
        change_direction(event.keysym)

    root = tk.Tk()
    root.title("Snake")

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
    canvas.pack()

    create_snake()
    random_food()

    root.bind("<KeyPress>", press_key)

    end_game()

    root.mainloop()
