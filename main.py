import tkinter as tk
from game import *


def main():

    def start_game():
        game()

    menu = tk.Tk()
    menu.title('Menu Snake Games')

    canvas = tk.Canvas(menu, width=500, height=500, bg='black')
    canvas.pack()
    canvas.create_text(WIDTH / 2, HEIGHT / 4, text="SNAKE GAME", fill="green", font=("Arial", 24))

    btn_start = tk.Button(menu, text="START", command=start_game, font=("Arial", 24), cursor="hand2")
    btn_start.pack()

    menu.mainloop()

if __name__ == '__main__':
    main()
