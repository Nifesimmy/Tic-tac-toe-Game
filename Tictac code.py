import tkinter as tk
from tkinter import messagebox


# Global variables
current_player = "X"
board = [" " for _ in range(9)]
buttons = []


def on_click(index):
    global current_player
    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player, state=tk.DISABLED)
       
        if check_winner():
            show_winner()
        elif " " not in board:
            show_tie()
        else:
            switch_player()


def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != " ":
            highlight_winner(i * 3, i * 3 + 1, i * 3 + 2)
            return True
        if board[i] == board[i + 3] == board[i + 6] != " ":
            highlight_winner(i, i + 3, i + 6)
            return True
    if board[0] == board[4] == board[8] != " ":
        highlight_winner(0, 4, 8)
        return True
    if board[2] == board[4] == board[6] != " ":
        highlight_winner(2, 4, 6)
        return True
    return False


def highlight_winner(*indices):
    for index in indices:
     buttons[index].config(bg='green', fg='white')


def show_winner():
    winner = f"Player {current_player} wins!"
    messagebox.showinfo("Game Over", winner)
    reset_game()


def show_tie():
    messagebox.showinfo("Game Over", "It's a tie!")
    reset_game()


def reset_game():
    global current_player
    current_player = "X"
    for i in range(9):
        board[i] = " "
        buttons[i].config(text=" ", state=tk.NORMAL, bg='SystemButtonFace', fg='black')
    turn_label.config(text=f"Player {current_player}'s turn")


def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    turn_label.config(text=f"Player {current_player}'s turn")


def restart_game():
    result = messagebox.askyesno("Restart Game", "Do you want to restart the game?")
    if result:
        reset_game()


# Main program
window = tk.Tk()
window.title("Tic Tac Toe")


turn_label = tk.Label(window, text=f"Player {current_player}'s turn", font=('normal', 14))
turn_label.grid(row=0, column=0, columnspan=3)


for i in range(9):
    row, col = divmod(i, 3)
    button = tk.Button(window, text=" ", font=('normal', 20), width=5, height=2, command=lambda i=i: on_click(i))
    button.grid(row=row + 1, column=col)
    buttons.append(button)


restart_button = tk.Button(window, text="Restart Game", command=restart_game)
restart_button.grid(row=10, column=0, columnspan=3)


window.mainloop()
