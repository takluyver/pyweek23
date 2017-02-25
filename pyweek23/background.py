import utils, pygame
from gameobject import GameObject

#draw a live background
class Background(object):
    #Load all full resolution assets as static
    space = pygame.image.load("assets/space.png")
    asteroids = [pygame.image.load("assets/asteroid1.png")]

    def __init__(self, width, height):
        self.resize_textures(width, height)

    def update(self, surf):
        width, height = surf.get_size()
        #black out whole surface
        surf.fill((0,0,0), (0, 0, width, height))
        #draw background
        space_width, space_height = self.resized_space.get_size()
        surf.blit(self.resized_space, (width-space_width, (height - space_height) / 2))

    def create_asteroid(self):
        pass

    def resize_textures(self, width, height):
        self.current_width = width
        self.current_height = height
        self.resized_space = utils.aspect_scale(self.space, (self.current_width, self.current_height))
