import tkinter as tk
import random

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg='black')

        self.current_player = None  
        self.board = ['-'] * 9
        self.buttons = []
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = screen_width // 2
        center_y = screen_height // 2

        frame = tk.Frame(root, bg='black')
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        for i in range(9):
            row = i // 3
            col = i % 3
            button = tk.Button(frame, text='', font=('normal', 24), width=7, height=2, command=lambda i=i: self.make_move(i))
            button.grid(row=row, column=col)
            self.buttons.append(button)
            button.config(bg='black', fg='lime')

        if random.choice([True, False]):
            self.current_player = 'X'
        else:
            self.current_player = 'O'
            self.computer_move()

    def make_move(self, i):
        if self.board[i] == '-' and not self.check_winner():
            self.board[i] = 'X'
            self.buttons[i]['text'] = 'X'
            if self.check_winner():
                self.display_winner('Player X')
                self.play_again_prompt()
            elif '-' not in self.board:
                self.display_draw()
                self.play_again_prompt()
            else:
                self.current_player = 'O'
                self.computer_move()

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '-':
                return True
        return False

    def display_winner(self, winner):
        winner_label = tk.Label(root, text=f"{winner} wins!", font=('normal', 20), bg='black', fg='red')
        winner_label.pack()
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def display_draw(self):
        draw_label = tk.Label(root, text="It's a draw!", font=('normal', 20), bg='black', fg='orange')
        draw_label.pack()

    def computer_move(self):
        available_spots = [i for i, val in enumerate(self.board) if val == '-']
        if available_spots:
            move = self.get_best_move()
            self.board[move] = 'O'
            self.buttons[move]['text'] = 'O'
            self.buttons[move].config(fg='magenta')
            if self.check_winner():
                self.display_winner('Player O')
                self.play_again_prompt()
            elif '-' not in self.board:
                self.display_draw()
                self.play_again_prompt()
            else:
                self.current_player = 'X'
    def get_best_move(self):
        for i in range(9):
            if self.board[i] == '-':
                self.board[i] = 'O'
                if self.check_winner():
                    self.board[i] = '-'
                    return i
                self.board[i] = '-'
        for i in range(9):
            if self.board[i] == '-':
                self.board[i] = 'X'
                if self.check_winner():
                    self.board[i] = '-'
                    return i
                self.board[i] = '-'
        return random.choice([i for i, val in enumerate(self.board) if val == '-'])
    def play_again_prompt(self):
        play_again_label = tk.Label(root, text="Press 'Y' to play again or 'N' to exit:", font=('normal', 16), bg='black', fg='blue')
        play_again_label.pack()
    
        root.bind('y', self.restart_game)
        root.bind('n', self.exit_game)

    def restart_game(self, event):
        self.reset_game()
    def exit_game(self, event):
        root.destroy()
    def reset_game(self):
        for button in self.buttons:
            button.config(state=tk.NORMAL, text='')
        self.board = ['-'] * 9
        self.current_player = 'X'
        self.clear_winner_display()

    def clear_winner_display(self):
        for widget in root.winfo_children():
            widget.destroy()
        self.__init__(root)
root = tk.Tk()
tic_tac_toe = TicTacToeGUI(root)
root.mainloop()
