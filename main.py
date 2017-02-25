import pygame
from pyweek23.statemanager import StateManager
from pyweek23.fader import Fader
from pyweek23.menu import Menu
from pygame.locals import *
from pyweek23.blank import Blank

if __name__ == "__main__":
    pygame.init()
    # create new state machine and register the clock  tick method
    # as our incrementing callback for current ticks in ms.
    clock = pygame.time.Clock()
    statemanager = StateManager(clock.tick)
    statemanager.add(Blank(1000))
    statemanager.add(Fader("CandL Development Presents", 750, 1500, 4500, "1938 STeMPEL.ttf", (196, 56, 21)))
    statemanager.add(Blank(500))
    statemanager.add(Fader("A Peter + Lucy Production", 750, 1500, 4500, "1938 STeMPEL.ttf", (171, 252, 251)))
    statemanager.add(Blank(500))
    statemanager.add(Fader("S O L A R  |  F L A I R", 2500, 3000, 9000, "good times rg.ttf", (252, 240, 15)))
    statemanager.add(Blank(500))
    statemanager.add(Menu())
    while statemanager.update():
        pass
