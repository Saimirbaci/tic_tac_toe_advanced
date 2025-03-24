# Advanced Network Tic-Tac-Toe

A Python-based advanced Tic-Tac-Toe game allowing two players to compete over a local network (LAN) with an intuitive graphical user interface built using `tkinter`. The game leverages sockets for seamless network connectivity and threading to maintain a responsive GUI.

## Features

- **Local Network Multiplayer**: Play Tic-Tac-Toe across two devices connected via LAN.
- **Responsive GUI**: Interactive and user-friendly interface developed with Tkinter.
- **Socket Programming**: Reliable network connection using TCP sockets.
- **Threading**: Ensures GUI responsiveness during gameplay.
- **Class-Based Design**: Clean and maintainable code structure.

## File Structure

```
tic_tac_toe_network/
├── tic_tac_toe.py
├── server.py
└── client.py
```

## Requirements

- Python 3.x
- Standard libraries only (no external packages required)

## Running the Game

### Step 1: Clone or Download

Clone this repository or download the files directly to your computer.

```bash
git clone https://github.com/your-repository/tic_tac_toe_network.git
cd tic_tac_toe_network
```

### Step 2: Run the Server

On the host machine (server):

```bash
python server.py
```

The server waits for a client connection and will indicate when a connection has been established.

### Step 3: Run the Client

On the client machine:

```bash
python client.py
```

Enter the server's IP address when prompted:

```
Enter Server IP: <Server IP Address>
```

Once connected, gameplay begins immediately.

## Gameplay

- The **Server** always plays first (`X`).
- The **Client** plays second (`O`).
- Click on an empty square to make your move.
- The game checks for win conditions or draw automatically.

## Screenshots

*(Add screenshots here to illustrate gameplay if desired)*

## Contributing

Contributions and improvements are welcome. Please open issues or submit pull requests.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.