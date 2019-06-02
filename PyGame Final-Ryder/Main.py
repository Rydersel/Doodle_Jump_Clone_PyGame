
#importing pygame as pg to simplify code
import pygame as pg
from os import path
import random
from Settings import *
from Sprites import *
import random
class Game:
    def __init__(self):
        # Run on Init
        pg.mixer.init()
        pg.init()
        self.screen = screen
        pg.display.set_caption("Pygame_Final")
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.data()
        #Plays background song on Init
        pg.mixer.music.load('13 Digital Native.mp3')
        pg.mixer.music.play(loops=-1)
        pg.mixer.music.play()

    #Makes bliting text alot easier
    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)




    #Storing Data for highscore/playing jump sound/loading spritesheet
    def data(self):

        self.jump_sound = pg.mixer.Sound('Jump16.wav')
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'Image')
        with open(path.join(self.dir, File), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        # load spritesheet image
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))



    def run(self):
        # The Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop Update

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
        #Scrolling Screen
        if self.player.rect.bottom > SCREEN_HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False


        #How many platforms are allowed on the screen at once
        while len(self.platforms) < 7:
            width = random.randrange(50, 100)
            #Randomizing platform size and location
            p = Platforms(random.randrange(0, SCREEN_WIDTH - width),
                         random.randrange(-75, -30),
                         width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)

    if Switch == 0:
        def events(self):
            # Game Loop - events
            for event in pg.event.get():
                #If Window is Clossed
                if event.type == pg.QUIT:
                    if self.playing:
                        self.playing = False
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        self.player.jump()

    def new(self):
        # start a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platforms(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    #Draw Sorites on Screen
    def draw(self):
        # Game Loop - draw
        self.screen.fill(SKYBLUE)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 23, RED, SCREEN_WIDTH / 2 , 15)
        #Outlining playable area
        pg.draw.rect(screen, BLACK, [0, 0, SCREEN_WIDTH, line_width])
        pg.draw.rect(screen, BLACK, [0, SCREEN_HEIGHT, SCREEN_WIDTH, line_width])
        pg.draw.rect(screen, BLACK, [0, 0, line_width, SCREEN_HEIGHT])
        pg.draw.rect(screen, BLACK, [SCREEN_WIDTH, 0, line_width, SCREEN_HEIGHT + line_width])
        pg.display.flip()
        #Show Welcome Screen

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(SKYBLUE)
        self.draw_text("Pygame Final", 48, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text("Arrows to move, Space to jump", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_WIDTH / 2)
        self.draw_text("Press a key to play", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()
    def show_end_screen(self):
        # game End Screen
        if not self.running:
            return
        self.screen.fill(RED)
        self.draw_text("GAME OVER", 48, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.draw_text("Press any key to play again ----->", 22, WHITE, SCREEN_HEIGHT / 2, SCREEN_HEIGHT * 3 / 3)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40)
            with open(path.join(self.dir, File), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("High Score: " + str(self.highscore), 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40)
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


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_end_screen()

pg.quit()