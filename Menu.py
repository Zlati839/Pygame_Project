import pygame
class Menu():
    def __init__(self, w ,h):
        self.image = pygame.image.load("Menu.png")
        self.rect = self.image.get_rect(topleft = (0, 0))

        self.image_play = pygame.image.load("Button_Play.png")
        self.rect_play = self.image_play.get_rect(topleft = (0, 0))
        self.rect_play.center = (w // 2, h - 148)\
        
        self.image_quit = pygame.image.load("Button_Off.png")
        self.rect_quit = self.image_quit.get_rect(topleft = (0, 0))
        self.rect_quit.center = (w // 2 + 330, h - 110)

        self.image_Settings = pygame.image.load("Button_Settings.png")
        self.rect_Settings = self.image_Settings.get_rect(topleft = (0, 0))
        self.rect_Settings.center = (w // 2 + 330, h - 180)

        self.image_Title = pygame.image.load("Title.png")
        self.rect_Title = self.image_Title.get_rect(topleft = (0, 0))
        self.rect_Title.center = (w // 2, h - 700)
