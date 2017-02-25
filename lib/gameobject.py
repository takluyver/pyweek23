import pygame
from lib import utils
import config


class GameObject(object):
    def __init__(self, image, pos, screenwidth, screenheight, displacement):
        self.rotation_vector = 0
        self.rotation = 0
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

    def move(self, newpos, dt):
        x,y = newpos
        if x < self.width / 2:
            x = self.width / 2
        if x > config.GAME_WIDTH - (self.width / 2):
            x = config.GAME_WIDTH - (self.width / 2)
        if y <  self.displacement - self.height:
            self.is_dead = True
        # if we are moving left, then start rotating left.
        # if we are moving right, start rotating right.
        if (self.position[0] < x): # we are moving right
            self.rotation_vector -= 0.01 * dt
        elif (self.position[0] > x): # we're moving left
            self.rotation_vector += 0.01 * dt
        else:
            #move vector back toward 0.
            if self.rotation_vector > 0:
                self.rotation_vector = max(0, self.rotation_vector - 0.05 * dt)
            else:
                self.rotation_vector = min(0, self.rotation_vector + 0.05 * dt)
        self.position = (x, y)
        return self.position

    def getpos(self, screensize):
        #bottom of image is y, center of bottom of image is x.
        drawpos = utils.get_screen_coords(self.position, screensize, self.displacement)
        drawpos = drawpos[0] - self.resized_image.get_size()[0]/2, drawpos[1] - self.resized_image.get_size()[1]
        return drawpos

    def getscreenrect(self, screensize):
        drawpos = self.getpos(screensize)
        return pygame.rect.Rect(drawpos[0], drawpos[1], self.resized_image.get_size()[0], self.resized_image.get_size()[1]).inflate(30, 30)


    def update(self, surf, displacement, dt):
        self.rotation += (dt / 5.0 * self.rotation_vector)
        self.displacement = displacement
        self.rotated_image = utils.rot_center(self.resized_image, self.rotation)
        drawpos = self.getpos(surf.get_size())
        #self.rotated.center = self.resized_image.get_rect().center
        surf.blit(self.rotated_image, drawpos)

    def resize(self, screenwidth, screenheight):
        heightratio = float(screenwidth) / config.GAME_HEIGHT
        widthratio = float(screenheight) / config.GAME_WIDTH
        self.resized_image = utils.aspect_scale(self.image, (self.image.get_size()[0] * widthratio, self.image.get_size()[1] * heightratio))
        self.resized_image.convert()
