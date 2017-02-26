import pygame
from state import State
from screenhandler import ScreenHandler
from utils import scale_rect, get_font

class Fader(ScreenHandler, State):
    def __init__(self, text, fadeinms, fadeoutms, totalms, fontname, color):
        super(Fader, self).__init__()
        self.label = get_font(text, fontname, 240, color)
        self.fadeinms = fadeinms
        self.fadeoutms = fadeoutms
        self.totalms = totalms
        self.currentms = 0
        self.is_done = False
        #start with a width of 60%
        self.width = .8
        self.alpha = 0


    def update(self, dt):
        self.currentms += dt
        if self.currentms <= self.fadeinms:
            #determine how far it is from 0 to fadeinms and that is the percentage of darkening.
            self.alpha = (float(self.currentms) / self.fadeinms) * 255
        elif self.currentms >= self.totalms - self.fadeoutms:
            self.alpha = ((float(self.totalms - self.currentms) / self.fadeoutms) * 255)
        self.width = 0.8 + (self.currentms / float(self.totalms)) * .1

        if self.currentms >= self.totalms:
            self.is_done = True

        center = self.screen.get_rect().center
        target = scale_rect(self.screen.get_rect(), self.label.get_rect(), self.width, self.width)
        target_surf = pygame.transform.smoothscale(self.label, (target.width, target.height))
        target_surf.set_alpha(self.alpha)
        #shift to be in the center of the screen
        target.center = center
        self.back_screen.fill((0,0,0), self.back_screen.get_rect())
        self.back_screen.blit(target_surf, target)


    def isdone(self):
        return self.is_done
