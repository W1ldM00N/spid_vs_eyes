#_ import
import random
import sys
import pygame
from random import randint

#_ init
pygame.init()
pygame.font.init()
pygame.mixer.init()

#_ display creation
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("wild")

#_ set font
my_font = pygame.font.SysFont('Comic Sans MS', 30)

#_ player vars
x = 500
y = 575
wid = 60
heg = 60
mjp = 10
touchable = True
walk_right = [pygame.image.load("pyg/wl1.png"), pygame.image.load("pyg/wl2.png"), pygame.image.load("pyg/wl3.png"),
              pygame.image.load("pyg/pixilart-drawing.png")]
walk_left = [pygame.image.load("pyg/wr1.png"), pygame.image.load("pyg/wr2.png"), pygame.image.load("pyg/wr3.png"),
             pygame.image.load("pyg/pixilart-drawing (1).png")]

#_ enemy vars
x1 = 100
yy = 575
en_pic = pygame.image.load("pyg/enemy.png")

#_ trident vars
tran = 1
tdone = False
ttime = 100
tx = 1000
ty = -300
tttime = 500
tt = True


#_ golden bullet vars
xl = 0
yl = 0
gg = False
lhitbox = (-40, -40, 40, 40)

#_ snake vars
snake_block = 15
snake_speed = 15
snake = []
score = 0
game_over = False
xsh = 500
ysh = 375
xs_change = 0
ys_change = 0
foodx = round(random.randrange(0, 1000 - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, 750 - snake_block) / 10.0) * 10.0

#_ wind vars
wind_pict = pygame.image.load("pyg/windie.png")
wind_pict_2 = pygame.image.load("pyg/windie2.png")
wind_ran = -10
wind_x = 1000
wind_y = 300
wind_vel = 6
wind_dir = 1
wind_start = 0

#_ helpful vars
room = 1
d = 0
frag = 0
rt = -1
rr = 0
bb = 0

#_ maze vars
solved = False
maze = False
justS = False
maze2 = False

#_ fire vars
fy = 0
ran = 1
fire = False
fire_hitbox = (ran, fy, 75, 75)

#_ storm vars
windd = pygame.mixer.Sound("pyg/wind_boss.mp3")
storm_pic = pygame.image.load("pyg/strom.png")
storm_x = 1000
ww = False
s = 0

#_ lighting vars
zap_ran = 1
lig1 = pygame.image.load("pyg/lighting1.png")
lig2 = pygame.image.load("pyg/lighting2.png")
lig3 = pygame.image.load("pyg/lighting3.png")
lig4 = pygame.image.load("pyg/lighting4.png")
lig5 = pygame.image.load("pyg/lighting5.png")
lig6 = pygame.image.load("pyg/lighting6.png")
lig7 = pygame.image.load("pyg/lighting7.png")
lig8 = pygame.image.load("pyg/lighting8.png")
lig9 = pygame.image.load("pyg/lighting9.png")
lig10 = pygame.image.load("pyg/lighting10.png")
lig_em = pygame.image.load("pyg/lighting_empty.png")
warnings = [pygame.image.load("pyg/warning_1.png"), pygame.image.load("pyg/warning_2.png"),
            pygame.image.load("pyg/warning_3.png")]
zap = False
zap_hitbox = (-250, -250, 100, 580)
zapzap = False
warn_i = 0
warn_loop = 0
zap_i = 1

#_ laser vars
lran = 1
ldone = False
ltime = 100
lw = 0
wx = -1000
ly = -300
lltime = 500
lt = True

#_ boss vars
boss = False
boss_2 = False
la = [pygame.image.load("pyg/l1.png"), pygame.image.load("pyg/l2.png"), pygame.image.load("pyg/l3.png"),
      pygame.image.load("pyg/l4.png"), pygame.image.load("pyg/l5.png")]
laugher = pygame.mixer.Sound("pyg/00002a5b.mp3")
bx = -1500
bhp = 150
bhitbox = (bx, -200, 1000, 1000)
windyBoss_start = 0
boss_3 = False
boss_4 = False

#_ setting vars
bg = pygame.image.load("pyg/bg1.png")

bs = pygame.mixer.Sound("pyg/bullet.mp3")
dd = pygame.mixer.Sound("pyg/hit.mp3")
conv = pygame.mixer.Sound("pyg/just-sans-talking.mp3")
ll = [pygame.mixer.Sound("pyg/just-sans-talking.mp3"), pygame.mixer.Sound("pyg/just-sans-talking.mp3"),
      pygame.mixer.Sound("pyg/just-sans-talking.mp3"), pygame.mixer.Sound("pyg/just-sans-talking.mp3"),
      pygame.mixer.Sound("pyg/just-sans-talking.mp3"), pygame.mixer.Sound("pyg/just-sans-talking.mp3")]

pygame.mixer.music.load("pyg/Mus_options_fall.oga")

#_ bird enemy vars
bird_pic = pygame.image.load("pyg/bird.png")

#_ tornado vars
tornado_pict = pygame.image.load("pyg/strom.png")
tornado_x = -50
tornado_y = 300
tornado_hitbox = (tornado_x, tornado_y, 75, 120)

#_ web vars
xw = -100
yw = -100
whitbox = (xw, yw, 50, 50)
web = False
web_pict = pygame.image.load("pyg/web.png")
isWeb = False
webc = 17
mwb = 17
webtime = 1000
awebtime = 5000


#_ classes
class SpiderPlayer:
    def __init__(self, xx, yyy, width, height):
        self.x = xx
        self.y = yyy
        self.width = width
        self.height = height
        self.vel = 5
        self.isjump = False
        self.left = False
        self.right = False
        self.walkC = 0
        self.jumpcount = 10
        self.last = 1
        self.score = 0
        self.hitbox = (self.x, self.y, 60, 60)

    def draw(self, sscreen):
        if self.walkC + 1 >= 18:
            self.walkC = 0
        if self.right:
            sscreen.blit(walk_right[self.walkC // 6], (self.x, self.y))
            self.walkC += 1
        elif self.left:
            sscreen.blit(walk_left[self.walkC // 6], (self.x, self.y))
            self.walkC += 1
        else:
            if self.last == 1:
                sscreen.blit(walk_left[3], (self.x, self.y))
            else:
                sscreen.blit(walk_right[3], (self.x, self.y))
        self.hitbox = (self.x, self.y, 60, 60)
        # pygame.draw.rect(sscreen, (255, 0, 0), self.hitbox, 2)


class Bullet:
    def __init__(self, qx, qy, r, fac):
        self.x = qx
        self.y = qy
        self.r = r
        self.col = (255, 255, 255)
        self.fac = fac
        self.vel = 8 * fac
        self.hitbox = (self.x - self.r, self.y - self.r, 10, 10)

    def draw(self, scren):
        if gg:
            self.col = (178, 148, 61)
        pygame.draw.circle(scren, self.col, (self.x, self.y), self.r)
        self.hitbox = (self.x - self.r - 2, self.y - 2 - self.r, 14, 14)
        # pygame.draw.rect(scren, (255, 0, 0), self.hitbox, 2)


class Enemy:
    def __init__(self, ex, ey, w, h):
        self.x = ex
        self.y = ey
        self.wid = w
        self.heg = h
        self.path = [10, 950]
        self.visible = True
        self.dir = 1
        self.vel = 1.5
        self.hp = 10
        self.hitbox = (self.x, self.y, self.wid, self.heg)

    def draw(self, scr):
        if self.visible:
            scr.blit(en_pic, (self.x, self.y))
            self.hitbox = (self.x, self.y, self.wid, self.heg)
            # pygame.draw.rect(scr, (255, 0, 0), self.hitbox, 2)
            pygame.draw.rect(scr, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(scr, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.hp)), 10))
        else:
            zz = randint(1, 2)
            if zz == 1:
                self.x = 10
            else:
                self.x = 950
            self.hp = 12
            self.visible = True


class Boss:
    def __init__(self, x3, y2, w, h, image, hp):
        self.x = x3
        self.y = y2
        self.wid = w
        self.heg = h
        self.pos = 1
        self.vel = 1.5
        self.hp = hp
        self.pict = image
        self.hitbox = (self.x, self.y, self.wid, self.heg)

    def draw(self, scr):
        scr.blit(self.pict, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.wid, self.heg)
        # pygame.draw.rect(scr, (255, 0, 0), self.hitbox, 2)


class BirdEnemy:
    def __init__(self, xb, by, w, h):
        self.x = xb
        self.y = by
        self.wid = w
        self.heg = h
        self.path = [-10, 1010]
        self.dir = 1
        self.vel = 3
        self.tr = 0
        self.hitbox = (self.x, self.y, self.wid, self.heg)

    def draw(self, ss):
        ss.blit(bird_pic, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.wid, self.heg)
        # pygame.draw.rect(scr, (255, 0, 0), self.hitbox, 2)


#_ init classes
spid = SpiderPlayer(x, y, wid, heg)
enemy = Enemy(x1, yy, 50, 50)
enemy2 = Enemy(-10000, yy, 50, 50)
birdie = BirdEnemy(-1000, 305, 75, 60)
flyingBoss = Boss(-1000, 100, 500, 375, pygame.image.load("pyg/boss-2-2.png"), 400)
windyBoss = Boss(-1000, 300, 360, 320, pygame.image.load("pyg/boss-3.png"), 200)
princeBoss = Boss(-1000, 250, 400, 400, pygame.image.load("pyg/boss-4.png"), 300)
kingBoss = Boss(-1000, 100, 500, 500, pygame.image.load("pyg/king-2.png"), 500)
bullets = []

#_ clock
clock = pygame.time.Clock()
clock.tick(18)


#_ blow
def catscene():
    global storm_x, ww
    storm_x -= 15
    screen.blit(storm_pic, (storm_x, 450))
    storm_hitbox = (storm_x, 450, 75, 150)
    if pygame.Rect.colliderect(pygame.Rect(spid.hitbox), pygame.Rect(storm_hitbox)):
        ww = True
    if ww:
        spid.x -= 15
        spid.y -= 7.5
    spid.draw(screen)
    pygame.display.update()


#_ big o finale
def final():
    screen.fill((0, 0, 0))
    screen.blit(pygame.image.load("pyg/boss.png"), (250, 50))
    deadtext = my_font.render("GOOD JOB!!", False, (255, 255, 255))
    screen.blit(deadtext, (70, 650))
    pygame.display.update()
    pygame.time.wait(1000)
    screen.fill((0, 0, 0))
    screen.blit(pygame.image.load("pyg/boss.png"), (250, 50))
    deadtext = my_font.render("YOU MADE ME A NEW KING OF THIS WORLD!", False, (255, 255, 255))
    screen.blit(deadtext, (70, 650))
    pygame.display.update()
    pygame.time.wait(2500)
    screen.fill((0, 0, 0))
    screen.blit(pygame.image.load("pyg/boss.png"), (250, 50))
    deadtext = my_font.render("I AM REALLY THANKFUL RIGHT NOW!!!", False, (255, 255, 255))
    screen.blit(deadtext, (70, 650))
    pygame.display.update()
    pygame.time.wait(2500)
    screen.fill((0, 0, 0))
    screen.blit(pygame.image.load("pyg/boss.png"), (250, 50))
    deadtext = my_font.render("I THINK IT IS GOOD IDEA FOR ME TO PAY YOU )", False, (255, 255, 255))
    screen.blit(deadtext, (70, 650))
    pygame.display.update()
    pygame.time.wait(3000)
    screen.fill((0, 0, 0))
    screen.blit(pygame.image.load("pyg/boss.png"), (250, 50))
    deadtext = my_font.render("IF YOU WANT, YOU CAN BE ANYONE HERE.", False, (255, 255, 255))
    screen.blit(deadtext, (70, 650))
    pygame.display.update()
    pygame.time.wait(3000)
    screen.fill((0, 0, 0))
    screen.blit(pygame.image.load("pyg/boss.png"), (250, 50))
    deadtext = my_font.render("SO WHO WOULD YOU LIKE TO BE?", False, (255, 255, 255))
    screen.blit(deadtext, (70, 650))
    pygame.display.update()
    pygame.time.wait(2000)
    curr = 1
    while True:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load("pyg/boss.png"), (250, 50))
        if curr == 1:
            dd1 = my_font.render("I wanna go home", False, (240, 83, 101))
            screen.blit(dd1, (70, 600))
        else:
            dd1 = my_font.render("I wanna go home", False, (255, 255, 255))
            screen.blit(dd1, (70, 600))
        if curr == 2:
            dd1 = my_font.render("I wanna be a prince", False, (240, 83, 101))
            screen.blit(dd1, (70, 650))
        else:
            dd1 = my_font.render("I wanna be a prince", False, (255, 255, 255))
            screen.blit(dd1, (70, 650))
        if curr == 3:
            dd1 = my_font.render("You liar! I'll kill you!", False, (240, 83, 101))
            screen.blit(dd1, (70, 700))
        else:
            dd1 = my_font.render("You liar! I'll kill you!", False, (255, 255, 255))
            screen.blit(dd1, (70, 700))
        pygame.display.update()

        for evnt in pygame.event.get():
            if evnt.type == pygame.QUIT:
                sys.exit()
            if evnt.type == pygame.KEYDOWN:
                if evnt.key == pygame.K_UP and curr != 1:
                    curr -= 1
                if evnt.key == pygame.K_DOWN and curr != 3:
                    curr += 1
                if evnt.key == pygame.K_z:
                    if curr == 1:
                        screen.fill((0, 0, 0))
                        screen.blit(pygame.image.load("pyg/boss.png"), (250, 50))
                        pygame.display.update()
                        screen.fill((0, 0, 0))
                        screen.blit(pygame.image.load("pyg/boss.png"), (250, 50))
                        deadtext = my_font.render("Alright)", False, (255, 255, 255))
                        screen.blit(deadtext, (70, 650))
                        pygame.display.update()
                        pygame.time.wait(2000)
                        screen.fill((255, 255, 255))
                        deadtext = my_font.render("You are home. Good night!", False, (0, 0, 0))
                        screen.blit(deadtext, (330, 300))
                        pygame.display.update()
                        pygame.time.wait(5000)
                        sys.exit()
                    if curr == 2:
                        screen.fill((0, 0, 0))
                        screen.blit(pygame.image.load("pyg/boss.png"), (250, 50))
                        pygame.display.update()
                        screen.fill((0, 0, 0))
                        screen.blit(pygame.image.load("pyg/boss.png"), (250, 50))
                        deadtext = my_font.render("Alright)", False, (255, 255, 255))
                        screen.blit(deadtext, (70, 650))
                        pygame.display.update()
                        pygame.time.wait(2000)
                        screen.fill((0, 0, 0))
                        deadtext = my_font.render("You are prince. Good night!", False, (255, 255, 255))
                        screen.blit(deadtext, (330, 300))
                        screen.blit(pygame.image.load("pyg/prince_end.png"), (450, 150))
                        pygame.display.update()
                        pygame.time.wait(5000)
                        sys.exit()
                    if curr == 3:
                        screen.fill((0, 0, 0))
                        screen.blit(pygame.image.load("pyg/boss.png"), (250, 50))
                        pygame.display.update()
                        screen.fill((0, 0, 0))
                        screen.blit(pygame.image.load("pyg/boss.png"), (250, 50))
                        deadtext = my_font.render("Seriously? Alright =)", False, (255, 255, 255))
                        screen.blit(deadtext, (70, 650))
                        pygame.display.update()
                        pygame.time.wait(2000)
                        screen.fill((0, 0, 0))
                        deadtext = my_font.render("You are dead =). Good night!", False, (255, 255, 255))
                        screen.blit(deadtext, (330, 300))
                        screen.blit(pygame.image.load("pyg/dead_end.png"), (450, 150))
                        pygame.display.update()
                        pygame.time.wait(5000)
                        sys.exit()


#_ fireball atack
def atack(fire_x, fire_y, pict):
    global fire
    global d
    global fire_hitbox
    fire = True
    fire_hitbox = (fire_x, fire_y, 75, 75)
    if touchable and pygame.Rect.colliderect(pygame.Rect(fire_hitbox), pygame.Rect(spid.hitbox)):
        d = -1
        dd.play()
        updater()
        pygame.time.wait(5000)
        sys.exit()
    if fire_y >= 550:
        fire = False
    if fire:
        screen.blit(pict, (fire_x, fire_y))
        pygame.display.update()


#_ zap atack
def zaptack(zap_x, zap_y):
    global zap, d, zap_hitbox, zapzap, warn_i, warn_loop, zap_i
    if zap and not zapzap:
        screen.blit(warnings[warn_i//3], (zap_x, 520))
        pygame.display.update()
        warn_i += 1
        if warn_i >= 6:
            warn_i = 0
            warn_loop += 1
            if warn_loop >= 12:
                warn_loop = 0
                zapzap = True
    elif zap and zapzap:
        if zap_i == 1:
            screen.blit(lig1, (zap_x, zap_y))
            pygame.display.update()
            zap_hitbox = (zap_x, zap_y, 100, 280)
            zap_i += 1
        elif zap_i % 2 == 0:
            screen.blit(lig_em, (zap_x, zap_y))
            pygame.display.update()
            zap_hitbox = (zap_x, zap_y, 100, 280)
            zap_i += 1
        elif zap_i == 3:
            screen.blit(lig2, (zap_x, zap_y))
            pygame.display.update()
            zap_hitbox = (zap_x, zap_y, 100, 580)
            zap_i += 1
        elif zap_i == 5:
            screen.blit(lig3, (zap_x, zap_y))
            pygame.display.update()
            zap_hitbox = (zap_x, zap_y, 100, 580)
            zap_i += 1
        elif zap_i == 7:
            screen.blit(lig4, (zap_x, zap_y))
            pygame.display.update()
            zap_hitbox = (zap_x, zap_y, 100, 580)
            zap_i += 1
        elif zap_i == 9:
            screen.blit(lig5, (zap_x, zap_y))
            pygame.display.update()
            zap_hitbox = (zap_x, zap_y, 100, 580)
            zap_i += 1
        elif zap_i == 11:
            screen.blit(lig6, (zap_x, zap_y))
            pygame.display.update()
            zap_hitbox = (zap_x, zap_y, 100, 580)
            zap_i += 1
        elif zap_i == 13:
            screen.blit(lig7, (zap_x, zap_y))
            pygame.display.update()
            zap_hitbox = (zap_x, zap_y, 100, 580)
            zap_i += 1
        elif zap_i == 15:
            screen.blit(lig8, (zap_x, zap_y))
            pygame.display.update()
            zap_hitbox = (zap_x, zap_y, 100, 580)
            zap_i += 1
        elif zap_i == 17:
            screen.blit(lig9, (zap_x, zap_y))
            pygame.display.update()
            zap_hitbox = (zap_x, zap_y, 100, 580)
            zap_i += 1
        elif zap_i == 19:
            screen.blit(lig10, (zap_x, zap_y))
            pygame.display.update()
            zap_hitbox = (zap_x, zap_y, 100, 580)
            zap_i += 1
            zap_i = 1
            zap = False
            zapzap = False


#_ display update
def updater():
    if d != 7 and d != 21 and d != 40 and d != 61 and not maze and d != 151:
        screen.blit(bg, (0, 0))
        for bul in bullets:
            bul.draw(screen)
        enemy.draw(screen)
        spid.draw(screen)
        birdie.draw(screen)
        text = my_font.render(str(spid.score), False, (255, 255, 255))
        screen.blit(text, (10, 10))
        flyingBoss.draw(screen)
        windyBoss.draw(screen)
        princeBoss.draw(screen)
        kingBoss.draw(screen)
        pygame.draw.rect(screen, (255, 0, 0), (100, ly, lw, 300))
        screen.blit(pygame.image.load("pyg/trident.png"), (tx, ty))
        screen.blit(pygame.image.load("pyg/wave.png"), (wx, 250))
        if rr == 2 and not solved:
            screen.blit(pygame.image.load("pyg/maze.png"), (750, 540))
        if rr == 3 and not solved:
            screen.blit(pygame.image.load("pyg/maze.png"), (750, 540))
        if wind_dir == 1:
            screen.blit(wind_pict, (wind_x, wind_y))
        elif wind_dir == 2:
            screen.blit(wind_pict_2, (wind_x, wind_y))
        if room >= 4:
            enemy2.draw(screen)
        if web:
            deadtext = my_font.render(str(awebtime), False, (255, 255, 255))
            screen.blit(deadtext, (900, 10))
    elif maze:
        screen.fill((0, 0, 0))
        value = my_font.render("You have " + str(score) + "/10", True, (255, 255, 255))
        screen.blit(value, (0, 0))
        for xs in snake:
            pygame.draw.rect(screen, (255, 255, 255), (xs[0], xs[1], snake_block, snake_block))
        pygame.draw.rect(screen, (255, 0, 0), (foodx, foody, snake_block, snake_block))
    elif d == 7:
        screen.fill((0, 0, 0), (0, 0, 1000, 750))
        deadtext = my_font.render("So you did kill him, I did not expect that.", False, (255, 255, 255))
        screen.blit(deadtext, (70, 50))
        deadtext = my_font.render("Anyway if you want to find me,", False, (255, 255, 255))
        screen.blit(deadtext, (70, 90))
        deadtext = my_font.render("you will eliminate every one of their leaders.", False, (255, 255, 255))
        screen.blit(deadtext, (70, 130))
        deadtext = my_font.render("GET OUT OF THIS CAVE!", False, (255, 255, 255))
        screen.blit(deadtext, (70, 170))
        stamp = pygame.image.load("pyg/stamp.png")
        screen.blit(stamp, (450, 300))
    elif d == 21:
        screen.fill((0, 0, 0), (0, 0, 1000, 750))
        deadtext = my_font.render("So another one. Good job!", False, (255, 255, 255))
        screen.blit(deadtext, (70, 50))
        deadtext = my_font.render("OH, you probably wanna know who I am", False, (255, 255, 255))
        screen.blit(deadtext, (70, 90))
        deadtext = my_font.render("Well, I am the one that brought you here", False, (255, 255, 255))
        screen.blit(deadtext, (70, 130))
        deadtext = my_font.render("Now continue your way!", False, (255, 255, 255))
        screen.blit(deadtext, (70, 170))
        stamp = pygame.image.load("pyg/stamp.png")
        screen.blit(stamp, (450, 300))
    elif d == 40:
        screen.fill((0, 0, 0), (0, 0, 1000, 750))
        deadtext = my_font.render("You lost. How pathetic....", False, (255, 255, 255))
        screen.blit(deadtext, (70, 50))
        deadtext = my_font.render("Once someone got serious, you lost", False, (255, 255, 255))
        screen.blit(deadtext, (70, 90))
        deadtext = my_font.render("GET UP! I will take care of him.", False, (255, 255, 255))
        screen.blit(deadtext, (70, 130))
        deadtext = my_font.render("Kill other bosses of the ELEYES", False, (255, 255, 255))
        screen.blit(deadtext, (70, 170))
        stamp = pygame.image.load("pyg/stamp.png")
        screen.blit(stamp, (450, 300))
    elif d == 61:
        screen.fill((0, 0, 0), (0, 0, 1000, 750))
        deadtext = my_font.render("Well, Alright, this was better.", False, (255, 255, 255))
        screen.blit(deadtext, (70, 50))
        deadtext = my_font.render("Only one left... I hope you will win.", False, (255, 255, 255))
        screen.blit(deadtext, (70, 90))
        deadtext = my_font.render("You are going to castle with traps, mazes and the KING.", False, (255, 255, 255))
        screen.blit(deadtext, (70, 130))
        deadtext = my_font.render("He is your next target... Good luck!", False, (255, 255, 255))
        screen.blit(deadtext, (70, 170))
        stamp = pygame.image.load("pyg/stamp.png")
        screen.blit(stamp, (450, 300))
    if d == -1 and room == 1:
        dtext = my_font.render("HAHAHAHAHAHAHAHAHAH, You seriosly died))", False, (255, 0, 0))
        screen.blit(dtext, (10, 675))
    if d == -1 and room == 2:
        dtext = my_font.render("We will not allow you here.", False, (185, 164, 76))
        screen.blit(dtext, (10, 675))
    if d == -1 and room == 3:
        dtext = my_font.render("Look like the game is over =)", False, (73, 65, 109))
        screen.blit(dtext, (10, 675))
    if d == 1:
        dtext = my_font.render("So you did kill my soldier, well, you better stop", False, (255, 0, 0))
        screen.blit(dtext, (10, 675))
    if d == 2:
        dtext = my_font.render("STOP! Or else You will have PROBLEMS!!", False, (255, 0, 0))
        screen.blit(dtext, (10, 675))
    if d == 3:
        dtext = my_font.render("Another Kill and I will come after You!!!", False, (255, 0, 0))
        screen.blit(dtext, (10, 675))
    if d == 4:
        dtext = my_font.render("WELL, IT IS YOUR PROBLEMS.", False, (255, 0, 0))
        screen.blit(dtext, (10, 675))
    if d == 5:
        end = pygame.image.load("pyg/pixil-frame-0.png")
        screen.blit(end, (bx, -200))
    if d == 6:
        dtext = my_font.render("H-HOW.............................................................", False, (255, 0, 0))
        screen.blit(dtext, (10, 675))
        deadend = pygame.image.load("pyg/pixil-frame-0 (2).png")
        screen.blit(deadend, (bx, -200))
    if d == 10:
        dtext = my_font.render("NO-NO, Your tiny bullets won't hurt them =)", False, (185, 164, 76))
        screen.blit(dtext, (10, 675))
    if d == 11:
        lol = pygame.image.load("pyg/bbu.png")
        screen.blit(lol, (xl, yl))
    if d == 12:
        screen.fill((0, 0, 0), (0, 0, 1000, 750))
        deadtext = my_font.render("Congratulations!", False, (255, 255, 255))
        screen.blit(deadtext, (400, 350))
        deadtext = my_font.render("You got golden bullet!", False, (255, 255, 255))
        screen.blit(deadtext, (350, 400))
    if d == 15:
        deadtext = my_font.render("NOOOOOOO.... My Birdie.... You are going to PAY", False, (185, 164, 76))
        screen.blit(deadtext, (10, 675))
    if d == 20:
        deadtext = my_font.render(".............................Al-lright", False, (185, 164, 76))
        screen.blit(deadtext, (10, 675))
    if d == 24:
        dtext = my_font.render("Well hello there! Look like you've come a litle too far)", False, (73, 65, 109))
        screen.blit(dtext, (10, 675))
    if d == 25:
        dtext = my_font.render("Others were just playing. That's why they died.", False, (73, 65, 109))
        screen.blit(dtext, (10, 675))
    if d == 26:
        dtext = my_font.render("But I won't be that stupid =)", False, (73, 65, 109))
        screen.blit(dtext, (10, 675))
    if d == 27:
        dtext = my_font.render("You're following someone very dangerous.", False, (73, 65, 109))
        screen.blit(dtext, (10, 675))
    if d == 28:
        dtext = my_font.render("But you won't listen to me.", False, (73, 65, 109))
        screen.blit(dtext, (10, 675))
    if d == 29:
        dtext = my_font.render("I won't let you go", False, (73, 65, 109))
        screen.blit(dtext, (10, 675))
    if d == 30:
        dtext = my_font.render("This will be your end =)", False, (73, 65, 109))
        screen.blit(dtext, (10, 675))
    if d == 31:
        dtext = my_font.render("NOW DIE =)", False, (73, 65, 109))
        screen.blit(dtext, (10, 675))
    if d == 45:
        screen.blit(web_pict, (xw, yw))
    if d == 46:
        screen.fill((0, 0, 0), (0, 0, 1000, 750))
        deadtext = my_font.render("Congratulations!", False, (255, 255, 255))
        screen.blit(deadtext, (400, 350))
        deadtext = my_font.render("You got web shuter!", False, (255, 255, 255))
        screen.blit(deadtext, (350, 400))
    if d == 50:
        deadtext = my_font.render("Good day! Uh. How are you there?", False, (255, 155, 66))
        screen.blit(deadtext, (10, 675))
    if d == 51:
        deadtext = my_font.render("Didn't windy kill you?", False, (255, 155, 66))
        screen.blit(deadtext, (10, 675))
    if d == 52:
        deadtext = my_font.render("Alright, well, I guess, I will have to kill you.", False, (255, 155, 66))
        screen.blit(deadtext, (10, 675))
    if d == 53:
        deadtext = my_font.render("Bye!", False, (255, 155, 66))
        screen.blit(deadtext, (10, 675))
    if d == 60:
        deadtext = my_font.render("You-u ..will p-pay for ...this-s!", False, (255, 155, 66))
        screen.blit(deadtext, (10, 675))
    if d == 100:
        deadtext = my_font.render("Good day! So you killed everyone. This is unexpected....", False, (255, 188, 66))
        screen.blit(deadtext, (10, 675))
    if d == 101:
        deadtext = my_font.render("Well, there is no need tp fight, at least anymore...", False, (255, 188, 66))
        screen.blit(deadtext, (10, 675))
    if d == 102:
        deadtext = my_font.render("Maybe we can drink some tea. You have a lot of questions", False, (255, 188, 66))
        screen.blit(deadtext, (10, 675))
    if d == 103:
        deadtext = my_font.render("Don't you?", False, (255, 188, 66))
        screen.blit(deadtext, (10, 675))
    if d == 104:
        deadtext = my_font.render("But you won't accept this offer, will you?", False, (255, 188, 66))
        screen.blit(deadtext, (10, 675))
    if d == 105:
        deadtext = my_font.render("Alright, if you'd like to fight...", False, (255, 188, 66))
        screen.blit(deadtext, (10, 675))
    if d == 106:
        deadtext = my_font.render("WE WILL =)", False, (255, 188, 66))
        screen.blit(deadtext, (10, 675))
    if d == 150:
        deadtext = my_font.render("............................................", False, (255, 188, 66))
        screen.blit(deadtext, (10, 675))
    pygame.display.update()


#_ start music
pygame.mixer.music.play(-1)

while True:

    #_ event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #_ room vars change
    if bb == 0 and d == 5:
        pygame.mixer.music.load("pyg/Mus_f_intro.ogg")
        pygame.mixer.music.play(-1)
        bb += 1
    if d == 8:
        bg = pygame.image.load("pyg/bg2.png")
        spid.y = 565
        enemy.y = 565
        enemy.vel = 3
        enemy.x = 100
        d += 1
        mjp = 12
        spid.jumpcount = mjp
        birdie.x = -10
        pygame.mixer.music.load("pyg/Mus_anothermedium.oga")
        pygame.mixer.music.play(-1)
    if d == 22:
        spid.y = 565
        enemy.y = 565
        enemy.vel = 3
        frag = 400
        bg = pygame.image.load("pyg/bg-3.png")
        pygame.mixer.music.load("pyg/Mus_barrier.oga")
        pygame.mixer.music.play(-1)
        d += 1
        mjp = 12
        spid.jumpcount = mjp
    if d == 41:
        spid.y = 565
        spid.x = 500
        enemy.y = 565
        enemy.x = 10
        enemy2.y = 565
        enemy2.x = 950
        enemy.vel = 3
        enemy2.vel = 3
        enemy2.dir = 1
        frag = 700
        rr = 0
        bg = pygame.image.load("pyg/bg-4.png")
        pygame.mixer.music.load("pyg/Mus_ruins.oga")
        pygame.mixer.music.play(-1)
        mjp = 12
        spid.jumpcount = mjp
        boss_2 = False
        wind_x = -10000
        room = 4
        d -= 41
        wx = -1000
    if d == 62:
        isWeb = False
        spid.y = 565
        spid.x = 0
        enemy.y = 565
        enemy.x = 950
        enemy2.y = 565
        enemy2.x = 10
        enemy.vel = 2.5
        enemy2.vel = 2.5
        frag = 1500
        bg = pygame.image.load("pyg/bg-5-1.png")
        pygame.mixer.music.load("pyg/Mus_chokedup.oga")
        pygame.mixer.music.play(-1)
        rr = 1
        mjp = 12
        spid.jumpcount = mjp
        boss_3 = False
        room = 5
        d = 0

    #_ enemy death
    if enemy.hp <= 0:
        enemy.visible = False
        frag += 1
        if frag == 1:
            d = 1
            ll[d - 1].play()
            updater()
            pygame.time.wait(1000)
            d -= 1
        if frag == 10:
            d = 2
            ll[d - 1].play()
            updater()
            pygame.time.wait(1000)
            d -= 2
        if frag == 230:
            d = 3
            ll[d - 1].play()
            updater()
            pygame.time.wait(1000)
            d -= 3
        if frag == 231:
            d = 4
            ll[d - 1].play()
            updater()
            pygame.time.wait(2000)
            d += 1
            bx = -1005
        if frag == 300:
            d = 11
            xl = enemy.x
            yl = enemy.y
            lhitbox = (xl, yl, 40, 40)
            updater()
        if frag == 420:
            d = 24
            updater()
            pygame.time.wait(2000)
            d -= 1
        if frag == 430:
            d = 25
            updater()
            pygame.time.wait(2000)
            d -= 2
        if frag == 440:
            d = 26
            updater()
            pygame.time.wait(2000)
            d -= 3
        if frag == 500:
            d = 27
            updater()
            pygame.time.wait(2000)
            d -= 4
        if frag == 550:
            d = 28
            updater()
            pygame.time.wait(2000)
            d -= 5
        if frag == 600:
            d = 29
            updater()
            pygame.time.wait(2000)
            d -= 6
        if frag == 610:
            d = 30
            updater()
            pygame.time.wait(2000)
            d -= 7
        if frag == 630:
            d = 31
            updater()
            enemy.x = -5000
            pygame.time.wait(2000)
            d += 1
            boss_2 = True
            pygame.mixer.music.load("pyg/Mus_dummybattle.oga")
            pygame.mixer.music.play(-1)
            windyBoss.x = -365
            windyBoss.pos = 2
        if frag == 900:
            d = 45
            xw = enemy.x
            yw = enemy.y
            whitbox = (xw, yw, 50, 50)
        if frag == 910:
            d = 50
            updater()
            pygame.time.wait(2000)
            d -= 50
        if frag == 920:
            d = 51
            updater()
            pygame.time.wait(2000)
            d -= 51
        if frag == 1000:
            d = 52
            updater()
            pygame.time.wait(2000)
            d -= 52
        if frag == 1099:
            d = 53
            updater()
            pygame.time.wait(2000)
            d -= 53
        if frag == 1100:
            enemy.x = -5000
            enemy2.x = -5000
            pygame.time.wait(2000)
            boss_3 = True
            pygame.mixer.music.load("pyg/Mus_date_tense.oga")
            pygame.mixer.music.play(-1)
            princeBoss.x = -450
            princeBoss.pos = 2
        spid.score += 9

    if enemy2.hp <= 0:
        enemy2.visible = False
        frag += 1
        if frag == 900:
            d = 45
            xw = enemy2.x
            yw = enemy2.y
            whitbox = (xw, yw, 50, 50)
        if frag == 910:
            d = 50
            updater()
            pygame.time.wait(2000)
            d -= 50
        if frag == 920:
            d = 51
            updater()
            pygame.time.wait(2000)
            d -= 51
        if frag == 1000:
            d = 52
            updater()
            pygame.time.wait(2000)
            d -= 52
        if frag == 1099:
            d = 53
            updater()
            pygame.time.wait(2000)
            d -= 53
        if frag == 1100:
            enemy.x = -5000
            enemy2.x = -5000
            pygame.time.wait(2000)
            boss_3 = True
            pygame.mixer.music.load("pyg/Mus_date_tense.oga")
            pygame.mixer.music.play(-1)
            princeBoss.x = -450
            princeBoss.pos = 2
        spid.score += 9

    #_ boss room 1 death
    if bhp <= 0:
        d = 6
        bhitbox = (-2000, -200, 1000, 1000)
        ll[d - 1].play()
        updater()
        pygame.time.wait(2000)
        room = 2
        d = 7
        pygame.mixer.music.load("pyg/Mus_amalgam.oga")
        pygame.mixer.music.play(-1)
        bhp = 10
        updater()
        pygame.time.wait(10000)
        pygame.mixer.music.load("pyg/Mus_options_fall.oga")
        pygame.mixer.music.play(-1)
        d += 1

    #_ bullet check
    for buull in bullets:
        if 1000 > buull.x > 0:
            buull.x += buull.vel
            if pygame.Rect.colliderect(pygame.Rect(buull.hitbox), pygame.Rect(enemy.hitbox)):
                try:
                    bullets.pop(bullets.index(buull))
                except ValueError:
                    q = 1
                if enemy.hp > 0:
                    enemy.hp -= 1
                    if gg:
                        enemy.hp -= 1
            if pygame.Rect.colliderect(pygame.Rect(buull.hitbox), pygame.Rect(enemy2.hitbox)):
                try:
                    bullets.pop(bullets.index(buull))
                except ValueError:
                    q = 1
                if enemy2.hp > 0:
                    enemy2.hp -= 1
                    if gg:
                        enemy2.hp -= 1
            if pygame.Rect.colliderect(pygame.Rect(flyingBoss.hitbox), pygame.Rect(buull.hitbox)):
                try:
                    bullets.pop(bullets.index(buull))
                except ValueError:
                    q = 1
                flyingBoss.hp -= 1
                if flyingBoss.hp == 300:
                    flyingBoss.pos = 2
                    enemy.x = 0
                    flyingBoss.x = 1000
                    flyingBoss.pict = pygame.image.load("pyg/boss-2.png")
                if flyingBoss.hp == 100:
                    flyingBoss.pos = 3
                if flyingBoss.hp == 75:
                    flyingBoss.pos = 4
                    flyingBoss.pict = pygame.image.load("pyg/boss-2-2.png")
                if flyingBoss.hp == 50:
                    flyingBoss.pos = 5
                if flyingBoss.hp == 25:
                    flyingBoss.pos = 7
                if flyingBoss.hp <= 0:
                    flyingBoss.pos = -1
            if pygame.Rect.colliderect(pygame.Rect(princeBoss.hitbox), pygame.Rect(buull.hitbox)):
                try:
                    bullets.pop(bullets.index(buull))
                except ValueError:
                    q = 1
                princeBoss.hp -= 1
                if princeBoss.hp == 150:
                    princeBoss.pos = 3
                    pygame.mixer.music.load("pyg/Mus_race.oga")
                    pygame.mixer.music.play(-1)
                if princeBoss.hp == 10:
                    princeBoss.pos = 4
                if princeBoss.hp == 0:
                    princeBoss.pos = -1
            if pygame.Rect.colliderect(pygame.Rect(windyBoss.hitbox), pygame.Rect(buull.hitbox)):
                try:
                    bullets.pop(bullets.index(buull))
                except ValueError:
                    q = 1
                windyBoss.hp -= 1
                if windyBoss.hp == 45:
                    windyBoss.pos = 3
                    enemy.x = -15000
                if windyBoss.hp <= 0:
                    windyBoss.pos = -1
            if pygame.Rect.colliderect(pygame.Rect(kingBoss.hitbox), pygame.Rect(buull.hitbox)):
                try:
                    bullets.pop(bullets.index(buull))
                except ValueError:
                    q = 1
                kingBoss.hp -= 1
                if kingBoss.hp == 350:
                    kingBoss.pos = 3
                if kingBoss.hp == 200:
                    kingBoss.pos = 4
                if kingBoss.hp <= 0:
                    kingBoss.pos = -1
            if pygame.Rect.colliderect(pygame.Rect(buull.hitbox), pygame.Rect(bhitbox)):
                try:
                    bullets.pop(bullets.index(buull))
                except ValueError:
                    q = 1
                if bhp > 0:
                    bhp -= 1
                if bhp == 75:
                    bx = 1005
            if room == 2 and pygame.Rect.colliderect(pygame.Rect(buull.hitbox), pygame.Rect(birdie.hitbox)):
                try:
                    bullets.pop(bullets.index(buull))
                except ValueError:
                    q = 1
                if gg and room == 2:
                    birdie.tr = 2
                    d = 15
                    updater()
                    birdie.x = -1000
                    bbx = -1005
                    enemy.x = -5000
                    pygame.time.wait(2000)
                    screen.fill((0, 0, 0), (0, 0, 1000, 750))
                    pygame.display.update()
                    laugher.play()
                    for qqx in range(19):
                        for i in range(100):
                            screen.blit(la[i // 20], (250, 125))
                            pygame.display.update()
                    boss = True
                    flyingBoss.x = -500
                    flyingBoss.pos = 0
                    pygame.mixer.music.load("pyg/Mus_boss1.oga")
                    pygame.mixer.music.play(-1)
                if birdie.tr <= 1:
                    d = 10
                rt = 0
                birdie.tr += 1
        #_ delete out of map bullet
        else:
            try:
                bullets.pop(bullets.index(buull))
            except ValueError:
                q = 1

    #_ rt thing I forgot about
    if rt != -1:
        rt += 1
    if rt == 1000:
        d = 0

    #_ golden bullet getting
    if pygame.Rect.colliderect(pygame.Rect(lhitbox), pygame.Rect(spid.hitbox)):
        d = 12
        updater()
        pygame.time.wait(1000)
        gg = True
        lhitbox = (-40, -40, 40, 40)
        d -= 12

    #_ web getting
    if pygame.Rect.colliderect(pygame.Rect(whitbox), pygame.Rect(spid.hitbox)):
        d = 46
        updater()
        pygame.time.wait(1000)
        web = True
        whitbox = (-70, -70, 40, 40)
        d -= 46

    #_ hitbox collision
    if touchable and pygame.Rect.colliderect(pygame.Rect(spid.hitbox), pygame.Rect(enemy.hitbox)):
        d = -1
        dd.play()
        pygame.time.wait(500)
        conv.play()
        updater()
        pygame.time.wait(5000)
        sys.exit()

    if touchable and room == 4 and pygame.Rect.colliderect(pygame.Rect(spid.hitbox), pygame.Rect(enemy2.hitbox)):
        d = -1
        dd.play()
        pygame.time.wait(500)
        conv.play()
        updater()
        pygame.time.wait(5000)
        sys.exit()

    if touchable and pygame.Rect.colliderect(pygame.Rect(spid.hitbox), pygame.Rect(bhitbox)):
        sys.exit()

    if touchable and pygame.Rect.colliderect(pygame.Rect(spid.hitbox), pygame.Rect(birdie.hitbox)):
        d = -1
        dd.play()
        pygame.time.wait(500)
        conv.play()
        updater()
        pygame.time.wait(5000)
        sys.exit()

    #_ enemy move
    if d == 5 or flyingBoss.pos == 0 or boss_2 or boss_3 or rr == 5 or rr == 2:
        enemy.dir = 0
        enemy.x = -1000
    elif kingBoss.pos == 2 or kingBoss.pos == 3:
        enemy.dir = 0
        enemy.x = -1000
    elif enemy.x >= enemy.path[1]:
        enemy.dir = 1
    elif enemy.x <= enemy.path[0]:
        enemy.dir = -1
    enemy.x += enemy.dir * enemy.vel * (-1)

    #_ enemy 2 move
    if room < 4 or boss_3 or rr == 5 or rr == 2 or kingBoss.pos == 2 or kingBoss.pos == 3:
        enemy2.dir = 0
        enemy2.x = -1000
    elif enemy2.x >= enemy2.path[1]:
        enemy2.dir = 1
    elif enemy2.x <= enemy2.path[0]:
        enemy2.dir = -1
    enemy2.x += enemy2.dir * enemy2.vel * (-1)

    #_ bird enemy move
    if room != 2:
        birdie.dir = 0
        birdie.x = -1000
    elif boss:
        birdie.dir = 0
    elif birdie.x >= birdie.path[1]:
        birdie.dir = 1
        bird_pic = pygame.image.load("pyg/bird2.png")
    elif birdie.x <= birdie.path[0]:
        birdie.dir = -1
        bird_pic = pygame.image.load("pyg/bird.png")
    birdie.x += birdie.dir * birdie.vel * (-1)

    #_ wind move
    if room == 3:
        wind_ran = randint(0, 1000)
        if wind_ran >= 997:
            wind_start = 1
        if wind_start == 1:
            if wind_dir == 1:
                wind_x -= wind_vel*3
                if spid.x - 3 >= 0:
                    spid.x -= 3
                if enemy.x - 3 >= 0:
                    enemy.x -= 3
                if wind_x <= -200:
                    wind_dir = 2
                    wind_start = 0
            elif wind_dir == 2:
                wind_x += wind_vel*3
                if enemy.x + 3 <= 900:
                    spid.x += 3
                    if spid.x >= 940:
                        spid.x = 940
                if enemy.x + 3 <= 1000 - enemy.wid:
                    enemy.x += 3
                if wind_x >= 1000:
                    wind_dir = 1
                    wind_start = 0

    #_ room type
    if room == 5 and rr != 5 and spid.x == 1000 - spid.width:
        spid.x = 0
        type_ran = randint(0, 100)
        solved = False
        if type_ran <= 24:
            rr = 1
            bg = pygame.image.load("pyg/bg-5-1.png")
        elif type_ran <= 49:
            rr = 2
            bg = pygame.image.load("pyg/bg-5-2.png")
        elif type_ran <= 74:
            rr = 3
            bg = pygame.image.load("pyg/bg-5-3.png")
        elif type_ran <= 99:
            rr = 4
            bg = pygame.image.load("pyg/bg-5-4.png")
        elif type_ran == 100:
            rr = 5
            bg = pygame.image.load("pyg/bg-5-5.png")
            pygame.mixer.music.load("pyg/Mus_x_undyne_pre.oga")
            pygame.mixer.music.play(-1)
        if justS:
            enemy.y = 565
            enemy.x = 1000
            enemy2.y = 565
            enemy2.x = 950
            justS = False
    elif room == 5 and rr == 5 and spid.x == 1000 - spid.width:
        spid.x = 0
        rr = 6
        enemy.x = -5000
        enemy2.x = -5000
        bg = pygame.image.load("pyg/bg-5-boss.png")
        kingBoss.x = 700
        kingBoss.pos = 2
        d = 100
        boss_4 = True
        updater()
        pygame.time.wait(3000)
        d += 1
        updater()
        pygame.time.wait(3000)
        d += 1
        updater()
        pygame.time.wait(3000)
        d += 1
        updater()
        pygame.time.wait(3000)
        d += 1
        updater()
        pygame.time.wait(3000)
        d += 1
        updater()
        pygame.time.wait(3000)
        d += 1
        updater()
        pygame.time.wait(3000)
        d = 0
        pygame.mixer.music.load("pyg/Mus_vsasgore.oga")
        pygame.mixer.music.play(-1)
    if rr == 2 and not solved:
        maze_hitbox = (750, 540, 100, 100)
        if pygame.Rect.colliderect(pygame.Rect(spid.hitbox), pygame.Rect(maze_hitbox)):
            maze = True
        enemy.x = -1000
        enemy2.x = -1000
    if maze and rr == 2:
        snake_block = 15
        snake_speed = 15
        snake = []
        score = 0
        game_over = False
        xsh = 500
        ysh = 375
        xs_change = 0
        ys_change = 0
        foodx = round(random.randrange(0, 1000 - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, 750 - snake_block) / 10.0) * 10.0
        pygame.mixer.music.load("pyg/Mus_wrongworld.oga")
        pygame.mixer.music.play(-1)
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        xs_change = -snake_block
                        ys_change = 0
                    elif event.key == pygame.K_RIGHT:
                        xs_change = snake_block
                        ys_change = 0
                    elif event.key == pygame.K_UP:
                        ys_change = -snake_block
                        xs_change = 0
                    elif event.key == pygame.K_DOWN:
                        ys_change = snake_block
                        xs_change = 0
            if xsh >= 1000 or xsh < 0 or ysh >= 750 or ysh < 0:
                game_over = True
                maze = False
                spid.x = 0
            if score >= 10:
                justS = True
                solved = True
                maze = False
                game_over = True
            xsh += xs_change
            ysh += ys_change
            snake_Head = [xsh, ysh]
            snake.append(snake_Head)
            if len(snake) > score + 1:
                del snake[0]
            for x in snake[:-1]:
                if x == snake_Head:
                    game_over = True
                    maze = False
                    spid.x = 0
            foodhitbox = pygame.Rect(foodx, foody, snake_block, snake_block)
            if pygame.Rect.colliderect(foodhitbox, pygame.Rect(xsh, ysh, snake_block, snake_block)):
                foodx = round(random.randrange(0, 1000 - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, 750 - snake_block) / 10.0) * 10.0
                score += 1
            clock.tick(snake_speed)
            updater()
    if rr == 3 and not solved:
        maze_hitbox = (750, 540, 100, 100)
        if pygame.Rect.colliderect(pygame.Rect(spid.hitbox), pygame.Rect(maze_hitbox)):
            maze = True
        enemy.x = -1000
        enemy2.x = -1000
    if maze and rr == 3:
        block = 50
        speed = 15
        field = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 2, 3, 0, 1, 1, 2, 0, 0, 3, 3, 1, 0, 1, 1, 2, 3, 0, 1],
            [1, 1, 0, 0, 1, 1, 0, 3, 1, 2, 3, 0, 1, 1, 1, 0, 2, 3, 0, 1],
            [1, 0, 1, 2, 3, 3, 0, 1, 1, 0, 3, 1, 0, 0, 0, 0, 1, 3, 2, 1],
            [1, 1, 0, 0, 1, 2, 3, 1, 0, 2, 1, 1, 1, 0, 0, 1, 2, 3, 1, 1],
            [1, 0, 1, 3, 2, 0, 1, 1, 2, 3, 0, 1, 2, 3, 2, 1, 1, 0, 2, 1],
            [1, 1, 0, 2, 0, 1, 1, 0, 3, 3, 2, 0, 3, 0, 0, 0, 1, 2, 0, 1],
            [1, 0, 0, 3, 1, 0, 0, 2, 3, 2, 0, 1, 1, 1, 0, 2, 1, 1, 1, 1],
            [1, 1, 3, 0, 2, 2, 3, 0, 3, 1, 0, 1, 1, 1, 1, 3, 1, 0, 2, 1],
            [1, 0, 1, 1, 1, 3, 1, 1, 1, 0, 0, 0, 3, 3, 2, 0, 0, 1, 3, 1],
            [1, 0, 1, 0, 2, 3, 0, 3, 1, 1, 1, 1, 1, 1, 3, 1, 0, 2, 3, 1],
            [1, 1, 1, 0, 1, 3, 2, 3, 0, 0, 2, 2, 2, 0, 2, 3, 0, 1, 3, 1],
            [1, 0, 1, 2, 0, 0, 1, 1, 1, 1, 3, 3, 3, 1, 3, 1, 1, 2, 3, 1],
            [1, 0, 1, 1, 1, 3, 2, 0, 0, 0, 0, 2, 0, 3, 3, 0, 0, 0, 2, 4],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        game_over = False
        xp = block
        yp = block
        smell = 0
        xs_change = 0
        ys_change = 0
        change = False
        pygame.mixer.music.load("pyg/Mus_wrongworld.oga")
        pygame.mixer.music.play(-1)
        while not game_over:
            for i in range(15):
                for j in range(20):
                    col = (0, 0, 0)
                    if field[i][j] == 1:
                        col = (255, 0, 0)
                    if field[i][j] == 2:
                        col = (255, 155, 66)
                    if field[i][j] == 3:
                        col = (0, 0, 255)
                    if field[i][j] == 0:
                        col = (255, 166, 158)
                    pygame.draw.rect(screen, col, (j*block, i*block, block, block))
            pygame.draw.rect(screen, (255, 255, 255), (xp, yp, block - 2, block - 2))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        xs_change = -block
                        ys_change = 0
                        change = True
                    elif event.key == pygame.K_RIGHT:
                        xs_change = block
                        ys_change = 0
                        change = True
                    elif event.key == pygame.K_UP:
                        ys_change = -block
                        xs_change = 0
                        change = True
                    elif event.key == pygame.K_DOWN:
                        ys_change = block
                        xs_change = 0
                        change = True
            if change:
                xp += xs_change
                yp += ys_change
                change = False
            if field[yp//block][xp//block] == 1:
                spid.x = 0
                maze = False
                game_over = True
            if field[yp//block][xp//block] == 0:
                smell = 0
            if field[yp//block][xp//block] == 2:
                smell = 1
            if field[yp//block][xp//block] == 3 and smell == 1:
                spid.x = 0
                maze = False
                game_over = True
            if field[yp//block][xp//block] == 4:
                justS = True
                solved = True
                maze = False
                game_over = True
            clock.tick(speed)

    #_ boss room 1
    if d == 5:
        bhitbox = (bx, -200, 1000, 1000)
        bx += 1
    if d == 5 and bhp <= 75:
        bhitbox = (bx, -200, 1000, 1000)
        bx -= 2
    if d != 5:
        bhitbox = (-1100, -1100, 1000, 1000)

    #_ boss room 2
    if boss and room == 2:
        if flyingBoss.pos == 0:
            if flyingBoss.x + flyingBoss.vel <= -200:
                flyingBoss.x += flyingBoss.vel
            if fire:
                fy += 8
            elif not fire:
                ran = random.randint(1, 900)
                fy = 0
            atack(ran, fy, pygame.image.load("pyg/fireball.png"))
        elif flyingBoss.pos == 2:
            if flyingBoss.x - flyingBoss.vel >= 800:
                flyingBoss.x -= flyingBoss.vel
        elif flyingBoss.pos >= 3:
            if fire:
                fy += 8
            elif not fire:
                ran = random.randint(1, 900)
                fy = 0
            atack(ran, fy, pygame.image.load("pyg/fireball.png"))
            if flyingBoss.pos == 4 and flyingBoss.x == 1000:
                flyingBoss.x = -500
            if 0 <= flyingBoss.x <= 1000 and flyingBoss.pos == 4:
                flyingBoss.x += flyingBoss.vel
            if flyingBoss.x + flyingBoss.vel <= -200 and 0 > flyingBoss.x and flyingBoss.pos == 4:
                flyingBoss.x += flyingBoss.vel
            if -200 <= flyingBoss.x <= 1000 and flyingBoss.pos == 5:
                flyingBoss.x += flyingBoss.vel + 8
            if flyingBoss.x >= 1000 and flyingBoss.pos == 5:
                flyingBoss.pict = pygame.image.load("pyg/boss-2.png")
                flyingBoss.pos = 6
            if flyingBoss.x >= 800 and flyingBoss.pos == 6:
                flyingBoss.x -= flyingBoss.vel
            if flyingBoss.x >= -500 and flyingBoss.pos == 7:
                flyingBoss.x -= flyingBoss.vel + 2
            if flyingBoss.x <= -500:
                flyingBoss.pos = 8
                flyingBoss.pict = pygame.image.load("pyg/boss-2-2.png")
            if flyingBoss.x <= 1000 and flyingBoss.pos == 8:
                flyingBoss.x += flyingBoss.vel + 2
            if flyingBoss.x >= 1000 and flyingBoss.pos == 8:
                flyingBoss.pos = 7
                flyingBoss.pict = pygame.image.load("pyg/boss-2.png")
        elif flyingBoss.pos == -1:
            flyingBoss.pos = -2
            flyingBoss.x = -1000
            flyingBoss.y = -1000
            room = 3
            d = 20
            updater()
            pygame.time.wait(2000)
            d += 1
            pygame.mixer.music.load("pyg/Mus_amalgam.oga")
            pygame.mixer.music.play(-1)
            updater()
            pygame.time.wait(10000)
            d += 1
            pygame.mixer.music.load("pyg/Mus_options_fall.oga")
            pygame.mixer.music.play(-1)

        if touchable and pygame.Rect.colliderect(pygame.Rect(flyingBoss.hitbox), pygame.Rect(spid.hitbox)):
            d = -1
            dd.play()
            updater()
            pygame.time.wait(5000)
            sys.exit()

    #_ boss room 3
    if boss_2 and room == 3:
        if windyBoss.pos == 2:
            if windyBoss.x + windyBoss.vel <= -200:
                windyBoss.x += windyBoss.vel
            if not zap:
                zap_ran = random.randint(1, 900)
                zap = True
            zaptack(zap_ran, 20)
            if touchable and pygame.Rect.colliderect(pygame.Rect(zap_hitbox), pygame.Rect(spid.hitbox)):
                d = -1
                dd.play()
                updater()
                if zap_i == 1:
                    screen.blit(lig1, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i % 2 == 0:
                    screen.blit(lig_em, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 3:
                    screen.blit(lig2, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 5:
                    screen.blit(lig3, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 7:
                    screen.blit(lig4, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 9:
                    screen.blit(lig5, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 11:
                    screen.blit(lig6, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 13:
                    screen.blit(lig7, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 15:
                    screen.blit(lig8, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 17:
                    screen.blit(lig9, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 19:
                    screen.blit(lig10, (zap_ran, 20))
                    pygame.display.update()
                pygame.time.wait(5000)
                sys.exit()
        elif windyBoss.pos == 3:
            windyBoss.x += windyBoss.vel*2
        elif windyBoss.pos == -1:
            windyBoss.x = -1000
            windyBoss.y = -1000
            if s == 0:
                pygame.mixer.music.load("pyg/wind_boss.mp3")
                pygame.mixer.music.play(-1)
            s += 1
            if s >= 100:
                catscene()
            if spid.x < -75 or spid.y < -75:
                d = 40
                pygame.mixer.music.load("pyg/Mus_amalgam.oga")
                pygame.mixer.music.play(-1)
                updater()
                pygame.time.wait(10000)
                d += 1
                pygame.mixer.music.load("pyg/Mus_options_fall.oga")
                pygame.mixer.music.play(-1)
                boss_3 = False
                room = 4
        if touchable and pygame.Rect.colliderect(pygame.Rect(windyBoss.hitbox), pygame.Rect(spid.hitbox)):
            d = -1
            dd.play()
            updater()
            pygame.time.wait(5000)
            sys.exit()

    #_ boss room 5
    if boss_4 and room == 5 and rr == 6:
        if kingBoss.pos == 2:
            if fire:
                fy += 8
            elif not fire:
                ran = random.randint(1, 900)
                fy = 0
            atack(ran, fy, pygame.image.load("pyg/fireball.png"))
            if not zap:
                zap_ran = random.randint(1, 900)
                zap = True
            zaptack(zap_ran, 20)
            if touchable and pygame.Rect.colliderect(pygame.Rect(zap_hitbox), pygame.Rect(spid.hitbox)):
                d = -1
                dd.play()
                updater()
                if zap_i == 1:
                    screen.blit(lig1, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i % 2 == 0:
                    screen.blit(lig_em, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 3:
                    screen.blit(lig2, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 5:
                    screen.blit(lig3, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 7:
                    screen.blit(lig4, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 9:
                    screen.blit(lig5, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 11:
                    screen.blit(lig6, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 13:
                    screen.blit(lig7, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 15:
                    screen.blit(lig8, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 17:
                    screen.blit(lig9, (zap_ran, 20))
                    pygame.display.update()
                elif zap_i == 19:
                    screen.blit(lig10, (zap_ran, 20))
                    pygame.display.update()
                pygame.time.wait(5000)
                sys.exit()
        elif kingBoss.pos == 3:
            if touchable and pygame.Rect.colliderect(pygame.Rect(spid.hitbox), pygame.Rect((tx, ty, 500, 200))):
                d = -1
                dd.play()
                updater()
                pygame.time.wait(5000)
                sys.exit()
            if tdone:
                tran = randint(1, 3)
                tdone = False
                tx = 1000
            elif not tdone and tran == 1:
                tx -= 10
                ty = 50
                if tx <= -500:
                    tttime -= 1
                    if tttime < 0:
                        tdone = True
                        tttime = 300
            elif not tdone and tran == 2:
                tx -= 10
                ty = 250
                if tx <= -500:
                    tttime -= 1
                    if tttime < 0:
                        tdone = True
                        tttime = 300
            elif not tdone and tran == 3:
                tx -= 10
                ty = 450
                if tx <= -500:
                    tttime -= 1
                    if tttime < 0:
                        tdone = True
                        tttime = 300
        elif kingBoss.pos == 4:
            if fire:
                fy += 8
            elif not fire:
                ran = random.randint(1, 900)
                fy = 0
            atack(ran, fy, pygame.image.load("pyg/fireball.png"))
            ty = -1000
        elif kingBoss.pos == -1:
            kingBoss.x = -1000
            kingBoss.y = -1000
            room = 5
            d = 150
            boss_4 = False
            updater()
            pygame.time.wait(2000)
            d += 1
            final()
            pygame.mixer.music.load("pyg/Mus_options_fall.oga")
            pygame.mixer.music.play(-1)

        if touchable and pygame.Rect.colliderect(pygame.Rect(kingBoss.hitbox), pygame.Rect(spid.hitbox)):
            d = -1
            dd.play()
            updater()
            pygame.time.wait(5000)
            sys.exit()

    #_ boss room 4
    if boss_3 and room == 4:
        if princeBoss.pos == 2:
            if princeBoss.x + princeBoss.vel <= -200:
                princeBoss.x += princeBoss.vel
            if fire:
                fy += 10
            elif not fire:
                ran = random.randint(1, 900)
                fy = 0
            atack(ran, fy, pygame.image.load("pyg/rock.png"))
        elif princeBoss.pos == 3:
            if touchable and pygame.Rect.colliderect(pygame.Rect(spid.hitbox), pygame.Rect((100, ly, lw, 300))):
                d = -1
                dd.play()
                updater()
                pygame.time.wait(5000)
                sys.exit()
            if ldone:
                lran = randint(1, 2)
                ldone = False
                lw = 0
                ltime = 500
            elif not ldone and lran == 1:
                if princeBoss.y - 5 > 0:
                    princeBoss.y -= 5
                elif ltime > 0:
                    ltime -= 1
                else:
                    lw += 50
                    ly = 50
                    if lw >= 1000:
                        if lw >= 1000:
                            lltime -= 1
                            if lltime < 0:
                                ldone = True
                                lltime = 500
            elif not ldone and lran == 2:
                if princeBoss.y + 5 < 250:
                    princeBoss.y += 5
                elif ltime > 0:
                    ltime -= 1
                else:
                    lw += 300
                    ly = 300
                    if lw >= 1000:
                        lltime -= 1
                        if lltime < 0:
                            ldone = True
                            lltime = 500
        elif princeBoss.pos == 4:
            lw = 0
            princeBoss.y = 0
            if lt:
                wx = -400
                lt = False
            wx += 10
            if touchable and pygame.Rect.colliderect(pygame.Rect(spid.hitbox), pygame.Rect((wx, 250, 350, 400))):
                d = -1
                dd.play()
                updater()
                pygame.time.wait(5000)
                sys.exit()
        elif princeBoss.pos == -1:
            wx = 1000
            princeBoss.x = -1000
            princeBoss.y = -1000
            room = 5
            d = 60
            updater()
            pygame.time.wait(2000)
            d += 1
            pygame.mixer.music.load("pyg/Mus_amalgam.oga")
            pygame.mixer.music.play(-1)
            updater()
            pygame.time.wait(10000)
            d += 1
            pygame.mixer.music.load("pyg/Mus_options_fall.oga")
            pygame.mixer.music.play(-1)

        if touchable and pygame.Rect.colliderect(pygame.Rect(princeBoss.hitbox), pygame.Rect(spid.hitbox)):
            d = -1
            dd.play()
            updater()
            pygame.time.wait(5000)
            sys.exit()

    #_ keyboard check
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DELETE]:
        touchable = False

    if keys[pygame.K_z]:
        frag += 1
        spid.score += 9

    if keys[pygame.K_RIGHT] and spid.x + spid.vel <= 1000 - 60 and not maze:
        spid.x += spid.vel
        spid.right = True
        spid.left = False
        spid.last = 0
    elif keys[pygame.K_LEFT] and spid.x - spid.vel >= 0 and not isWeb and not maze:
        spid.x -= spid.vel
        spid.right = False
        spid.left = True
        spid.last = 1
    else:
        if spid.left:
            spid.last = 1
        elif spid.right:
            spid.last = 0
        spid.left = False
        spid.right = False
        spid.walkC = 0

    if keys[pygame.K_SPACE] and not maze:
        facing = 1
        if spid.last == 1:
            facing = -1
        if len(bullets) < 7:
            bs.play()
            bullets.append(
                Bullet(round(spid.x + spid.width // 2), round(spid.y + spid.height // 2), 5, facing))

    if not spid.isjump and not isWeb and not maze:
        if keys[pygame.K_UP]:
            spid.isjump = True
    elif spid.isjump and not maze:
        if spid.jumpcount >= -mjp:
            neg = 1
            if spid.jumpcount < 0:
                neg = -1
            spid.y -= (spid.jumpcount ** 2) * 0.5 * neg
            spid.jumpcount -= 1
        else:
            spid.isjump = False
            spid.jumpcount = mjp
    awebtime -= 5
    if not isWeb and web and awebtime <= 0 and not maze:
        awebtime = 0
        if keys[pygame.K_x]:
            isWeb = True
    elif isWeb and web and not maze:
        awebtime = 0
        if webc >= 0:
            spid.y -= (webc ** 2) * 0.25
            webc -= 1
            webtime = 1000
            pygame.draw.rect(screen, (255, 255, 255), (spid.x + spid.width // 2 - 1, 0, 2, spid.y))
            pygame.display.update()
        else:
            pygame.draw.rect(screen, (255, 255, 255), (spid.x + spid.width // 2 - 1, 0, 2, spid.y))
            pygame.display.update()
            webtime -= 2
            if webtime <= 0:
                if webc >= -mwb:
                    spid.y += (webc ** 2) * 0.25
                    webc -= 1
                else:
                    isWeb = False
                    webc = mwb
                    awebtime = 5000

    #_ update display
    updater()
