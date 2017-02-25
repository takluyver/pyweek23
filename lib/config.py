from pygame.locals import *

#display settings
width = 1920
height = 1080
screen_setting = RESIZABLE

# Keyboard settings
quitkeys = [K_ESCAPE]
downkeys = [K_DOWN, K_s]
upkeys = [K_UP, K_w]
leftkeys = [K_LEFT, K_a]
rightkeys = [K_RIGHT, K_d]
jumpkeys = [K_UP]
swapkeys = [K_SPACE, K_RETURN]



#don't change any of this unless you want to watch the world burn.
FONT_ROOT = "assets/fonts/"

IMAGE_ROOT = "assets/images/"

#don't change this.
GAME_WIDTH = 1920 # half of 4K width
GAME_HEIGHT = 2160 # 4K height

highscores = []
for line in file("highscores.txt").readlines():
    highscores.append(line.split("|"))
