WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 600
PLAYER_GRAV = 0.8
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
Switch = False

PLATFORM_LIST = [(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40),
                 (SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT * 3 / 4, 100, 20),
                 (125, SCREEN_HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]