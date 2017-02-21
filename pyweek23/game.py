import pygame
from pygame.locals import *
import config
from background import Background


class Game(object):
    def __init__(self):
        self.is_running = True
        self.__resizeall()

    def __resizeall(self):
        # get closest aspect to 16:9 and set to that.
        temp_height = int(config.width * 9 / 16.0)
        temp_width = int(config.height * 16 / 9.0)

        print "width: ", config.width, " temp_width: ", temp_width
        print "height: ", config.height, " temp_height: ", temp_height
        # determine which is a larger % shift from the other and use the lower.
        error_ratio_y = float(config.height) / temp_height
        error_ratio_x = float(config.width) / temp_width
        print "error y: ", error_ratio_y
        print "error x: ", error_ratio_x
        if error_ratio_x > error_ratio_y:
            if (config.width % 16 != 0):
                config.width = temp_width + (16 - (temp_width % 16))
            else:
                config.width = temp_width
            config.height = int(config.width * 9.0 / 16)
        else:
            if (config.height % 9 != 0):
                config.height = temp_height + (9 - (temp_height % 9))
            else:
                config.height = temp_height
            config.width = int(config.height * 16 / 9.0)

        print "final width: ", config.width
        print "final height: ", config.height
        self.screen = pygame.display.set_mode((config.width, config.height), config.screen_setting)
        self.background_left = Background(config.width/2, config.height)
        self.background_right = Background(config.width/2, config.height)
        width, height = self.screen.get_size()
        print width, height
        self.back_screen = pygame.Surface((width, height))
        self.__initbackgrounds()

    def __initbackgrounds(self):
        width, height = self.screen.get_size()
        self.left_back_screen = self.back_screen.subsurface(0, 0, width/2, height)
        self.right_back_screen = self.back_screen.subsurface(width/2, 0, width/2, height)
        self.background_left.resize_textures(width, height)
        self.background_right.resize_textures(width, height)

    def apply_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.is_running = False
            elif event.type == KEYDOWN:
                if event.key in config.quitkeys:
                    self.is_running = False
                if event.key == K_DOWN:
                    print "Down pressed."
                print event
            elif event.type == VIDEORESIZE:
                config.width = event.w
                config.height = event.h
                self.__resizeall()
            #TODO: handle VIDEORESIZE
    def update(self):
        self.apply_events()
        self.background_left.update(self.left_back_screen)
        self.background_left.update(self.right_back_screen)
        self.screen.blit(self.back_screen, (0,0))
        pygame.display.flip()
