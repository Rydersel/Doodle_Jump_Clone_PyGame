import pygame as pg
size = (480, 600)
screen = pg.display.set_mode(size)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
SCREEN_WIDTH = 480
background_image = pg.image.load("76291.jpg")
SCREEN_HEIGHT = 600
PLAYER_GRAV = 0.8
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_JUMP = 20
FONT_NAME = 'Times New Roman'
lava_x = 0
lava_y = 0
vec = pg.math.Vector2
File = "highscore.txt"
SPRITESHEET = "sokoban_spritesheet@2.png"
Switch = 0
Boost_Power = 60
POW_SPAWN = 7
def changespeed(self, x, y):
    """ Change the speed of the player. """
    self.change_x += x
    self.change_y += y

PLATFORM_LIST = [(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40),
                 (SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT * 3 / 4, 100, 20),
                 (125, SCREEN_HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]