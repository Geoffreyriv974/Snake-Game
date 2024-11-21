import tkinter as tk
from game import *
from score import *
from mode import *

def main():

    def select_mode():
        game()

    def stop_game():
        menu.destroy()

    def on_enter(event, label):
        label.config(fg="#B8860B")

    def on_leave(event, label):
        label.config(fg="yellow")

    menu = tk.Tk()
    menu.title('Menu Snake Games')
    menu.attributes('-fullscreen', True)
    menu.resizable(False, False)
    menu.config(bg="green")

    game_title = tk.Label(menu, fg="yellow", bg="green", text='Snake-Games', font=('Press Start 2P', 40))
    game_title.pack(ipady=50)

    frame_score = tk.Frame(menu, bg="green")
    frame_score.pack(ipady=50)
    last_score = tk.Label(frame_score, fg="yellow", bg="green", text='Last Score: 0000', font=('Press Start 2P', 15))
    last_score.pack()
    best_score = tk.Label(frame_score, fg="yellow", bg="green", text='Best Score: 1000', font=('Press Start 2P', 15))
    best_score.pack()

    basic_mode = tk.Label(menu, fg="yellow", bg="green", text='Basic mode', font=('Press Start 2P', 25), cursor='hand2')
    basic_mode.pack()
    basic_mode.bind("<Enter>", lambda event, label=basic_mode: on_enter(event, label))
    basic_mode.bind("<Leave>", lambda event, label=basic_mode: on_leave(event, label))

    fast_mode = tk.Label(menu, fg="yellow", bg="green", text='Fast mode', font=('Press Start 2P', 25), cursor='hand2')
    fast_mode.pack()
    fast_mode.bind("<Enter>", lambda event, label=fast_mode: on_enter(event, label))
    fast_mode.bind("<Leave>", lambda event, label=fast_mode: on_leave(event, label))

    express_mode = tk.Label(menu, fg="yellow", bg="green", text='Express mode', font=('Press Start 2P', 25), cursor='hand2')
    express_mode.pack()
    express_mode.bind("<Enter>", lambda event, label=express_mode: on_enter(event, label))
    express_mode.bind("<Leave>", lambda event, label=express_mode: on_leave(event, label))

    quit_game = tk.Label(menu, fg="yellow", bg="green", text='Quit', font=('Press Start 2P', 25), cursor='hand2')
    quit_game.pack()
    quit_game.bind("<Enter>", lambda event, label=quit_game: on_enter(event, label))
    quit_game.bind("<Leave>", lambda event, label=quit_game: on_leave(event, label))
    quit_game.bind("<Button-1>", lambda event: stop_game())

    menu.mainloop()

if __name__ == '__main__':
    main()
