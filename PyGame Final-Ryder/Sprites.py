
from Settings import *

from random import choice, randrange
class Player(pg.sprite.Sprite):

    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.jumping = False
        self.image = game.spritesheet.get_image(557, 108, 42, 50)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.pos = vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)



    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > SCREEN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = SCREEN_WIDTH
        self.rect.midbottom = self.pos

#Player Jump
    def jump(self):
        self.rect.x += 2
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 2
        if hits and  not self.jumping:
            self.game.jump_sound.play()
        if hits:
            self.vel.y = -20
#Random platfrom generation
class Platforms(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#Class for Spritesheet
class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()
    #Method for cutting image out of spritesheet
    def get_image(self, x, y, width, height):
        image = pg.Surface((width,height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (width // 2, height // 2))
        return image