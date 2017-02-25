import pygame
import config

class ScreenHandler(object):
    def __init__(self):
        super(ScreenHandler, self).__init__()
        self.is_screen_done = False
        self.__resizeall()

    def resize(self): ## OVERRIDE THIS
        pass

    def __resizeall(self):
        print "resized"
        # get closest aspect to 16:9 and set to that.
        temp_height = int(config.width * 9 / 16.0)
        temp_width = int(config.height * 16 / 9.0)

        #print "width: ", config.width, " temp_width: ", temp_width
        #print "height: ", config.height, " temp_height: ", temp_height
        # determine which is a larger % shift from the other and use the lower.
        error_ratio_y = float(config.height) / temp_height
        error_ratio_x = float(config.width) / temp_width
        #print "error y: ", error_ratio_y
        #print "error x: ", error_ratio_x
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

        #print "final width: ", config.width
        #print "final height: ", config.height
        self.screen = pygame.display.set_mode((config.width, config.height), config.screen_setting)
        self.back_screen = pygame.Surface((config.width, config.height))

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_screen_done = True
            elif event.type == pygame.KEYDOWN:
                if event.key in config.quitkeys:
                    self.is_screen_done = True
                if event.key == pygame.K_DOWN:
                    print "Down pressed."
                #print event
            elif event.type == pygame.VIDEORESIZE:
                config.width = event.w
                config.height = event.h
                self.__resizeall()
                self.resize()

    def super_active(self):
        self.__resizeall()

    def super_isdone(self):
        return self.is_screen_done

    def update_super(self, dt):
        #print "update screen dt: ", dt
        self.process_events()
        self.update(dt)
        self.screen.blit(self.back_screen, (0,0))
        pygame.display.flip()
