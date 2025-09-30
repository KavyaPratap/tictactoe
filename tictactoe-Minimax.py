import tkinter as tk
import random

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe") 
        self.root.geometry("500x500")
        self.root.configure(bg='black')
        self.current_player = None
        self.board = ['-'] * 9
        self.buttons = []
        
        frame = tk.Frame(root, bg='black')
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        for i in range(9):
            row = i // 3
            col = i % 3
            button = tk.Button(frame, text='', font=('normal', 24), width=7, height=2, 
                               command=lambda i=i: self.make_move(i))
            button.grid(row=row, column=col)
            self.buttons.append(button)
            button.config(bg='black', fg='lime')
            
        if random.choice([True, False]):
            self.current_player = 'X'
        else:
            self.current_player = 'O'
            self.root.after(100, self.computer_move) 

    def make_move(self, i):
        if self.board[i] == '-' and not self.check_winner_general(self.board):
            self.board[i] = 'X'
            self.buttons[i]['text'] = 'X'
            
            if self.check_winner_general(self.board):
                self.display_winner('Player X')
                self.play_again_prompt()
            elif '-' not in self.board:
                self.display_draw()
                self.play_again_prompt()
            else:
                self.current_player = 'O'
                # Schedule computer move to allow GUI update
                self.root.after(200, self.computer_move)

    def computer_move(self):
        available_spots = [i for i, val in enumerate(self.board) if val == '-']
        
        if available_spots and not self.check_winner_general(self.board):
            # Minimax provides the optimal move
            move = self.get_best_move() 
            
            self.board[move] = 'O'
            self.buttons[move]['text'] = 'O'
            self.buttons[move].config(fg='magenta')
            
            if self.check_winner_general(self.board):
                self.display_winner('Player O (Computer)')
                self.play_again_prompt()
            elif '-' not in self.board:
                self.display_draw()
                self.play_again_prompt()
            else:
                self.current_player = 'X'

    def check_winner_general(self, board):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != '-':
                return True
        return False

    def evaluate_board(self, board):
        """
        Assigns a score to the board state for the minimax algorithm.
        
        Returns:
            10: 'O' (Computer) wins
            -10: 'X' (User) wins
            0: Game is ongoing or a draw
        """
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        
        for combo in winning_combinations:
            a, b, c = combo
            if board[a] == board[b] == board[c] != '-':
                if board[a] == 'O':
                    return 10  
                else:
                    return -10 
        return 0 

    def minimax(self, board, depth, is_maximizing):

        # Base case: Check for terminal states (win, loss, or draw)
        score = self.evaluate_board(board)
        #if we add this then we can limit the power of ai [minimax approach], else we can never win....
        # if depth > 4: 
        #     return 0 
        if score != 0:
            # Prefer quicker wins (higher score) and slower losses (less negative score)
            # The depth adjustment helps the AI choose the fastest winning path.
            return score - depth if score > 0 else score + depth
        if '-' not in board: 
            return 0 # Draw
        
        # Maximizing Player ('O' - Computer)
        if is_maximizing:
            best_score = -float('inf')

            player = 'O'
            for i in range(9):
                if board[i] == '-':
                    board[i] = player
                    score = self.minimax(board, depth + 1, False)
                    board[i] = '-'  # Undo the move (backtrack)
                    best_score = max(best_score, score)
            return best_score
        
        # Minimizing Player ('X' - User)
        else: 
            best_score = float('inf')
            player = 'X'
            for i in range(9):
                if board[i] == '-':
                    board[i] = player
                    score = self.minimax(board, depth + 1, True)
                    board[i] = '-'  # Undo the move (backtrack)
                    best_score = min(best_score, score)
            return best_score

    def get_best_move(self):
        """
        Finds the optimal move for the computer ('O') using the Minimax algorithm.
        This is a wrapper that tests each available move and uses Minimax to score it.
        """
        best_score = -float('inf')
        best_move = -1
        
        for i in range(8):#if here 9 is there instead of 8.....it would be impossible to win.
            if self.board[i] == '-':
                self.board[i] = 'O' 
                move_score = self.minimax(self.board, 0, False) 
                
                self.board[i] = '-' 
                
                if move_score > best_score:
                    best_score = move_score
                    best_move = i
                    
        if best_move == -1:
             return random.choice([i for i, val in enumerate(self.board) if val == '-'])
             
        return best_move


    def display_winner(self, winner):
        self.clear_info_display() 
        winner_label = tk.Label(self.root, text=f"{winner} wins!", font=('normal', 20), bg='black', fg='red')
        winner_label.pack(side=tk.TOP, pady=20)
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def display_draw(self):
        self.clear_info_display() 
        draw_label = tk.Label(self.root, text="It's a draw!", font=('normal', 20), bg='black', fg='orange')
        draw_label.pack(side=tk.TOP, pady=20)

    def play_again_prompt(self):
        play_again_label = tk.Label(self.root, text="Press 'Y' to play again or 'N' to exit:", font=('normal', 16), bg='black', fg='blue')
        play_again_label.pack(side=tk.TOP)
    
        self.root.bind('y', self.restart_game)
        self.root.bind('n', self.exit_game)

    def restart_game(self, event):
        self.reset_game()
        
    def exit_game(self, event):
        self.root.destroy()
        
    def reset_game(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                continue
            widget.destroy() 
            
        self.board = ['-'] * 9
        self.buttons = []
        self.__init__(self.root) 

    def clear_info_display(self):
        for widget in self.root.winfo_children():
            if not isinstance(widget, tk.Frame):
                widget.destroy()

root = tk.Tk()
tic_tac_toe = TicTacToeGUI(root)
root.mainloop()
