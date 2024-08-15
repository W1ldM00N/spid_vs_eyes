import pygame
import sys
from random import randint

pygame.init()

enemy_images = {
    "eye": [pygame.image.load("pyg/enemy_eye_1.png"), pygame.image.load("pyg/enemy_eye_2.png")],
    "darklet": [pygame.image.load("pyg/boss-1-1.png"), pygame.image.load("pyg/boss-1-2.png"),
                pygame.image.load("pyg/boss-1-3.png"), pygame.image.load("pyg/boss-1-4.png")],
    "flyer": [pygame.image.load("pyg/enemy_fly_1.png"), pygame.image.load("pyg/enemy_fly_2.png")],
    "induk": [pygame.image.load("pyg/boss-2-1.png"), pygame.image.load("pyg/boss-2-2.png")],
    "godzilla": [pygame.image.load("pyg/boss-3-1.png"), pygame.image.load("pyg/boss-3-2.png")],
    "catagents": [pygame.image.load("pyg/boss-4-1.png")],
    "jayawardenepuraKotte": [pygame.image.load("pyg/final_boss.png")]
}
enemy_damages = {
    "eye": 0.5,
    "darklet": 2.5,
    "flyer": 1,
    "induk": 4,
    "godzilla": 6,
    "catagents": 8,
    "jayawardenepuraKotte": 12
}

enemy_attacks = {
    "eye": {
        1: pygame.image.load("pyg/eye_attack.png"),
        2: pygame.image.load("pyg/eye_attack_2.png")
    },
    "darklet": {
        1: pygame.image.load("pyg/boss-1-attack-1.png"),
        2: pygame.image.load("pyg/boss-1-attack-2.png")
    },
    "flyer": {
        1: pygame.image.load("pyg/eye_attack.png"),
        2: pygame.image.load("pyg/eye_attack_2.png")
    },
    "induk": {
        1: pygame.image.load("pyg/boss-2-attack-1.png"),
        2: pygame.image.load("pyg/boss-2-attack-2.png"),
        3: pygame.image.load("pyg/boss-2-attack-3.png")
    },
    "godzilla": {
        1: pygame.image.load("pyg/boss-3-attack-2.png"),
        2: pygame.image.load("pyg/boss-3-attack-3.png")
    },
    "catagents": {
        1: pygame.image.load("pyg/boss-4-attack.png"),
        2: pygame.image.load("pyg/boss-4-attack-2.png"),
        3: pygame.image.load("pyg/boss4-attack-3.png"),
        4: pygame.image.load("pyg/boss-4-attack-4.png")
    },
    "jayawardenepuraKotte": {
        1: pygame.image.load("pyg/final boss1-attack.png"),
        2: pygame.image.load("pyg/final boss1 attack 2.png"),
        3: pygame.image.load("pyg/final boss1 attack3.png"),
    }
}

attack_style = {
    "eye": "fall",
    "darklet": "fall",
    "flyer": "fall",
    "induk": "fall",
    "godzilla": "move",
    "catagents": "fall",
    "jayawardenepuraKotte": "move"
}


class Enemy:
    def __init__(self, name, player, max_hp, frame_speed, speed, eee, min_exp, max_exp):
        self.max_exp = max_exp
        self.min_exp = min_exp

        self.screen = pygame.display.get_surface()
        self.frame = 0
        self.frame_speed = frame_speed
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.clock = pygame.time.Clock()

        self.name = name
        self.images = enemy_images[name]
        self.hp = max_hp
        self.max_hp = max_hp
        self.damage = enemy_damages[name]
        self.attacks = enemy_attacks[name]
        self.style = attack_style[name]

        self.player = player
        self.hp_bar = pygame.Rect(20, 15, 100, 15)
        self.energy_bar = pygame.Rect(20, 35, 100, 15)

        self.player_image = pygame.image.load("pyg/player_fight.png")
        self.player_rect = self.player_image.get_rect(topleft=(462.5, 605))
        self.player_dir = pygame.math.Vector2()

        self.vel = self.player.fight_vel
        self.at_speed = speed

        self.turn = 1
        self.attack_button = pygame.image.load("pyg/attack_button.png")
        self.heal_button = pygame.image.load("pyg/heal_button.png")
        self.attack_rect = self.attack_button.get_rect(topleft=(195, 550))
        self.heal_rect = self.heal_button.get_rect(topleft=(605, 550))

        self.at = False
        self.at_frame = 0
        self.at_img = [pygame.image.load("pyg/hit_1.png"), pygame.image.load("pyg/hit_2.png"),
                       pygame.image.load("pyg/hit_3.png"), pygame.image.load("pyg/hit_4.png"),
                       pygame.image.load("pyg/hit_5.png")]
        self.choosing = True
        self.ran = 1
        self.at_y = 400
        self.at_x = randint(145, 855)
        self.at_2_x = randint(145, 855)
        self.loop = 0
        self.hp_ebar = pygame.Rect(250, 15, 500, 30)

        self.run = True

        self.dead_time = 0
        self.wait = 480
        self.exp_plus = 0
        self.eee = eee

    def fight(self):
        while self.run:
            keys = pygame.key.get_pressed()
            if self.turn != 0:
                if keys[pygame.K_UP] and self.player_rect.y + self.vel > 525:
                    self.player_dir.y = -1
                elif keys[pygame.K_DOWN] and self.player_rect.y - self.vel < 625:
                    self.player_dir.y = 1
                else:
                    self.player_dir.y = 0
                if keys[pygame.K_LEFT] and self.player_rect.x - self.vel > 145:
                    self.player_dir.x = -1
                elif keys[pygame.K_RIGHT] and self.player_rect.x + self.vel < 805:
                    self.player_dir.x = 1
                else:
                    self.player_dir.x = 0

            self.screen.fill((0, 0, 0))

            pygame.draw.rect(self.screen, "red", self.hp_bar)
            curr_hp_width = 100 * self.player.hp / self.player.stats["hp"]
            curr_hp_bar = pygame.Rect(20, 15, curr_hp_width, 15)
            pygame.draw.rect(self.screen, "green", curr_hp_bar)

            pygame.draw.rect(self.screen, "#222222", self.energy_bar)
            curr_energy_width = 100 * self.player.energy / self.player.stats["energy"]
            curr_energy_bar = pygame.Rect(20, 35, curr_energy_width, 15)
            pygame.draw.rect(self.screen, "light blue", curr_energy_bar)

            kill_count = self.font.render("Exp: " + str(self.player.exp), False, "white")
            self.screen.blit(kill_count, (20, 50))

            love = self.font.render("LV: " + str(self.player.love), False, "white")
            self.screen.blit(love, (20, 85))

            if self.turn != 0:
                self.screen.blit(self.images[int(self.frame)], (250, -50))
                self.frame += self.frame_speed
                if self.frame >= len(self.images) - self.eee:
                    self.frame = 0

            pygame.draw.rect(self.screen, "white", (125, 500, 750, 200))
            pygame.draw.rect(self.screen, "black", (145, 520, 710, 160))

            if self.turn == 1 and not self.at:
                self.screen.blit(self.attack_button, (195, 550))
                self.screen.blit(self.heal_button, (605, 550))
                if self.player_rect.colliderect(self.heal_rect) and keys[pygame.K_z] and self.player.energy >= 5:
                    self.player.energy -= 5
                    self.player.hp += self.player.heal
                    if self.player.hp > self.player.stats["hp"]:
                        self.player.hp = self.player.stats["hp"]
                    self.turn = 2
                elif self.player_rect.colliderect(self.attack_rect) and keys[pygame.K_z] and not self.at:
                    self.hp -= (self.player.max_damage - randint(0, 5))
                    self.at = True
                    if self.hp <= 0:
                        self.dead_time = pygame.time.get_ticks()
                        self.exp_plus = randint(self.min_exp, self.max_exp)
                        self.player.exp += self.exp_plus

            if self.at:
                self.screen.blit(self.at_img[int(self.at_frame)], (400, 125))
                self.at_frame += 0.01 * 50
                if self.at_frame >= len(self.at_img):
                    self.at_frame = 0
                    self.at = False
                    self.turn = 2

            if self.hp <= 0:
                self.turn = 0
                kill_count = self.font.render("Congarts!", False, "white")
                self.screen.blit(kill_count, (505, 550))
                kill_count = self.font.render("You got " + str(self.exp_plus) + " exp!", False, "white")
                self.screen.blit(kill_count, (505, 580))
                curr_time = pygame.time.get_ticks()
                if curr_time - self.dead_time >= self.wait:
                    self.run = False

            if self.player.hp <= 0:
                self.turn = 0
                kill_count = self.font.render("Congarts!", False, "white")
                self.screen.blit(kill_count, (505, 550))
                kill_count = self.font.render("You got DIED!", False, "white")
                self.screen.blit(kill_count, (505, 580))
                curr_time = pygame.time.get_ticks()
                if curr_time - self.dead_time >= self.wait:
                    sys.exit()

            pygame.draw.rect(self.screen, "#222222", self.hp_ebar)
            curr_hp_width = 500 * self.hp / self.max_hp
            curr_hp_bar = pygame.Rect(250, 15, curr_hp_width, 30)
            pygame.draw.rect(self.screen, "red", curr_hp_bar)

            if self.turn == 2 and not self.choosing:
                self.ran = randint(1, len(self.attacks))
                if self.style == "fall":
                    self.at_y = 400
                    self.at_x = randint(145, 855)
                    self.at_2_x = randint(145, 855)
                elif self.style == "move":
                    qwe = randint(1, 2)
                    if qwe == 1:
                        self.at_y = 520
                    elif qwe == 2:
                        self.at_y = 580
                    self.at_x = 0
                    self.at_2_x = -250
                self.choosing = True

            if self.turn == 2 and self.style == "fall":
                img = (self.attacks[self.ran])
                self.screen.blit(img, (self.at_x, self.at_y))
                self.screen.blit(img, (self.at_2_x, self.at_y))
                self.at_y += self.at_speed
                if self.player_rect.colliderect(img.get_rect(topleft=(self.at_x, self.at_y))):
                    self.player.hp -= self.damage
                    self.turn = 1
                    self.choosing = False
                    self.loop = 0
                    if self.player.hp <= 0:
                        self.dead_time = pygame.time.get_ticks()
                elif self.player_rect.colliderect(img.get_rect(topleft=(self.at_2_x, self.at_y))):
                    self.player.hp -= 0.5
                    self.choosing = False
                    self.loop = 0
                    self.turn = 1
                    if self.player.hp <= 0:
                        self.dead_time = pygame.time.get_ticks()

            if self.turn == 2 and self.at_y >= 750 and self.style == "fall":
                self.choosing = False
                self.loop += 1
                if self.loop == 3:
                    self.loop = 0
                    self.turn = 1

            if self.turn == 2 and self.style == "move":
                img = (self.attacks[self.ran])
                self.screen.blit(img, (self.at_x, self.at_y))
                self.at_x += self.at_speed
                if self.player_rect.colliderect(img.get_rect(topleft=(self.at_x, self.at_y))):
                    self.player.hp -= self.damage
                    self.turn = 1
                    self.choosing = False
                    self.loop = 0
                    if self.player.hp <= 0:
                        self.dead_time = pygame.time.get_ticks()

            if self.turn == 2 and self.at_x >= 1000 and self.style == "move":
                self.choosing = False
                self.loop += 1
                if self.loop == 3:
                    self.loop = 0
                    self.turn = 1

            self.screen.blit(self.player_image, self.player_rect.topleft)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if self.player_dir.magnitude() != 0:
                self.player_dir = self.player_dir.normalize()
            self.player_rect.x += self.player_dir.x * self.vel
            self.player_rect.y += self.player_dir.y * self.vel

            self.clock.tick(60)
