import subprocess
import os
import sys
import pygame
class Game():
   def __init__(self):
      #=================Mini Game 1 ========================
      self.minigame_process = None
      self.mini_on = False
      self.lock = False
      #=================Mini Game 2 ========================
      self.minigame_process1 = None
      self.mini_on1 = False
      self.lock1 = False
   def Start(self,game): 
       if self.lock:
            game_file = os.path.join(os.path.dirname(__file__), game)
            self.minigame_process = subprocess.Popen([sys.executable, game_file])
            self.mini_on = True
            self.lock = False
            #Check if minigame has finished
       if self.minigame_process is not None and self.minigame_process.poll() is not None:
            self.mini_on = False
            self.minigame_process = None
   def Start1(self,game): 
       if self.lock1:
            game_file = os.path.join(os.path.dirname(__file__), game)
            self.minigame_process1 = subprocess.Popen([sys.executable, game_file])
            self.mini_on1 = True
            self.lock1 = False
            #Check if minigame has finished
       if self.minigame_process1 is not None and self.minigame_process1.poll() is not None:
            self.mini_on1 = False
            self.minigame_process1 = None