import pygame   
class Board():# this is so cp i cant belive how cp is this omg 

    def __init__(self):
        self.taken1 = False
        self.taken2 = False
        self.taken3 = False
        self.taken4 = False
        self.taken5 = False
        self.taken6 = False
        self.taken7 = False
        self.taken8 = False
        self.taken9 = False
        self.X1 = False
        self.X2 = False
        self.X3 = False
        self.X4 = False
        self.X5 = False
        self.X6 = False
        self.X7 = False
        self.X8 = False
        self.X9 = False
        self.O1 = False
        self.O2 = False
        self.O3 = False
        self.O4 = False
        self.O5 = False
        self.O6 = False
        self.O7 = False
        self.O8 = False
        self.O9 = False
        self.image = pygame.image.load("Board.png")
        self.rect = self.image.get_rect(topleft = (0, 0))
    def space1(self):
        self.image = pygame.image.load("1-1.png")
        self.rect = self.image.get_rect(topleft = (800, 150))
        self.taken1 = False
    def space2(self):
        self.taken2 = False
        self.image = pygame.image.load("1-2.png")
        self.rect = self.image.get_rect(topleft = (1037, 150))
    def space3(self):
        self.taken3 = False
        self.image = pygame.image.load("1-3.png")
        self.rect = self.image.get_rect(topleft = (1270, 150))
    def space4(self):
        self.taken4 = False
        self.image = pygame.image.load("2-1.png")
        self.rect = self.image.get_rect(topleft = (800, 388))
    def space5(self):
        self.taken5 = False
        self.image = pygame.image.load("2-2.png")
        self.rect = self.image.get_rect(topleft = (1037, 388))
    def space6(self):
        self.taken6 = False
        self.image = pygame.image.load("2-3.png")
        self.rect = self.image.get_rect(topleft = (1270, 388))
    def space7(self):
        self.taken7 = False
        self.image = pygame.image.load("3-1.png")
        self.rect = self.image.get_rect(topleft = (800, 626))
    def space8(self):
        self.taken8 = False
        self.image = pygame.image.load("3-2.png")
        self.rect = self.image.get_rect(topleft = (1037, 626))
    def space9(self):
        self.taken9 = False
        self.image = pygame.image.load("3-3.png")
        self.rect = self.image.get_rect(topleft = (1269, 626))
