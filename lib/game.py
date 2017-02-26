import random
import pygame
from pygame.locals import *
import config
from background import Background
from screenhandler import ScreenHandler
from state import State
from gameobject import PlatformObject
from gameobject import StarObject
import utils
from platform import PlatformManager

class Game(State, ScreenHandler):
    def __init__(self):
        super(Game, self).__init__()
        width, height = self.back_screen.get_size()
        self.background_left = Background(width/2, height)
        self.background_right = Background(width/2, height)
        self.position = (960,0)
        self.bright_star = StarObject(["sprites/star1.png", "sprites/star2.png", "sprites/star3.png"], self.position, width/2, height, 0)
        self.dark_star = StarObject(["sprites/dark1.png", "sprites/dark2.png", "sprites/dark3.png"], self.position, width/2, height, 0)

        self.right_platforms = []
        self.left_platforms = []
        y = 0
        x = 200
        manager = PlatformManager()
        for i in range(0, 100):
            y += random.randint(250,450)
            x += random.randint(-450, 450)
            if (x < 0):
                x = 0
            if x > config.GAME_WIDTH - 500:
                x = config.GAME_WIDTH - 500
            z = random.choice([True, False])
            size = random.randint(3, 9)
            plat = PlatformObject(manager, z, (x, y), size, width/2, height, 0)
            if not z:
                self.left_platforms.append(plat)
            else:
                self.right_platforms.append(plat)
        #plat = PlatformObject(True, (600, 600), 8, width/2, height, 0)

        self.__sizetextures()
        self.displacement = 0
        self.is_displacing = False
        self.keyvector = (0,0)
        self.movement_speed = 1
        self.vertical_speed = 0
        self.is_done = False
        self.moving_left = False
        self.moving_right = False
        self.active_player = 0
        self.gravity = -15
        self.score = 0
        self.ramprate = 1
        self.scorefont = utils.get_font("Hi Score: " + str(config.highscores[0][1]).zfill(10) + " Score: " + str(self.score).zfill(10), "good times rg.ttf", 35, (255,255,255), None)

    def update(self, dt):
        width, height = self.back_screen.get_size()

        # TODO: implement gravity
        # dt / 1000 to get fractional seconds and / 2 to get proper integration https://www.niksula.hut.fi/~hkankaan/Homepages/gravity.html
        self.vertical_speed += self.gravity * (dt / 1000.0)
        #scroll the screen
        if self.is_displacing:
            self.displacement += (dt / 3.0) + (self.displacement / 3000.0)
            self.score = self.displacement

        #only check this if the star is moving negative so we don't stick the star to stuff

        if self.vertical_speed < 0 and self.activesun_on_platform():
            self.vertical_speed = 0 # reset vertical speed since we're on a platform that's currently active.

        if self.moving_left:
            self.keyvector = (-1, self.vertical_speed)
        elif self.moving_right:
            self.keyvector = (1, self.vertical_speed)
        else:
            self.keyvector = (0,self.vertical_speed)

        #collect all our dirty rects (must be done before player moves)
        dirty_rects = [self.bright_star.getscreenrect((width/2, height))]

        #reposition the player
        self.position = (self.position[0] + dt * self.keyvector[0] * self.movement_speed,
                        self.position[1] + dt * self.keyvector[1] * self.movement_speed)
        if self.vertical_speed <= 0 and self.activesun_on_platform():
            self.position = (self.position[0], self.get_sun_platform_offset())
        self.position = self.bright_star.move((self.position[0], max(self.position[1], 1)), dt)
        # start scrolling once past halfway point.
        if (self.position[1] > config.GAME_HEIGHT / 2):
                self.is_displacing = True

        self.dark_star.move(self.position, dt)

        #set our state to done if player is dead
        if (self.bright_star.isdead()):
            #save our score.
            #TODO: make this less ghetto
            newscores = []
            has_scored = False
            for hiscore in config.highscores:
                if not has_scored and hiscore[1] < int(self.score): #we have a score higher than this one so insert now.
                    has_scored = True
                    newscores.append(("XXX", self.score))
                newscores.append(hiscore)
            if not has_scored:
                newscores.append(("XXX", self.score))
            config.update_scores(newscores)
            self.is_done = True




        dirty_rects.append(pygame.rect.Rect(0, 20, width/2, self.scorefont.get_size()[1] + 30))
        for platform in self.left_platforms:
            if platform.is_onscreen(self.displacement):
                dirty_rects.append(platform.getscreenrect((width/2, height)))

        for platform in self.right_platforms:
            if platform.is_onscreen(self.displacement):
                dirty_rects.append(platform.getscreenrect((width/2, height)))

        #redraw background
        updateall = self.background_left.update(self.back_screen.subsurface(0, 0, width/2, height), dirty_rects)
        self.background_right.update(self.back_screen.subsurface(width/2, 0, width/2, height), dirty_rects)


        #draw platforms
        #TODO: make dirty_rects an screen_dirty 2 separate lists, and then extend them.
        for platform in self.left_platforms:
            if platform.is_onscreen(self.displacement):
                platform.update(self.back_screen.subsurface(0, 0, width/2, height), self.displacement, dt)
                dirty_rects.append(platform.getscreenrect((width/2, height)))

        for platform in self.right_platforms:
            if platform.is_onscreen(self.displacement):
                platform.update(self.back_screen.subsurface(width/2, 0, width/2, height), self.displacement, dt)
                dirty_rects.append(platform.getscreenrect((width/2, height)))

        if (self.active_player == 0):
            self.bright_star.update(self.back_screen.subsurface(0, 0, width/2, height), self.displacement, dt)
            self.dark_star.update(self.back_screen.subsurface(width/2, 0, width/2, height), self.displacement, dt)
        else:
            self.bright_star.update(self.back_screen.subsurface(width/2, 0, width/2, height), self.displacement, dt)
            self.dark_star.update(self.back_screen.subsurface(0, 0, width/2, height), self.displacement, dt)

        #draw score
        temphi = int(config.highscores[0][1])
        if self.score > temphi:
            temphi = self.score
        self.scorefont = utils.get_font("Hi Score: " + str(int(temphi)).zfill(10) + " Score: " + str(int(self.score)).zfill(10), "monofonto.ttf", 32, (255,255,255), None)
        destrect = pygame.rect.Rect(self.back_screen.get_size()[0] - self.scorefont.get_size()[0] - 20,
                            20, self.scorefont.get_size()[0], self.scorefont.get_size()[1] + 20)

        #make a platform on the left side.
        #destrect = pygame.rect.Rect(0, 0, plat5.get_size()[0], plat5.get_size()[1])
        #dirty_rects.append(destrect)
        #self.back_screen.blit(plat5, destrect)


        #self.left_platforms.append(self.platformmanager.getplatformimage(5))

        #draw font
        self.back_screen.blit(self.scorefont, destrect)
        #TODO: add all current positions to dirty rects so we can pass all to display update.
        dirty_rects.append(self.bright_star.getscreenrect((width/2, height)))

        #double all dirty rects that are in both windows
        #this is really not optimal because the platforms are not on both sides but no time to make better
        final_rects = []
        for rect in dirty_rects:
            final_rects.append(rect)
            final_rects.append(rect.move(self.back_screen.get_size()[0] / 2, 0))

        #Trigger a full screen redraw if anything needs it.
        if updateall:
            return None
        return final_rects

    #determine if active sun is on an active platform.
    def activesun_on_platform(self):
        isonplat = False
        if self.active_player == 0:
            for platform in self.left_platforms:
                if platform.is_star_colliding(self.bright_star.get_bottomleft(), self.bright_star.get_bottomright()):
                    isonplat = True
                    break
        else:
            for platform in self.right_platforms:
                if platform.is_star_colliding(self.bright_star.get_bottomleft(), self.bright_star.get_bottomright()):
                    isonplat = True
                    break

        return isonplat

    def get_sun_platform_offset(self):
        if self.active_player == 0:
            for platform in self.left_platforms:
                if platform.is_star_colliding(self.bright_star.get_bottomleft(), self.bright_star.get_bottomright()):
                    return platform.get_top()
        else:
            for platform in self.right_platforms:
                if platform.is_star_colliding(self.bright_star.get_bottomleft(), self.bright_star.get_bottomright()):
                    return platform.get_top()


    def jump_pressed(self):
        if self.activesun_on_platform() or self.position[1] < 10:
            self.vertical_speed = 4
            #self.position = (self.position[0], self.position[1] + 150)

    def swap_pressed(self):
        self.active_player = not self.active_player
        for platform in self.left_platforms:
            platform.toggle_dark()
        for platform in self.right_platforms:
            platform.toggle_dark()

    def left_pressed(self):
        self.moving_left = True
    def left_released(self):
        self.moving_left = False

    def right_pressed(self):
        self.moving_right = True
    def right_released(self):
        self.moving_right = False

    def isdone(self):
        return self.is_done

    def resize(self):
        self.__sizetextures()

    def __sizetextures(self):
        width, height = self.back_screen.get_size()
        self.background_left.resize_textures(width/2, height)
        self.background_right.resize_textures(width/2, height)
        self.bright_star.resize(width/2, height)
        self.dark_star.resize(width/2, height)
        for platform in self.left_platforms:
            platform.resize(width/2, height)
        for platform in self.right_platforms:
            platform.resize(width/2, height)
