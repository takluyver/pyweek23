from pygame.locals import *
import os.path

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
jumpkeys = [K_SPACE]
swapkeys = [K_UP, K_RETURN]

INSTALL_DIR = "/app/share/solarflair"  # Flatpak installed
INSTALL_DIR = ""  # Running from git - comment this out before building with Flatpak

def asset(*path):
    return os.path.join(INSTALL_DIR, "assets", *path)

#don't change any of this unless you want to watch the world burn.
FONT_ROOT = os.path.join(INSTALL_DIR, "assets", "fonts")
IMAGE_ROOT = os.path.join(INSTALL_DIR, "assets", "images")
HIGH_SCORES = os.path.join(INSTALL_DIR, "highscores.txt")

#don't change this.
GAME_WIDTH = 1920 # half of 4K width
GAME_HEIGHT = 2160 # 4K height

def reload_scores():
    global highscores
    highscores = []
    f = open(HIGH_SCORES)
    for line in f.readlines():
        highscores.append((line.split("|")[0], int(line.split("|")[1].strip())))
    f.close()

def update_scores(newscores):
    # only accept the top 10 scores.
    newscores = newscores[:10]
    scorefile = open(HIGH_SCORES, "w")
    for score in newscores:
        scorefile.write(score[0] + "|" + str(int(score[1])) + "\n")
    scorefile.close()
    reload_scores()

reload_scores()
highscores
