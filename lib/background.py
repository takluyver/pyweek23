import os.path
from . import config
import utils, pygame

#draw a live background
class Background(object):
    #Load all full resolution assets as static
    space = pygame.image.load(os.path.join(config.IMAGE_ROOT, "space.png"))

    def __init__(self, width, height):
        self.resize_textures(width, height)
        self.has_rendered = False

    def update(self, surf, dirty_rects):
        width, height = surf.get_size()
        #black out whole surface
        #surf.fill((0,0,0), (0, 0, width, height))
        #draw background
        space_width, space_height = self.resized_space.get_size()
        if not self.has_rendered:
            surf.blit(self.resized_space, (0, 0))
            self.has_rendered = True
            return True
        else:
            for rect in dirty_rects:
                surf.blit(self.resized_space, rect, rect)
        return False

    def resize_textures(self, width, height):
        self.current_width = width
        self.current_height = height
        self.resized_space = utils.aspect_scale(self.space, (self.current_width, self.current_height))
        self.resized_space.convert()
        self.has_rendered = False
