import socket
import threading
import tkinter as tk
from tic_tac_toe import TicTacToe

class Client:
    def __init__(self, server_ip, port=65432):
        self.server_ip = server_ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server_ip, self.port))
        print("Connected to the server!")
        self.root = tk.Tk()
        self.game = TicTacToe(self.root, 'O', self.send_move)
        threading.Thread(target=self.receive_moves, daemon=True).start()
        self.root.mainloop()

    def send_move(self, idx):
        self.sock.sendall(str(idx).encode())

    def receive_moves(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            idx = int(data.decode())
            self.game.opponent_move(idx)

if __name__ == "__main__":
    server_ip = input("Enter Server IP: ")
    Client(server_ip)
