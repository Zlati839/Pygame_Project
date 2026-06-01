import pygame 
import random
import os
import math

pygame.init()
#=====DISPLAY SETTING========
info = pygame.display.Info()
w ,h = info.current_w , info.current_h
#w_pos = random.randint(0, w  - w/1.5)
#h_pos = random.randint(0, h - h/1.5)
#os.environ['SDL_VIDEO_WINDOW_POS'] = f'{w_pos},{h_pos}'
display = pygame.display.set_mode((w, h),pygame.NOFRAME)
#=====BALL SETTING========
Radius = 100
number_of_balls = 2
#======BALL Class========
class Ball():
    def __init__(self):
        self.crit1 = random.randint(1, 3) 
        self.crit2 = random.randint(1, 3)
        self.max_hp = 20
        self.hp = self.max_hp
        self.x = random.randint(Radius, w - Radius)
        self.y = random.randint(Radius, h - Radius)
        self.color = (255, 0, 0)
        self.speed_x = random.uniform(-5, 5)
        self.speed_y = random.uniform(-5, 5)
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if not 0<self.x < w:
            self.speed_x *= -1
        if not 0<self.y < h:
            self.speed_y *= -1
    def draw(self, display):
        pygame.draw.circle(display, self.color, (int(self.x), int(self.y)), Radius)
    def collide(self, other):
        if math.hypot(self.x - other.x, self.y - other.y) < 2 * Radius:
            self.crit1 = random.randint(1, 3) 
            self.crit2 = random.randint(1, 3)
            self.speed_x , other.speed_x = other.speed_x , self.speed_x
            self.speed_y, other.speed_y = other.speed_y , self.speed_y
            if self.crit1 == 2:
             other.hp -= 2
             print ("Critical Hit For Red!")
            else:
             other.hp -= 1

            if self.crit2 == 2:
             self.hp -= 2
             print ("Critical Hit For Blue!")
            else:             
             self.hp -= 1

class Bar1():
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
        pygame.draw.rect(display, ('Red'), (self.x, self.y, self.w, self.h))
        pygame.draw.rect(display, ('Yellow'), (self.x, self.y, self.w * self.ratio, self.h))


class Ball2():
    def __init__(self): 
        self.max_hp = 20
        self.hp = self.max_hp
        self.x = random.randint(Radius, w - Radius)
        self.y = random.randint(Radius, h - Radius)
        self.color = (0, 0, 255)
        self.speed_x = random.uniform(-5, 5)
        self.speed_y = random.uniform(-5, 5)
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if not 0<self.x < w:
            self.speed_x *= -1
        if not 0<self.y < h:
            self.speed_y *= -1
    def draw(self, display):
        pygame.draw.circle(display, self.color, (int(self.x), int(self.y)), Radius)
class Bar2():
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
        pygame.draw.rect(display, ('Blue'), (self.x, self.y, self.w, self.h))
        pygame.draw.rect(display, ('Yellow'), (self.x, self.y, self.w * self.ratio, self.h))


running = True
ball1 = Ball()
bar1 = Bar1(50, 50, 200, 20, ball1.max_hp)
ball2 = Ball2()
bar2 = Bar2(w - 250, 50, 200, 20, ball2.max_hp)
while running:
    display.fill((0,0,0))
    #Draw and move balls
    ball1.move()
    ball2.move()

    bar1.hp = ball1.max_hp - ball1.hp
    bar2.hp = ball2.max_hp - ball2.hp

    bar1.draw(display)
    bar2.draw(display)

    ball1.draw(display)
    ball2.draw(display)
    
    ball1.collide(ball2)

    if ball1.hp <= 0:
        print("Blue Wins!")
        running = False
    elif ball2.hp <= 0:
        print("Red Wins!")
        running = False
    #Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()