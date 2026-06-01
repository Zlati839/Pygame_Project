import os
import random
import pygame
pygame.init()
class Bar():
    def __init__(self, x, y, w, h, max):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.max = max
        self.hp = 0
        self.ratio = 0
    def draw(self, display):
        self.ratio = max(0, min(self.hp / self.max, 1))
        pygame.draw.rect(display, ('black'), (self.x, self.y, self.w, self.h))
        pygame.draw.rect(display, ('Yellow'), (self.x, self.y, self.w * self.ratio, self.h))
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
      self.fishing = False
      self.animating_rod = False
      self.lock = False
      self.lock10 = False
      self.end = False
      self.speed = 5
      #===============Images================
      #Water
      self.water = pygame.image.load("Fish/Water.png")
      self.water = pygame.transform.scale(self.water, (self.w, self.h))
      #Rod
      self.rod = pygame.image.load("Fish/Fishing_Rod.png")
      self.rod_rect = self.rod.get_rect(center=(self.w - self.w // 1.5, self.h // 2))
      self.rod_frame = 0
      self.rod_frames = []
      for i in range(1, 9):
          frame = pygame.image.load(f"Fish/Throwing_animation{i}.png")
          self.rod_frames.append(frame)
      #pull
      self.rod_image_pull = pygame.image.load("Fish/Fishing_Rod.png")
      self.animating_pull = False
      self.rod_pull_frames = 0
      self.rod_img = []
      for i in range(1, 4):
          frame = pygame.image.load(f"Fish/Pull_anim{i}.png")
          self.rod_img.append(frame)
      #Bar
      self.bar = pygame.image.load("Fish/Fish_Bar.png")
      self.bar_rect = self.bar.get_rect(center=(self.w // 2 - self.bar.get_width() // 2, self.h // 2 + 100))
      #Fish
      self.fish = pygame.image.load("Fish/Fish.png")
      self.fish_rect = self.fish.get_rect(center=(self.bar_rect.topleft[0] , self.bar_rect.centery))
      #Player
      self.player = pygame.image.load("Fish/Player_line.png")
      self.player_rect = self.player.get_rect(center=(self.bar_rect.centerx, self.bar_rect.centery))
      self.progress = Bar(250, self.bar_rect.top - 40, 500, 20, 4)
   def animate_rod(self):
    
       if self.animating_rod and not self.lock:
         self.rod_frame += 0.2
         if self.rod_frame >= len(self.rod_frames):
              self.rod_frame = 0
              self.animating_rod = False
              self.lock = True
       self.rod = self.rod_frames[int(self.rod_frame)]
   def animate_pull(self):
       self.end = True
       if self.animating_pull:
         self.rod_pull_frames += 0.05
         if self.rod_pull_frames >= len(self.rod_img):
              self.rod_pull_frames = 0
              self.animating_pull = False
              self.lock10 = True
              self.on = False
       self.rod_image_pull = self.rod_img[int(self.rod_pull_frames)]
   def fish_moving(self):
      self.fish_rect.x += self.speed
      # Keep the fish inside the bar and reverse direction at each end
      if self.fish_rect.left <= self.bar_rect.left + 10:
         self.fish_rect.left = self.bar_rect.left + 10  
         self.speed = 5
      elif self.fish_rect.right >= self.bar_rect.right - 10:
         self.fish_rect.right = self.bar_rect.right - 10
         self.speed = -5
   def run(self):
       while self.on:
         if self.fishing:
          self.fish_moving()
         self.animate_rod()
         self.animate_pull()
         self.display.blit(self.water , (0,0))
         if self.animating_pull:
          self.display.blit(self.rod_image_pull , self.rod_rect)
         else:
          self.display.blit(self.rod , self.rod_rect)
         if self.fishing:
          self.progress.draw(self.display)
         if self.fishing:
           self.display.blit(self.bar , self.bar_rect)
           self.display.blit(self.fish , self.fish_rect)
           self.display.blit(self.player , self.player_rect)
         if self.progress.hp >= self.progress.max and not self.lock10:
            self.animating_pull = True
            self.fishing = False
         for event in pygame.event.get():
             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and  self.end:
                self.animating_rod = True
                self.fishing = True
                if self.fishing and self.fish_rect.colliderect(self.player_rect) and self.progress.hp < self.progress.max:
                     self.progress.hp += 1
                     
                
                   
         pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()