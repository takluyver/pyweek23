import pygame
import config
# from http://www.pygame.org/wiki/RotateCenter
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def get_font(text, fontname, size, color, bgcolor=(0,0,0)):
    font = pygame.font.Font(config.FONT_ROOT + fontname, size)
    if bgcolor == None:
        surf = font.render(text, True, color)
        surf = surf.convert_alpha()
    else:
        surf = font.render(text, True, color, bgcolor)
        surf = surf.convert(32)
    return surf

def aspect_scale(img,(bx,by)):
    """ Scales 'img' to fit into box bx/by.
     This method will retain the original image's aspect ratio """
    ix,iy = img.get_size()
    if ix > iy:
        # fit to width
        scale_factor = bx/float(ix)
        sy = scale_factor * iy
        if sy > by:
            scale_factor = by/float(iy)
            sx = scale_factor * ix
            sy = by
        else:
            sx = bx
    else:
        # fit to height
        scale_factor = by/float(iy)
        sx = scale_factor * ix
        if sx > bx:
            scale_factor = bx/float(ix)
            sx = bx
            sy = scale_factor * iy
        else:
            sy = by

    return pygame.transform.scale(img, (int(sx),int(sy)))

def scale_rect(screen_rect, source_rect, widthpct, heightpct):
    #to make a rect that is 60% of the width, get the current rect, and determine the scale ratio between full screen and
    # current width, then scale to full width, then multiply by scale ratio.
    scale_factor =  screen_rect.width / float(source_rect.width)
    newrect = pygame.rect.Rect(0, 0, source_rect.width * scale_factor * widthpct, source_rect.height * scale_factor * heightpct)
    return newrect
    #TODO: handle height scaling too.


def get_screen_coords(gamecoords, screen, displacement):
    heightratio = float(screen[1]) / config.GAME_HEIGHT
    widthratio = float(screen[0]) / config.GAME_WIDTH
    screencoordy = screen[1] - ((gamecoords[1] - displacement) * heightratio)
    screencoordx = gamecoords[0] * widthratio
    screencoords = screencoordx, screencoordy
    return screencoords
