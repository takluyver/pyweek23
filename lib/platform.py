import pygame
import config
light_images = ["left_corner_lit.png", "mid_platform_lit.png", "right_corner_lit.png"]
dark_images = ["left_corner_dark.png", "mid_platform_dark.png", "right_corner_dark.png"]
class PlatformManager(object):
    def __init__(self):
        self.light_surfaces = []
        self.dark_surfaces = []
        for image in light_images:
            self.light_surfaces.append(pygame.image.load(config.IMAGE_ROOT + "/platforms/" + image))
        for image in dark_images:
            self.dark_surfaces.append(pygame.image.load(config.IMAGE_ROOT + "/platforms/" + image))
        self.platformcache = {"light": [], "dark": []}
        for i in range(3, 20):
            self.platformcache["light"].append(self._getplatformimage(i, False))
            self.platformcache["dark"].append(self._getplatformimage(i, True))

    def getplatformimage(self, width, is_dark):
        if width > 20: return None
        if is_dark:
            return self.platformcache["dark"][width-3]
        else:
            return self.platformcache["light"][width-3]

    def _getplatformimage(self, width, is_dark):
        img_width, img_height = self.dark_surfaces[0].get_size()
        if is_dark:
            surf = pygame.Surface((width * img_width, img_height), pygame.SRCALPHA)
            surf.convert_alpha()
            #surf.fill((0,0,0,0), (0,0,surf.get_size()[0], surf.get_size()[1]))
            surf.blit(self.dark_surfaces[0], (0,0))
            for i in range(1, width-1):
                surf.blit(self.dark_surfaces[1], (img_width * i,0))
            surf.blit(self.dark_surfaces[2], (img_width * (width-1),0))
            return surf
        else:
            surf = pygame.Surface((width * img_width, img_height), pygame.SRCALPHA)
            surf.blit(self.light_surfaces[0], (0,0))
            for i in range(1, width-1):
                surf.blit(self.light_surfaces[1], (img_width * i,0))
            surf.blit(self.light_surfaces[2], (img_width * (width-1),0))
            return surf
