import pygame
from pygame.locals import *
import config
from state import State
from screenhandler import ScreenHandler
from utils import get_font, scale_rect
from game import Game
from settings import Settings

class Menu(State, ScreenHandler):

    def __init__(self, statemanager):
        super(State, self).__init__()
        #TODO: just use state def in lambda.  if we don't init outside lambda, the exception is squelched for some baffling reason.
        g = Game()
        s = Settings()
        self.options = [ (get_font("New Game", "good times rg.ttf", 240, (252, 240, 15)), lambda x: x.statemanager.addnextstate(g)),
                        (get_font("Settings", "good times rg.ttf", 240, (252, 240, 15)), lambda x: x.statemanager.addnextstate(s)),
                        (get_font("   Exit   ", "good times rg.ttf", 240, (252, 240, 15)), lambda x: x) ]
        self.is_done = False
        self.selected_option = 0
        self.statemanager = statemanager

    def isdone(self):
        return self.is_done

    def update(self, dt):
        self.back_screen.fill((0,0,0), self.back_screen.get_rect())
        for i, option in enumerate(self.options):
            #TODO: break this grid code out into a acutal layout function
            target = scale_rect(self.screen.get_rect(), option[0].get_rect(), .6, .3)
            target_surf = pygame.transform.smoothscale(option[0], (target.width, target.height))
            target.center = (self.screen.get_width() / 2, (i * (self.screen.get_height() / 2 - ((target.height))) + 50 + target.height / 2))
            self.back_screen.blit(target_surf, target)
            #draw border around selected option
            if i == self.selected_option:
                border = target.inflate(40, 40)
                pygame.draw.rect(self.back_screen, (252, 240, 15), target, 5)

    def down_pressed(self):
        self.selected_option = min(len(self.options)-1, self.selected_option + 1)

    def up_pressed(self):
        self.selected_option = max(0, self.selected_option - 1)

    def swap_pressed(self):
        self.options[self.selected_option][1](self)
        self.is_done = True
