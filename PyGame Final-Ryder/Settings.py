import pygame as pg
size = (480, 600)
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
SKYBLUE = (0, 155, 155)
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 600
PLAYER_GRAV = 0.8
PLAYER_ACC = 0.6
line_width = 10
PLAYER_FRICTION = -0.12
Jumps = 0
PLAYER_JUMP = 40
#Because Ubuntu is the best font
FONT_NAME = 'Ubuntu'
vec = pg.math.Vector2
#File that stores highscores
File = "highscore.txt"
#Spritesheet I barely ended up using
SPRITESHEET = "sokoban_spritesheet@2.png"
Switch = 0


PLATFORM_LIST = [(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40),
                 (SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT * 3 / 4, 100, 20),
                 (125, SCREEN_HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]