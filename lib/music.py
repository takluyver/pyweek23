import pygame
from state import State
from stubhandler import StubHandler

class MusicStart(State, StubHandler):
    def __init__(self, filename):
        self.filename = filename
        self.is_done = False

    def update(self, dt):
        if not self.is_done:
            pygame.mixer.music.load(self.filename)
            pygame.mixer.music.play(0)
            self.is_done = True

    def isdone(self):
        return self.is_done

class MusicStop(State, StubHandler):
    def __init__(self):
        self.is_done = False

    def update(self, dt):
        if not self.is_done:
            pygame.mixer.music.stop()
        self.is_done = True

    def isdone(self):
        return self.is_done
