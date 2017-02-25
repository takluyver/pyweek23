import pygame
from pygame.locals import *
import config
from state import State
from screenhandler import ScreenHandler

class Menu(State, ScreenHandler):
    def __init__(self):
        super(State, self).__init__()
        self.is_done = False

    def isdone(self):
        return self.is_done

    def update(self, dt):
        pass
