<h1>Tic Tac Toe GUI</h1>

<h3>Overview</h3>
<p>This project is a GUI-based Tic Tac Toe game implemented in Python using the Tkinter library. The game features a simple interface where the player competes against the computer. The game can be played in fullscreen mode, and it provides a seamless experience with options to restart or exit after each game.</p>

<h3>Features</h3>
<ul>
    <li><strong>Fullscreen Mode</strong>: The game starts in fullscreen mode, providing an immersive experience.</li>
    <li><strong>Player vs Computer</strong>: The player competes against an AI, which makes its moves based on a simple decision-making algorithm.</li>
    <li><strong>Responsive Design</strong>: The game board adjusts to the center of the screen regardless of screen size.</li>
    <li><strong>Immediate Feedback</strong>: The game updates the board and announces the winner or a draw promptly.</li>
    <li><strong>Restart and Exit Options</strong>: After each game, players can choose to play again or exit the game.</li>
</ul>

<h3>Getting Started</h3>

<h4>Prerequisites</h4>
<p>Ensure you have Python installed on your system. This game is built using Python 3.x.</p>

<h4>Installation</h4>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/yourusername/tic-tac-toe-gui.git
cd tic-tac-toe-gui</code></pre>
    </li>
    <li>Run the game:
        <pre><code>python tictactoe.py</code></pre>
    </li>
</ol>

<h3>How to Play</h3>
<ol>
    <li><strong>Starting the Game</strong>: Run the script to start the game in fullscreen mode.</li>
    <li><strong>Making a Move</strong>: Click on an empty cell to place your 'X'. The computer will automatically make its move after yours.</li>
    <li><strong>Winning the Game</strong>: Align three of your marks horizontally, vertically, or diagonally to win. The game will display a winning message.</li>
    <li><strong>Drawing</strong>: If all cells are filled without a winner, the game will announce a draw.</li>
    <li><strong>Restart or Exit</strong>: After each game, press 'Y' to play again or 'N' to exit.</li>
</ol>

<h3>Code Explanation</h3>

<h4>Initialization</h4>
<p>The <code>TicTacToeGUI</code> class initializes the game. It sets up the main window, configures fullscreen mode, and creates the game board with buttons.</p>

<h4>Making a Move</h4>
<p>The <code>make_move</code> method handles player moves. It updates the board and checks for a winner or a draw. If the game continues, it triggers the computer's move.</p>

<h4>Checking for a Winner</h4>
<p>The <code>check_winner</code> method checks all possible winning combinations to determine if there is a winner.</p>

<h4>Displaying Results</h4>
<p>The <code>display_winner</code> and <code>display_draw</code> methods show the game result on the screen and disable further moves.</p>

<h4>Computer's Move</h4>
<p>The <code>computer_move</code> method decides the computer's move, prioritizing winning moves or blocking the player's winning moves.</p>

<h4>Restart and Exit</h4>
<p>The <code>play_again_prompt</code> method prompts the user to restart or exit. The <code>restart_game</code> and <code>exit_game</code> methods handle these actions.</p>
