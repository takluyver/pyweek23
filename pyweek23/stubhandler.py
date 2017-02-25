import pygame
import config

class StubHandler(object):
    def __init__(self):
        super(StubHandler, self).__init__()

    def resize(self): ## OVERRIDE THIS
        pass

    def super_active(self):
        pass

    def super_isdone(self):
        return False

    def update_super(self, dt):
        pass
