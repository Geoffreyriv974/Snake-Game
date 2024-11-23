import tkinter as tk
from basic_mode import *
from fast_mode import *
from double_mode import *

def stop_game():
    menu.destroy()

def start_basic_mode():
    basic_game()

def start_fast_mode():
    fast_game()

def start_dooble_mode():
    double_game()

def main():
    global menu

    menu = tk.Tk()
    menu.title('Menu Snake Game')
    menu.attributes('-fullscreen', True)
    menu.resizable(False, False)
    menu.config(bg="green")

    game_title = tk.Label(menu, fg="yellow", bg="green", text='Snake-Games', font=('Press Start 2P', 40))
    game_title.pack(ipady=70)

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
    basic_mode.bind("<Button-1>", lambda event: start_basic_mode())

    fast_mode = tk.Label(menu, fg="yellow", bg="green", text='Fast mode', font=('Press Start 2P', 25), cursor='hand2')
    fast_mode.pack()
    fast_mode.bind("<Enter>", lambda event, label=fast_mode: on_enter(event, label))
    fast_mode.bind("<Leave>", lambda event, label=fast_mode: on_leave(event, label))
    fast_mode.bind("<Button-1>", lambda event: start_fast_mode())

    dooble_mode = tk.Label(menu, fg="yellow", bg="green", text='Double mode', font=('Press Start 2P', 25), cursor='hand2')
    dooble_mode.pack()
    dooble_mode.bind("<Enter>", lambda event, label=dooble_mode: on_enter(event, label))
    dooble_mode.bind("<Leave>", lambda event, label=dooble_mode: on_leave(event, label))
    dooble_mode.bind("<Button-1>", lambda event: start_dooble_mode())

    quit_game = tk.Label(menu, fg="yellow", bg="green", text='Quit', font=('Press Start 2P', 25), cursor='hand2')
    quit_game.pack()
    quit_game.bind("<Enter>", lambda event, label=quit_game: on_enter(event, label))
    quit_game.bind("<Leave>", lambda event, label=quit_game: on_leave(event, label))
    quit_game.bind("<Button-1>", lambda event: stop_game())

    menu.mainloop()

if __name__ == '__main__':
    main()
