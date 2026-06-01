import pygame
import random
class Ai():
    def __init__(self, check_win_func,board):
        self.check_win = check_win_func
        self.board = board
        self.lock = False
    def check(self, board, is_checking):

     score = -1000
     move = None
     chance = random.randint(1, 3)


     for i in range(9):
        if board[i] == "":

            board[i] = "O"
            temp_score = self.checking(board, False)
            board[i] = ""
            if chance == 1:
                self.lock = True
                while move is None:
                 random_move = random.randint(0, 8)
                 if board[random_move] == "":
                   print("AI made a random move")
                   move = random_move

            if temp_score > score and not self.lock:
                score = temp_score
                move = i

     return move  
    def checking(self, board, is_checking):
      winner = self.check_win(board)
      if winner == "X":
         return -1
      elif winner == "O":
         return 1
      elif all(space != "" for space in board):
         return 0
      if is_checking:
         best_score = -1000
         for i in range(9):
            if board[i] == "":
               board[i] = "O"
               score = self.checking(board, False)
               board[i] = ""
               best_score = max(score, best_score)
         return best_score
      else:
         best_score = 1000
         for i in range(9):
            if board[i] == "":
               board[i] = "X"
               score = self.checking(board, True)
               board[i] = ""
               best_score = min(score, best_score)
         return best_score
