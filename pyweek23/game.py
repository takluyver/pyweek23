import pygame
from pygame.locals import *
import config
from background import Background




class Game(ScreenHandler):
    def __init__(self):
        self.__sizetextures()
        self.gameobjects = []
        self.background_left = Background(config.width/2, config.height)
        self.background_right = Background(config.width/2, config.height)

    def update(self):
        width, height = self.screen.get_size()

    def resize(self):
        self.__sizetextures()

    def __sizetextures(self):
        width, height = self.screen.get_size()
        self.left_back_screen = self.back_screen.subsurface(0, 0, width/2, height)
        self.right_back_screen = self.back_screen.subsurface(width/2, 0, width/2, height)
        self.background_left.resize_textures(width/2, height)
        self.background_right.resize_textures(width/2, height)
