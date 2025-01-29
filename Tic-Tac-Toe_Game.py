# import numpy as np
# import matplotlib.pyplot as plt

# class TicTacToe:
#     def __init__(self):
#         self.board = np.zeros((3, 3))
#         self.current_player = 1
#         self.fig, self.ax = plt.subplots(figsize=(5, 5))
#         self.game_over = False
#         self.draw_board()

#     def draw_board(self):
#         self.ax.clear()
#         for row in range(4):
#             self.ax.plot([row, row], [0, 3], color="black")
#             self.ax.plot([0, 3], [row, row], color="black")
        
#         for i in range(3):
#             for j in range(3):
#                 if self.board[i, j] == 1:
#                     self.ax.text(j + 0.5, 2.5 - i, "X", ha="center", va="center", fontsize=24, color="blue")
#                 elif self.board[i, j] == 2:
#                     self.ax.text(j + 0.5, 2.5 - i, "O", ha="center", va="center", fontsize=24, color="red")

#         if self.check_winner():
#             self.ax.set_title(f"Player {self.current_player} Wins!")
#             self.game_over = True
#         elif not np.any(self.board == 0):
#             self.ax.set_title("Game Over - Draw")
#             self.game_over = True
#         else:
#             self.ax.set_title(f"Player {self.current_player}'s Turn")

#         self.ax.set_xticks([])
#         self.ax.set_yticks([])
#         self.fig.canvas.draw()

#     def click_handler(self, event):
#         if self.game_over:
#             return
#         x, y = int(event.xdata), int(3 - event.ydata)%3
#         # x, y = int(event.xdata), int(event.ydata)
#         print(x,y)
#         if 0 <= x < 3 and 0 <= y < 3:
#             self.make_move(y, x)

#     def make_move(self, row, col):
#         if self.board[row, col] == 0:
#             self.board[row, col] = self.current_player
#             if self.check_winner():
#                 self.draw_board()
#             else:
#                 self.current_player = 2 if self.current_player == 1 else 1
#                 self.draw_board()
#         else:
#             print("Invalid move. Try again.")

#     def check_winner(self):
#         for i in range(3):
#             if np.all(self.board[i, :] == self.current_player) or np.all(self.board[:, i] == self.current_player):
#                 return True
#         if np.all(np.diag(self.board) == self.current_player) or np.all(np.diag(np.fliplr(self.board)) == self.current_player):
#             return True
#         return False

#     def start_game(self):
#         self.fig.canvas.mpl_connect("button_press_event", self.click_handler)
#         plt.show()

# if __name__ == "__main__":
#     game = TicTacToe()
#     game.start_game()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Button

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.current_player = 1
        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.game_over = False
        self.create_restart_button()
        self.draw_board()

    def create_restart_button(self):
        # Adding the restart button below the board
        self.restart_ax = self.fig.add_axes([0.35, 0.01, 0.3, 0.075])  # position [left, bottom, width, height]
        self.restart_button = Button(self.restart_ax, 'Restart Game', color="lightgrey", hovercolor="darkgrey")
        self.restart_button.on_clicked(self.restart_game)

    def draw_board(self):
        self.ax.clear()
        for row in range(4):
            self.ax.plot([row, row], [0, 3], color="black")
            self.ax.plot([0, 3], [row, row], color="black")
        
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == 1:
                    self.ax.text(j + 0.5, 2.5 - i, "X", ha="center", va="center", fontsize=24, color="blue")
                elif self.board[i, j] == 2:
                    self.ax.text(j + 0.5, 2.5 - i, "O", ha="center", va="center", fontsize=24, color="red")

        if self.check_winner():
            self.ax.set_title(f"Player {self.current_player} Wins!")
            self.game_over = True
            self.show_celebration(f"Player {self.current_player} Wins!")
        elif not np.any(self.board == 0):
            self.ax.set_title("Game Over - Draw")
            self.game_over = True
            self.show_celebration("Game Over - Draw")
        else:
            self.ax.set_title(f"Player {self.current_player}'s Turn")

        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.fig.canvas.draw()

    def click_handler(self, event):
        if self.game_over:
            return
        x, y = int(event.xdata), int(3 - event.ydata)%3
        if 0 <= x < 3 and 0 <= y < 3:
            self.make_move(y, x)

    def make_move(self, row, col):
        if self.board[row, col] == 0:
            self.board[row, col] = self.current_player
            if self.check_winner():
                self.draw_board()
            else:
                self.current_player = 2 if self.current_player == 1 else 1
                self.draw_board()
        else:
            print("Invalid move. Try again.")

    def check_winner(self):
        for i in range(3):
            if np.all(self.board[i, :] == self.current_player) or np.all(self.board[:, i] == self.current_player):
                return True
        if np.all(np.diag(self.board) == self.current_player) or np.all(np.diag(np.fliplr(self.board)) == self.current_player):
            return True
        return False

    def show_celebration(self, message):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.text(0.5, 0.5, message, ha="center", va="center", fontsize=24, color="green" if "Wins" in message else "purple")
        ax.set_xticks([])
        ax.set_yticks([])
        fig.patch.set_facecolor("#DFF2BF" if "Wins" in message else "#FFD1DC")

        def update_background(i):
            color = "#DFF2BF" if i % 2 == 0 else "#FFD1DC"
            fig.patch.set_facecolor(color)
        
        ani = animation.FuncAnimation(fig, update_background, frames=10, interval=500, repeat=False)
        plt.show()

    def restart_game(self, event=None):
        # Reset the game to its initial state
        self.board = np.zeros((3, 3))
        self.current_player = 1
        self.game_over = False
        self.draw_board()

    def start_game(self):
        self.fig.canvas.mpl_connect("button_press_event", self.click_handler)
        plt.show()

if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()
