import pygame
from Ai import Ai
from Board import *
from Menu import *

pygame.init()

def animate(self, frames, img):
   frames += 0.4
   if frames >= 14:
      frames = 0
   self.image = img[int(frames)]
                             
    
class Game():
   def __init__(self):
      self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.SCALED)
      w = self.display.get_width()
      h = self.display.get_height()
      self.board_state = [""] * 9
      self.roundX_turn = True
      self.X_clicked = False
      self.roundO_turn = False
      self.O_clicked = False
      self.wins = [
         (0,1,2),
         (3,4,5),
         (6,7,8),
         (0,3,6),
         (1,4,7),
         (2,5,8),
         (0,4,8),
         (2,4,6)
        ]
#=============Loading the board ==========
      self.board = Board()
      self.board.image = pygame.transform.scale(self.board.image, (w, h))
      for i in range(1, 10):
         space = Board()           
         getattr(space, f'space{i}')()  
         setattr(self, f'space{i}', space)
      self.spaces = [self.space1, self.space2, self.space3, self.space4, 
          self.space5, self.space6, self.space7, self.space8, self.space9]
#=============Game states=============  
      self.on = True
      self.ai_played = False
      self.game = False
      self.menu = Menu(w , h) 
      self.menu.image = pygame.transform.scale(self.menu.image, (w, h))
#=============AI========================
      self.ai = Ai(self.check_win,self.board_state)
   def check_win(self, board):
        for a, b, c in self.wins:
            if board[a] == board[b] == board[c] != "":
                return board[a]  
        return None
   def run(self):
      while self.on :
       if self.game:
         self.display.blit(self.board.image, self.board.rect)
         #displaying spaces
         for space in self.spaces:
             self.display.blit(space.image, space.rect)
         #switching rounds
         if self.X_clicked:
            self.roundO_turn = True
            self.roundX_turn = False
            self.X_clicked = False
            self.ai_played = False
         #wins
         winner = self.check_win(self.board_state)
         if winner:
            self.game = False
         # the ai initiation and move
         if self.roundO_turn and not self.ai_played:
           move = self.ai.check(self.board_state, True)
           if move is not None:
            self.board_state[move] = "O"
            space = self.spaces[move]
            row = move // 3 + 1
            col = move % 3 + 1
            space.image = pygame.image.load(
                f"O_tile/{row}-{col}-O.png"
            )
            setattr(space, f"taken{move+1}", True)
 
           self.ai_played = True
           self.ai.lock = False
           self.roundO_turn = False
           self.roundX_turn = True
         #draw
         if self.board_state.count("") == 0 and not winner:
            print("Draw")
            self.game = False
       elif not self.game :
         self.display.blit(self.menu.image, self.menu.rect)
         self.display.blit(self.menu.image_play, self.menu.rect_play)
         self.display.blit(self.menu.image_quit, self.menu.rect_quit)
         self.display.blit(self.menu.image_Settings, self.menu.rect_Settings)
         self.display.blit(self.menu.image_Title, self.menu.rect_Title)
#=============event loop=====================
       for event in pygame.event.get() :
          if event.type == pygame.VIDEORESIZE:
               self.display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
          if event.type == pygame.MOUSEBUTTONUP:
            for i, space in enumerate(self.spaces, start=1):
             if space.rect.collidepoint(event.pos) and not getattr(space, f"taken{i}"):
              if self.roundX_turn:
               space.image = pygame.image.load(f"X_tile/{(i-1)//3+1}-{(i-1)%3+1}-X.png")
               self.board_state[i-1] = "X"
               self.X_clicked = True
               setattr(space, f"taken{i}", True)
          if event.type == pygame.MOUSEBUTTONUP and self.menu.rect_play.collidepoint(event.pos) and not self.game:
            self.__init__() 
            self.game = True
          if event.type == pygame.MOUSEBUTTONUP and self.menu.rect_quit.collidepoint(event.pos) and not self.game:
            self.on = False
          if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE ):
            self.on = False
       pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
