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
        # get closest aspect to 16:9 and set to that.
        temp_height = int(config.width * 9 / 16.0)
        temp_width = int(config.height * 16 / 9.0)

        # determine which is a larger % shift from the other and use the lower.
        error_ratio_y = float(config.height) / temp_height
        error_ratio_x = float(config.width) / temp_width
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

        self.screen = pygame.display.set_mode((config.width, config.height), config.screen_setting)
        self.back_screen = self.screen #pygame.Surface((config.width, config.height))

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_screen_done = True
            elif event.type == pygame.KEYDOWN:
                if event.key in config.quitkeys:
                    self.is_screen_done = True
                if event.key in config.downkeys:
                    try: self.down_pressed()
                    except: pass
                if event.key in config.upkeys:
                    try: self.up_pressed()
                    except: pass
                if event.key in config.leftkeys:
                    try: self.left_pressed()
                    except: pass
                if event.key in config.rightkeys:
                    try: self.right_pressed()
                    except: pass
                if event.key in config.jumpkeys:
                    try: self.jump_pressed()
                    except: pass
                if event.key in config.swapkeys:
                    try: self.swap_pressed()
                    except: pass
                if event.key in config.leftkeys:
                    try: self.left_pressed()
                    except: pass
            elif event.type == pygame.KEYUP:
                if event.key in config.downkeys:
                    try: self.down_released()
                    except: pass
                if event.key in config.upkeys:
                    try: self.up_released()
                    except: pass
                if event.key in config.leftkeys:
                    try: self.left_released()
                    except: pass
                if event.key in config.rightkeys:
                    try: self.right_released()
                    except: pass
                if event.key in config.jumpkeys:
                    try: self.jump_released()
                    except: pass
                if event.key in config.swapkeys:
                    try: self.swap_released()
                    except: pass
                if event.key in config.leftkeys:
                    try: self.left_released()
                    except: pass
            elif event.type == pygame.VIDEORESIZE:
                config.width = event.w
                config.height = event.h
                self.__resizeall()
                self.resize()

    def super_active(self):
        self.__resizeall()
        try: self.resize()
        except: pass

    def super_isdone(self):
        return self.is_screen_done

    def update_super(self, dt):
        self.process_events()
        rects = self.update(dt)
        #self.screen.blit(self.back_screen, (0,0))
        if rects:
            #get a list of all rects, doubled for both sides of the screen.
            final_rects = []
            for rect in rects:
                final_rects.append(rect)
                final_rects.append(rect.move(self.back_screen.get_size()[0] / 2, 0))
            pygame.display.update(final_rects)
        else:
            pygame.display.update()
        #pygame.display.flip()
