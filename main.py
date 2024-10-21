import tkinter as tk
from game import *
from score import *
from mode import *

def main():

    def select_mode():
        choice_mode()

    menu = tk.Tk()
    menu.title('Menu Snake Games')
    menu.geometry('500x500')

    Game_title = tk.Label(menu, fg="green", text='Snake-Games', font=('Arial', 30))
    Game_title.pack(ipady=100)

    btn_start = tk.Button(menu, text="START", command=select_mode, font=("Arial", 24), cursor="hand2", borderwidth=10)
    btn_start.pack(side=tk.LEFT, padx=50)

    btn_score = tk.Button(menu, text="SCORE", font=("Arial", 24), cursor="hand2", borderwidth=10)
    btn_score.pack(side=tk.RIGHT, padx=50)

    # image_pomme = Image.open("image/pomme.png")
    # image_pomme = image_pomme.resize((20, 20))

    # pommes = ImageTk.PhotoImage(image_pomme)
    # canvas = tk.Canvas(menu, width=500, height=500)
    # canvas.create_image(500/2, 500/2, image=pommes)

    # canvas.image = pommes

    # canvas.pack()

    menu.mainloop()

if __name__ == '__main__':
    main()
