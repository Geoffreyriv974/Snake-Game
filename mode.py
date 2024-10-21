import tkinter as tk
from tkinter import Label

from game import *
from PIL import Image, ImageTk

def choice_mode():
    def start_game():
        game()

    mode = tk.Tk()
    mode.title('Menu Snake Games')
    mode.geometry('500x500')

    Game_title = tk.Label(mode, fg="green", text='Snake-Games', font=('Arial', 30))
    Game_title.pack(ipady=40)
    Label_mode = tk.Label(mode, fg="blue", text='Choice mode', font=('Arial', 20))
    Label_mode.pack(ipady=5)

    image_pomme = Image.open("image/pomme.png")

    pomme = ImageTk.PhotoImage(image_pomme)

    btn_start = tk.Button(mode, command=start_game, cursor="hand2", image=pomme)
    btn_start.pack(side=tk.LEFT, padx=50)

    btn_score = tk.Button(mode, text="SCORE", font=("Arial", 24), cursor="hand2", borderwidth=10)
    btn_score.pack(side=tk.RIGHT, padx=50)

    mode.mainloop()