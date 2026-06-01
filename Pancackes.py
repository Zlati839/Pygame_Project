import os
import pygame
import random 
pygame.init()

class Game():
   def __init__(self):
#================Display================
    
      info = pygame.display.Info()
      self.w , self.h = info.current_w , info.current_h
      w_pos = random.randint(0, self.w  - self.w/1.5)
      h_pos = random.randint(0, self.h - self.h/1.5)
      os.environ['SDL_VIDEO_WINDOW_POS'] = f'{w_pos},{h_pos}'
      self.display = pygame.display.set_mode((self.w/1.5, self.h/1.5),pygame.NOFRAME)
      self.display.fill('black')
      self.on = True
      self.dragging = False
#===============Images================
      #cat
      self.cat_imaage = pygame.image.load("Panake/Niko.Webp")  
      self.cat_rect = self.cat_imaage.get_rect(topleft=(self.w // 2.5 , self.h - self.h/1.2))
      #wall
      self.background = pygame.image.load("Panake/Background_Cat.png")
      self.background = pygame.transform.scale(self.background, (self.w, self.h))
      #panake
      self.pancake = pygame.image.load("Panake/Pancake.png")
      widthP = self.pancake.get_width()
      heightP = self.pancake.get_height()
      self.pancake = pygame.transform.scale(self.pancake, (widthP // 2, heightP // 2))
      self.pancake_rect = self.pancake.get_rect(topleft=(0, self.h - self.h/1.2))
#============================================================================================================
   def run(self):
      while self.on:
        if  self.dragging:
          self.cat_imaage = pygame.image.load("Panake/Niko1.png")
        else:
          self.cat_imaage = pygame.image.load("Panake/Niko.Webp")
        self.display.blit(self.background , (0,0))
        self.display.blit(self.cat_imaage , self.cat_rect)
        self.display.blit(self.pancake , self.pancake_rect)
      
        if self.pancake_rect.colliderect(self.cat_rect) :
            self.on = False
        if self.dragging:
            mouse_pos = pygame.mouse.get_pos()
            self.pancake_rect.center = mouse_pos
            self.pancake_rect.x = max(0, min(self.pancake_rect.x, self.display.get_width() - self.pancake_rect.width))
            self.pancake_rect.y = max(0, min(self.pancake_rect.y, self.display.get_height() - self.pancake_rect.height))
        for event in pygame.event.get():
             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.pancake_rect.collidepoint(event.pos):
                self.dragging = True
             if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.dragging = False
        pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()