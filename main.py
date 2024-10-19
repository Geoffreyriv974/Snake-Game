import tkinter as tk
from game import *
from score import *


def main():

    def start_game():
        game()

    menu = tk.Tk()
    menu.title('Menu Snake Games')
    menu.geometry('500x500')

    Game_title = tk.Label(menu, fg="green", text='Snake-Games', font=('Arial', 30))
    Game_title.pack(ipady=100)

    btn_start = tk.Button(menu, text="START", command=start_game, font=("Arial", 24), cursor="hand2", borderwidth=10)
    btn_start.pack(side=tk.LEFT, padx=50)
    btn_score = tk.Button(menu, text="SCORE", font=("Arial", 24), cursor="hand2", borderwidth=10)
    btn_score.pack(side=tk.RIGHT, padx=50)

    menu.mainloop()

if __name__ == '__main__':
    main()
