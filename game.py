import pygame
from pygame.locals import *
from pyweek23.game import Game
from pyweek23 import config

def main():
    maingame = Game()
    running = True
    while maingame.is_running:
        maingame.update()
