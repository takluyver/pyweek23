import pygame
from lib import utils
import config


class GameObject(object):
    def __init__(self, image, pos, screenwidth, screenheight, displacement):
        self.direction = 90
        self.speed = 0
        self.position = pos
        self.image = pygame.image.load(config.IMAGE_ROOT + image)
        self.width = self.image.get_size()[0]
        self.height = self.image.get_size()[1]
        self.displacement = displacement
        self.resize(screenwidth, screenheight)
        self.is_dead = False

    def isdead(self):
        return self.is_dead

    def move(self, newpos):
        x,y = newpos
        if x < self.width / 2:
            x = self.width / 2
        if x > config.GAME_WIDTH - (self.width / 2):
            x = config.GAME_WIDTH - (self.width / 2)
        if y <  self.displacement - self.height:
            self.is_dead = True
        self.position = (x, y)
        return self.position
    def getpos(self, screensize):
        #bottom of image is y, center of bottom of image is x.
        drawpos = utils.get_screen_coords(self.position, screensize, self.displacement)
        drawpos = drawpos[0] - self.resized_image.get_size()[0]/2, drawpos[1] - self.resized_image.get_size()[1]
        return drawpos

    def update(self, surf, displacement):
        self.displacement = displacement
        surf.blit(self.resized_image, self.getpos(surf.get_size()))

    def resize(self, screenwidth, screenheight):
        heightratio = float(screenwidth) / config.GAME_HEIGHT
        widthratio = float(screenheight) / config.GAME_WIDTH
        self.resized_image = utils.aspect_scale(self.image, (self.image.get_size()[0] * widthratio, self.image.get_size()[1] * heightratio))
        self.resized_image.convert()
