import socket
import threading
import tkinter as tk
from tic_tac_toe import TicTacToe

class Server:
    def __init__(self, host='0.0.0.0', port=65432):
        self.host = host
        self.port = port
        self.conn = None
        self.root = tk.Tk()
        self.game = TicTacToe(self.root, 'X', self.send_move)
        threading.Thread(target=self.start_server, daemon=True).start()
        self.root.mainloop()

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen(1)
            print("Waiting for opponent to connect...")
            self.conn, addr = s.accept()
            print(f"Opponent connected from {addr}")
            threading.Thread(target=self.receive_moves, daemon=True).start()

    def send_move(self, idx):
        if self.conn:
            self.conn.sendall(str(idx).encode())

    def receive_moves(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            idx = int(data.decode())
            self.game.opponent_move(idx)

if __name__ == "__main__":
    Server()
