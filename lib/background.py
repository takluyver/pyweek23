import utils, pygame
from gameobject import GameObject

#draw a live background
class Background(object):
    #Load all full resolution assets as static
    space = pygame.image.load("assets/images/space.png")

    def __init__(self, width, height):
        self.resize_textures(width, height)

    def update(self, surf):
        width, height = surf.get_size()
        #black out whole surface
        surf.fill((0,0,0), (0, 0, width, height))
        #draw background
        space_width, space_height = self.resized_space.get_size()
        surf.blit(self.resized_space, (0, 0))


    def resize_textures(self, width, height):
        self.current_width = width
        self.current_height = height
        self.resized_space = utils.aspect_scale(self.space, (self.current_width, self.current_height))
        self.resized_space.convert()
