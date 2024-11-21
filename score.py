from tkinter import *
import mysql.connector


def score():

    board_windows = Toplevel()
    board_windows.config(bg="white")
    board_windows.title("scoreboard")
    board_windows.resizable(height=False, width=False)

    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user='root',
            password='root',
            database='Snake-game'
        )
    except mysql.connector.Error as e:
        print("Erreur lors de la connexion à la base de données :", e)
        exit()

    cursor = connection.cursor()
    query = "SELECT * FROM score ORDER BY score DESC LIMIT 10"
    cursor.execute(query)

    place_header = Label(board_windows, text='PLACE')
    place_header.grid(row=0, column=0)
    pseudo_header = Label(board_windows, text='NAME')
    pseudo_header.grid(row=0, column=1)
    score_header = Label(board_windows, text='SCORE')
    score_header.grid(row=0, column=2)
    date_header = Label(board_windows, text='DATE')
    date_header.grid(row=0, column=3)

    place = 0
    for i in cursor:
        place+=1
        place_label = Label(board_windows, text=place)
        place_label.grid(row=place+1, column=0)
        pseudo_label = Label(board_windows, text=i[1])
        pseudo_label.grid(row=place+1, column=1)
        score_label = Label(board_windows, text=i[2])
        score_label.grid(row=place+1, column=2)
        date_label = Label(board_windows, text=i[3])
        date_label.grid(row=place+1, column=3)

    cursor.close()
    connection.close()
