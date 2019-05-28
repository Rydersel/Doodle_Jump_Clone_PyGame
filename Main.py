import pygame as pg
import random
from Settings import *
from Sprites import *

class Game:

    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Pygame_Final")
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
    def new(self):
        # start a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        if self.player.rect.top <= SCREEN_HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= SCREEN_HEIGHT:
                    plat.kill()
                    self.score += 100

        if self.player.rect.bottom > SCREEN_HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False


            self.playing = False
        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, SCREEN_WIDTH - width),
                         random.randrange(-75, -30),
                         width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)

    if Switch == 0:
        def events(self):
            # Game Loop - events
            for event in pg.event.get():
                # check for closing window
                if event.type == pg.QUIT:
                    if self.playing:
                        self.playing = False
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        self.player.jump()
    if Switch == 1:
        def events(self):
            # Game Loop - events
            for event in pg.event.get():
               global x
               global y
               x = 50
               y = 50
               if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
               if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_LEFT]:
                    x -= PLAYER_ACC
                if keys[pg.K_RIGHT]:
                    x += PLAYER_ACC
                if keys[pg.K_UP]:
                    y -= PLAYER_ACC
                if keys[pg.K_DOWN]:
                    y += PLAYER_ACC

    def draw(self):
        # Game Loop - draw
        self.screen.fill(LIGHTBLUE)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 23, RED, SCREEN_WIDTH / 2 , 15)
        pg.display.flip()


    def show_start_screen(self):
        self.screen.fill(LIGHTBLUE)
        self.draw_text("PyGame Final"
                       "", 48, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text("Instructions: Arrows to move, Up Arrow to jump", 22, WHITE,SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.draw_text("Press any key to continue", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 /4 )
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        if not self.running:
            return
        self.screen.fill(RED)
        self.draw_text("GAME OVER", 48, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text("Score: "+ str(self.score), 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.draw_text("Press any key to continue", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()