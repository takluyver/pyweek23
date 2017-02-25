import sys
sys.dont_write_bytecode = True
import pygame
import lib
from lib.fader import Fader
from lib.menu import Menu
from lib.blank import Blank
from lib.statemanager import StateManager
from lib.music import MusicStart, MusicStop
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    # create new state machine and register the clock  tick method
    # as our incrementing callback for current ticks in ms.
    clock = pygame.time.Clock()
    statemanager = StateManager(clock.tick)
    pygame.mixer.init()
    """
    statemanager.add(MusicStart("assets/sound/intro.ogg"))
    statemanager.add(Blank(1500))
    statemanager.add(Fader("CandL Development Presents", 750, 1500, 3000, "1938 STeMPEL.ttf", (196, 56, 21)))
    statemanager.add(Blank(1000))
    statemanager.add(Fader("A Peter + Lucy Production", 750, 1500, 3000, "1938 STeMPEL.ttf", (171, 252, 251)))
    statemanager.add(Blank(1000))
    statemanager.add(Fader("S O L A R  |  F L A I R", 2500, 3000, 9000, "good times rg.ttf", (252, 240, 15)))
    statemanager.add(Blank(500))
    statemanager.add(MusicStop())
    """
    statemanager.add(Menu(statemanager))
    statemanager.add(Fader("THANKS FOR PLAYING!", 500, 4000, 5000, "good times rg.ttf", (171, 252, 251)))
    while statemanager.update():
        pass
