import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root, player_symbol, on_move_callback):
        self.root = root
        self.root.title(f"Tic Tac Toe - You are {player_symbol}")
        self.player_symbol = player_symbol
        self.opponent_symbol = 'O' if player_symbol == 'X' else 'X'
        self.on_move_callback = on_move_callback
        self.my_turn = player_symbol == 'X'
        self.board = [''] * 9
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text='', font=('Arial', 32), width=5, height=2,
                               command=lambda idx=i: self.make_move(idx))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def make_move(self, idx):
        if self.my_turn and self.board[idx] == '':
            self.update_board(idx, self.player_symbol)
            self.on_move_callback(idx)
            self.my_turn = False
            self.check_game_over()

    def opponent_move(self, idx):
        self.update_board(idx, self.opponent_symbol)
        self.my_turn = True
        self.check_game_over()

    def update_board(self, idx, symbol):
        self.board[idx] = symbol
        self.buttons[idx].config(text=symbol, state='disabled')

    def check_game_over(self):
        winner = self.check_winner()
        if winner or '' not in self.board:
            self.end_game(winner)

    def check_winner(self):
        conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in conditions:
            if self.board[a] == self.board[b] == self.board[c] != '':
                return self.board[a]
        return None

    def end_game(self, winner):
        if winner:
            msg = f"{winner} wins!"
        else:
            msg = "It's a draw!"
        messagebox.showinfo("Game Over", msg)
        self.reset_board()

    def reset_board(self):
        self.board = [''] * 9
        for button in self.buttons:
            button.config(text='', state='normal')
        self.my_turn = self.player_symbol == 'X'
