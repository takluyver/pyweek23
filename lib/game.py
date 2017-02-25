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
        self.bright_star = GameObject("star.png", self.position, width/2, height, 0)
        self.dark_star = GameObject("star_dark.png", self.position, width/2, height, 0)
        self.__sizetextures()
        self.gameobjects = []
        self.displacement = 0
        self.is_displacing = False
        self.keyvector = (0,0)
        self.movement_speed = 1
        self.vertical_speed = 0
        self.is_done = False
        self.moving_left = False
        self.moving_right = False
        self.active_player = 0
        self.gravity = -15


    def update(self, dt):
        width, height = self.back_screen.get_size()

        # TODO: implement gravity
        # dt / 1000 to get fractional seconds and / 2 to get proper integration https://www.niksula.hut.fi/~hkankaan/Homepages/gravity.html
        self.vertical_speed += self.gravity * (dt / 1000.0)
        #scroll the screen
        if self.is_displacing:
            pass
            self.displacement += dt / 10.0
        if self.moving_left:
            self.keyvector = (-1, self.vertical_speed)
        elif self.moving_right:
            self.keyvector = (1, self.vertical_speed)
        else:
            self.keyvector = (0,self.vertical_speed)
        #reposition the player
        self.position = (self.position[0] + dt * self.keyvector[0] * self.movement_speed,
                        self.position[1] + dt * self.keyvector[1] * self.movement_speed)
        self.position = self.bright_star.move((self.position[0], max(self.position[1], 10)))
        self.dark_star.move(self.position)

        #set our state to done if player is dead
        if (self.bright_star.isdead()):
            self.is_done = True

        #redraw all
        self.background_left.update(self.back_screen.subsurface(0, 0, width/2, height))
        self.background_right.update(self.back_screen.subsurface(width/2, 0, width/2, height))
        if (self.active_player == 0):
            self.bright_star.update(self.back_screen.subsurface(0, 0, width/2, height), self.displacement)
            self.dark_star.update(self.back_screen.subsurface(width/2, 0, width/2, height), self.displacement)
        else:
            self.bright_star.update(self.back_screen.subsurface(width/2, 0, width/2, height), self.displacement)
            self.dark_star.update(self.back_screen.subsurface(0, 0, width/2, height), self.displacement)

    def jump_pressed(self):
        self.is_displacing = True
        self.vertical_speed = 5
        self.position = (self.position[0], self.position[1] + 150)

    def swap_pressed(self):
        self.active_player = not self.active_player

    def left_pressed(self):
        self.moving_left = True
    def left_released(self):
        self.moving_left = False

    def right_pressed(self):
        self.moving_right = True
    def right_released(self):
        self.moving_right = False

    def isdone(self):
        return self.is_done

    def resize(self):
        self.__sizetextures()

    def __sizetextures(self):
        width, height = self.back_screen.get_size()
        self.background_left.resize_textures(width/2, height)
        self.background_right.resize_textures(width/2, height)
        self.bright_star.resize(width, height)
        self.dark_star.resize(width, height)
