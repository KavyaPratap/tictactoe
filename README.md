Tic Tac Toe GUI
Overview
This project is a GUI-based Tic Tac Toe game implemented in Python using the Tkinter library. The game features a simple interface where the player competes against the computer. The game can be played in fullscreen mode, and it provides a seamless experience with options to restart or exit after each game.

Features
Fullscreen Mode: The game starts in fullscreen mode, providing an immersive experience.
Player vs Computer: The player competes against an AI, which makes its moves based on a simple decision-making algorithm.
Responsive Design: The game board adjusts to the center of the screen regardless of screen size.
Immediate Feedback: The game updates the board and announces the winner or a draw promptly.
Restart and Exit Options: After each game, players can choose to play again or exit the game.
Getting Started
Prerequisites
Ensure you have Python installed on your system. This game is built using Python 3.x.

Installation
Clone the repository:
sh
Copy code
git clone https://github.com/yourusername/tic-tac-toe-gui.git
cd tic-tac-toe-gui
Run the game:
sh
Copy code
python tictactoe.py
How to Play
Starting the Game: Run the script to start the game in fullscreen mode.
Making a Move: Click on an empty cell to place your 'X'. The computer will automatically make its move after yours.
Winning the Game: Align three of your marks horizontally, vertically, or diagonally to win. The game will display a winning message.
Drawing: If all cells are filled without a winner, the game will announce a draw.
Restart or Exit: After each game, press 'Y' to play again or 'N' to exit.
Code Explanation
Initialization
The TicTacToeGUI class initializes the game. It sets up the main window, configures fullscreen mode, and creates the game board with buttons.

Making a Move
The make_move method handles player moves. It updates the board and checks for a winner or a draw. If the game continues, it triggers the computer's move.

Checking for a Winner
The check_winner method checks all possible winning combinations to determine if there is a winner.

Displaying Results
The display_winner and display_draw methods show the game result on the screen and disable further moves.

Computer's Move
The computer_move method decides the computer's move, prioritizing winning moves or blocking the player's winning moves.

Restart and Exit
The play_again_prompt method prompts the user to restart or exit. The restart_game and exit_game methods handle these actions.
