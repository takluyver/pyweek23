import pygame
from pygame.locals import *
import config
from background import Background
from screenhandler import ScreenHandler
from state import State
class Settings(State, ScreenHandler):
    def __init__(self):
        super(Settings, self).__init__()
        #self.__sizetextures()
        self.gameobjects = []
        self.background_left = Background(config.width/2, config.height)
        self.background_right = Background(config.width/2, config.height)

    def update(self, dt):
        pass
        #width, height = self.screen.get_size()

    def isdone(self):
        return False

    def resize(self):
        pass
        #self.__sizetextures()

    def __sizetextures(self):
        width, height = self.screen.get_size()
        self.left_back_screen = self.back_screen.subsurface(0, 0, width/2, height)
        self.right_back_screen = self.back_screen.subsurface(width/2, 0, width/2, height)
        self.background_left.resize_textures(width/2, height)
        self.background_right.resize_textures(width/2, height)
