import pygame
from pygame.locals import *
import config
from background import Background
from screenhandler import ScreenHandler
from state import State
from gameobject import GameObject

class Game(State, ScreenHandler):
    def __init__(self):
        super(Game, self).__init__()
        width, height = self.back_screen.get_size()
        self.background_left = Background(width/2, height)
        self.background_right = Background(width/2, height)
        self.position = (960,0)
        self.player_left = GameObject("star.png", self.position, width/2, height, 0)
        self.player_right = GameObject("star_dark.png", self.position, width/2, height, 0)
        self.__sizetextures()
        self.gameobjects = []
        self.displacement = 0
        self.is_displacing = False
        self.keyvector = (0,0)
        self.movement_speed = .75
        self.is_done = False

    def update(self, dt):
        width, height = self.back_screen.get_size()
        self.background_left.update(self.back_screen.subsurface(0, 0, width/2, height))
        self.background_right.update(self.back_screen.subsurface(width/2, 0, width/2, height))
        self.player_left.update(self.back_screen.subsurface(0, 0, width/2, height), self.displacement)
        self.player_right.update(self.back_screen.subsurface(width/2, 0, width/2, height), self.displacement)
        if self.is_displacing:
            self.displacement += dt / 10.0
        self.position = (self.position[0] + dt * self.keyvector[0] * self.movement_speed,
                        self.position[1] + dt * self.keyvector[1] * self.movement_speed)
        self.position = self.player_left.move(self.position)
        self.player_right.move(self.position)
        if (self.player_left.isdead()):
            self.is_done = True

    def jump_pressed(self):
        self.is_displacing = True
        self.position = (self.position[0], self.position[1] + 150)

    def left_pressed(self):
        self.keyvector = (-1,0)
    def left_released(self):
        self.keyvector = (0,0)

    def right_pressed(self):
        self.keyvector = (1,0)
    def right_released(self):
        self.keyvector = (0,0)

    def isdone(self):
        return self.is_done

    def resize(self):
        self.__sizetextures()

    def __sizetextures(self):
        width, height = self.back_screen.get_size()
        self.background_left.resize_textures(width/2, height)
        self.background_right.resize_textures(width/2, height)
