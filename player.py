import pygame
pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, obs):
        super().__init__(group)
        self.image = pygame.image.load("pyg/player_up_2.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-20, -20)
        self.dir = pygame.math.Vector2()
        self.vel = 5
        self.status = "down"
        self.frame = 0
        self.frame_speed = 0.1
        self.obstacles = obs
        self.stats = {
            "hp": 10,
            "energy": 100,
        }
        self.need = 100
        self.hp = self.stats["hp"]
        self.energy = self.stats["energy"]
        self.exp = 0
        self.love = 0
        self.max_damage = 25
        self.heal = 2
        self.fight_vel = 4
        self.animations = {
            "up": [pygame.image.load("pyg/player_down_1.png"), pygame.image.load("pyg/player_down_2.png"),
                   pygame.image.load("pyg/player_down_1.png"), pygame.image.load("pyg/player_down_4.png")],

            "down": [pygame.image.load("pyg/player_up_1.png"), pygame.image.load("pyg/player_up_2.png"),
                     pygame.image.load("pyg/player_up_1.png"), pygame.image.load("pyg/player_up_4.png")],

            "left": [pygame.image.load("pyg/player_left_1.png"), pygame.image.load("pyg/player_left_2.png"),
                     pygame.image.load("pyg/player_left_3.png"), pygame.image.load("pyg/player_left_4.png")],

            "right": [pygame.image.load("pyg/player_right_1.png"), pygame.image.load("pyg/player_right_2.png"),
                      pygame.image.load("pyg/player_right_3.png"), pygame.image.load("pyg/player_right_4.png")],

            "up_idle": [pygame.image.load("pyg/player_down_1.png")],

            "down_idle": [pygame.image.load("pyg/player_up_1.png")],

            "left_idle": [pygame.image.load("pyg/player_left_1.png")],

            "right_idle": [pygame.image.load("pyg/player_right_1.png")],
        }
        self.q = 0
        self.boss = 0

    def get_status(self):
        if self.dir.x == 0 and self.dir.y == 0:
            if "_idle" in self.status:
                self.q = 0
            else:
                self.status = self.status + "_idle"

    def keyPress(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.dir.y = -1
            self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.dir.y = 1
            self.status = "down"
        else:
            self.dir.y = 0
        if keys[pygame.K_LEFT]:
            self.status = "left"
            self.dir.x = -1
        elif keys[pygame.K_RIGHT]:
            self.dir.x = 1
            self.status = "right"
        else:
            self.dir.x = 0

    def posChange(self):
        if self.dir.magnitude() != 0:
            self.dir = self.dir.normalize()
        self.hitbox.x += self.dir.x * self.vel
        self.collide("horizontal")
        self.hitbox.y += self.dir.y * self.vel
        self.collide("vertical")
        self.rect.center = self.hitbox.center

    def collide(self, direction):
        if direction == "horizontal":
            for tile in self.obstacles:
                if tile.hitbox.colliderect(self.hitbox):
                    if self.dir.x > 0:
                        self.hitbox.right = tile.hitbox.left
                    elif self.dir.x < 0:
                        self.hitbox.left = tile.hitbox.right
        if direction == "vertical":
            for tile in self.obstacles:
                if tile.hitbox.colliderect(self.hitbox):
                    if self.dir.y > 0:
                        self.hitbox.bottom = tile.hitbox.top
                    elif self.dir.y < 0:
                        self.hitbox.top = tile.hitbox.bottom

    def animate(self):
        anim = self.animations[self.status]
        self.frame += self.frame_speed
        if self.frame >= len(anim):
            self.frame = 0

        self.image = anim[int(self.frame)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def update(self):
        if self.exp >= self.need:
            self.love += 1
            self.stats["hp"] += 7
            self.stats["energy"] += 5
            self.max_damage += 5
            self.need *= 2.5
            self.hp = self.stats["hp"]
            self.energy = self.stats["energy"]
            self.heal += 2
            self.fight_vel += 0.5
        self.keyPress()
        self.get_status()
        self.animate()
        self.posChange()
