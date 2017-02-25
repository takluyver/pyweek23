import pygame
from lib import utils
IMAGE_ROOT = "assets/images/"

GAME_WIDTH = 1920
GAME_HEIGHT = 2160


def get_screen_coords(gamecoords, screen, displacement):
    #print gamecoords, screen, displacement
    heightratio = float(screen[1]) / GAME_HEIGHT
    widthratio = float(screen[0]) / GAME_WIDTH
    screencoordy = screen[1] - ((gamecoords[1] - displacement) * heightratio)
    screencoordx = gamecoords[0] * widthratio
    screencoords = screencoordx, screencoordy
    return screencoords

class GameObject(object):
    def __init__(self, image, pos, width, height):
        self.direction = 90
        self.speed = 0
        self.position = pos
        self.image = pygame.image.load(IMAGE_ROOT + image)
        self.resize(width, height)

    def update(self, surf, displacement):
        drawpos = get_screen_coords(self.position, surf.get_size(), displacement)
        drawpos = drawpos[0], drawpos[1] - self.resized_image.get_size()[1]
        surf.blit(self.resized_image, drawpos)

    def resize(self, width, height):
        heightratio = float(width) / GAME_HEIGHT
        widthratio = float(height) / GAME_WIDTH
        self.resized_image = utils.aspect_scale(self.image, (self.image.get_size()[0] * widthratio, self.image.get_size()[1] * heightratio))
