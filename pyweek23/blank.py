import pygame
from state import State
from screenhandler import ScreenHandler

class Blank(ScreenHandler, State):
    def __init__(self, animationms):
        super(Blank, self).__init__()
        self.animationms = animationms
        self.currentms = 0
        self.is_done = False

    def update(self, dt):
        self.currentms += dt
        if self.currentms >= self.animationms:
            self.is_done = True

    def isdone(self):
        return self.is_done
