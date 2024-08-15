import pygame
from player import Player
from random import randint
from fight import Enemy

pygame.init()
pygame.mixer.init()

level_map = {
    1: [
        ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
        ["w", " ", " ", "r", "l", " ", " ", "i", "i", "i", "r", " ", " ", " ", " ", "l", " ", " ", "r", "w"],
        ["w", " ", " ", " ", " ", " ", "r", "i", " ", " ", "l", " ", "r", " ", " ", " ", " ", " ", "l", "w"],
        ["w", "r", "r", " ", " ", " ", "l", " ", " ", "r", " ", " ", " ", " ", "r", "r", "r", " ", " ", "w"],
        ["w", " ", "r", " ", "r", "p", " ", " ", " ", " ", "r", " ", " ", " ", "r", "r", " ", " ", "r", "w"],
        ["w", " ", "l", " ", "r", " ", "r", "r", " ", " ", "l", " ", "r", " ", " ", "r", "r", " ", " ", "w"],
        ["w", " ", " ", " ", "r", " ", "r", "i", " ", " ", " ", " ", "r", " ", " ", " ", "r", " ", " ", "w"],
        ["w", "r", " ", " ", "r", " ", "i", "r", " ", " ", " ", " ", "l", " ", " ", "r", "r", " ", "l", "w"],
        ["w", "l", " ", " ", " ", " ", "i", "r", " ", " ", " ", " ", " ", " ", " ", "r", "r", "r", "r", "w"],
        ["w", " ", " ", " ", " ", " ", " ", "i", " ", " ", "l", " ", " ", " ", " ", " ", " ", " ", "r", "w"],
        ["w", " ", " ", " ", " ", " ", " ", "i", " ", " ", "r", " ", " ", " ", " ", " ", " ", " ", " ", "w"],
        ["w", "r", "r", "r", "r", " ", "r", "r", " ", " ", " ", " ", " ", " ", "r", "r", "r", " ", " ", "w"],
        ["w", " ", "l", " ", "r", " ", " ", " ", " ", " ", "l", " ", " ", " ", "r", " ", " ", " ", "l", "w"],
        ["w", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
        ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]
    ],
    2: [
        ["t", "t", "t", "t", "r", "r", "t", "t", "t", "t", "t", "'", "'", "'", "'", "'", "'", "'", "'", "'"],
        ["t", " ", " ", "r", "r", " ", " ", "t", " ", " ", "r", "'", "'", "r", "t", "t", "t", "'", "'", "'"],
        ["t", "r", " ", " ", " ", " ", "r", "r", " ", " ", "r", "l", "t", "t", " ", " ", " ", "t", "'", "'"],
        ["t", "r", "r", " ", " ", " ", "l", " ", " ", "r", " ", " ", " ", " ", " ", "r", " ", "r", "t", "t"],
        ["t", " ", "r", " ", " ", " ", "t", " ", " ", "t", "r", " ", " ", " ", "r", "r", " ", " ", "r", "t"],
        ["t", " ", "l", " ", "t", " ", "t", "r", " ", "t", "l", " ", "r", "t", "t", "r", "r", " ", " ", "t"],
        ["x", " ", " ", " ", "t", " ", "t", "t", " ", "t", " ", " ", "r", " ", "l", "t", "t", " ", " ", "t"],
        ["r", "r", "r", "r", "t", " ", "t", "r", " ", "t", " ", " ", "l", " ", " ", " ", "r", " ", "l", "r"],
        ["t", "l", " ", "t", " ", " ", "t", " ", " ", " ", " ", " ", "r", " ", " ", "r", "r", " ", "r", "r"],
        ["t", " ", " ", " ", " ", " ", " ", " ", " ", " ", "l", "t", "t", " ", " ", " ", " ", " ", "r", "t"],
        ["t", "t", " ", " ", "r", "r", " ", " ", " ", " ", "r", " ", " ", "t", " ", " ", " ", " ", " ", "t"],
        ["'", "r", " ", " ", "r", "t", "r", "r", " ", " ", " ", " ", " ", " ", "r", "t", "t", " ", " ", "t"],
        ["'", "'", "l", "t", "r", "'", "'", "'", "t", " ", "l", " ", " ", " ", "l", " ", " ", " ", "l", "r"],
        ["'", "'", "'", "'", "'", "'", "'", "'", "'", "t", "t", "t", " ", " ", "r", "i", " ", " ", " ", "r"],
        ["'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "t", "t", "t", "t", "r", "r", "i", "r"]
    ],
    3: [
        ["t", "l", "t", "t", "r", "r", "t", "t", "t", "t", "t", "v", "v", "v", "v", "v", "v", "v", "v", "v"],
        ["t", " ", " ", " ", "t", " ", " ", "t", " ", " ", " ", "v", "v", "v", "v", "v", "v", "v", "v", "v"],
        ["t", " ", "l", " ", " ", " ", "r", "r", " ", " ", " ", "l", "v", "v", "v", "v", "v", "v", "v", "v"],
        ["t", " ", "r", " ", " ", " ", " ", " ", " ", "r", " ", " ", " ", " ", "v", "v", "v", "v", "v", "v"],
        ["t", " ", "r", "t", "r", "r", " ", " ", " ", "r", "r", "r", "r", " ", " ", " ", " ", "v", "v", "v"],
        ["t", " ", " ", "t", "t", "t", "r", "t", "t", "v", "l", "v", "v", "r", "r", "r", " ", " ", " ", "t"],
        ["t", " ", " ", "t", "t", "l", "r", "t", "v", "v", "v", "v", "v", " ", " ", " ", " ", " ", " ", "t"],
        ["t", "r", "l", " ", "t", " ", " ", " ", " ", "t", "v", "v", "l", " ", " ", "r", "r", " ", "l", "r"],
        ["t", "l", "t", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "l", "r", " ", "t", "r"],
        ["t", " ", " ", " ", "r", "r", "t", "t", "r", "r", "r", " ", " ", " ", " ", " ", "t", " ", "t", "t"],
        ["t", " ", " ", " ", " ", " ", " ", " ", " ", " ", "r", "l", "r", "t", " ", "t", "t", " ", "t", "t"],
        ["'", "r", " ", " ", " ", "r", "r", "r", "r", " ", " ", " ", " ", "r", "r", "t", "t", " ", "t", "t"],
        ["'", "'", "l", "t", "t", "'", "t", "r", "x", " ", " ", " ", " ", " ", "r", "t", " ", " ", "l", "r"],
        ["'", "'", "'", "'", "'", "'", "'", "t", "r", "r", "t", "t", " ", " ", "t", "t", " ", " ", " ", "r"],
        ["'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "l", "t", "t", "t", "r", "l", "r", "r"]
    ],
    4: [
        ["h", "'", "'", "'", "h", "'", "'", "'", "h", "'", "'", "v", "v", "v", "v", "v", "v", "v", "v", "v"],
        ["'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "v", "v", "v", "v", "v", "v", "v", "v", "v"],
        ["'", "'", "'", "'", "'", "'", "'", "t", "'", "'", "'", "l", "v", "v", "v", "v", "v", "v", "v", "v"],
        [" ", " ", " ", "t", " ", " ", " ", "l", " ", " ", " ", " ", " ", " ", "v", "v", "v", "v", "v", "v"],
        ["t", " ", " ", " ", " ", " ", " ", " ", " ", "r", "r", " ", " ", " ", "r", "r", " ", "x", "v", "v"],
        ["t", " ", " ", " ", "r", "l", "r", " ", "l", "v", "l", "t", "r", " ", " ", "r", "t", " ", " ", "t"],
        ["t", " ", " ", " ", "t", "t", "r", "t", "v", "v", "v", "v", "v", " ", " ", " ", "t", " ", " ", "t"],
        ["t", "r", " ", " ", "t", "t", "l", " ", " ", "t", "v", "v", "l", " ", " ", "r", "r", " ", "l", "r"],
        ["t", "l", " ", " ", " ", " ", "t", " ", " ", " ", "v", "v", " ", " ", " ", "l", "r", " ", "r", "r"],
        ["t", " ", " ", " ", " ", " ", " ", " ", " ", " ", "l", " ", " ", " ", " ", " ", "t", " ", "r", "t"],
        ["t", " ", " ", " ", " ", " ", " ", " ", " ", " ", "r", " ", " ", "t", " ", "t", "t", " ", " ", "t"],
        ["'", "r", " ", " ", "r", "t", "r", "r", " ", " ", "t", " ", " ", " ", "r", "t", "t", " ", " ", "t"],
        ["'", "'", "l", "t", "r", "'", "'", "'", "t", " ", "l", "t", " ", " ", "r", "t", "l", " ", " ", "r"],
        ["'", "'", "'", "'", "'", "'", "'", "'", "'", "r", "t", "t", "t", " ", " ", " ", " ", " ", " ", "r"],
        ["'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "l", "r", "r", "r", "r", "l", "r", "r"]
    ],
    5: [
        ["q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "'", "'", "'", "'"],
        ["q", " ", " ", " ", " ", " ", "c", "q", "c", " ", " ", " ", " ", " ", "c", "q", "'", "'", "'", "'"],
        ["q", "x", "a", "a", "a", "a", " ", "q", " ", "a", "a", "a", "a", "a", " ", "q", "'", "'", "'", "'"],
        ["q", " ", " ", " ", " ", "a", " ", "q", " ", "a", " ", " ", " ", "a", " ", "q", "q", "q", "q", "q"],
        ["q", "q", "q", "q", "c", "a", "c", "q", "c", "a", "c", "q", "c", "a", "c", "q", "c", " ", "c", "q"],
        ["'", "'", "'", "q", " ", "a", " ", "q", " ", "a", " ", "q", " ", "a", " ", "q", " ", "a", " ", "q"],
        ["'", "'", "'", "q", " ", "a", " ", "q", " ", "a", " ", "q", " ", "a", " ", "q", " ", "a", " ", "q"],
        ["'", "'", "'", "q", "c", "a", "c", "q", "c", "a", "c", "q", "c", "a", "c", "q", "c", "a", "c", "q"],
        ["'", "'", "'", "q", " ", "a", " ", "q", " ", "a", " ", "q", " ", "a", " ", "q", " ", "a", " ", "q"],
        ["'", "'", "'", "q", " ", "a", " ", "q", " ", "a", " ", "q", " ", "a", " ", "q", " ", "a", " ", "q"],
        ["'", "'", "'", "q", "c", "a", "c", "q", "c", "a", "c", "q", "c", "a", "c", "q", "c", "a", "c", "q"],
        ["'", "'", "'", "q", " ", "a", " ", " ", " ", "a", " ", "q", " ", "a", " ", " ", " ", "a", " ", "q"],
        ["'", "'", "'", "q", " ", "a", "a", "a", "a", "a", " ", "q", " ", "a", "a", "a", "a", "a", " ", "q"],
        ["'", "'", "'", "q", "c", " ", " ", " ", " ", " ", "c", "q", "c", " ", " ", " ", " ", " ", "c", "q"],
        ["'", "'", "'", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q"]
    ]
}


# tiles
class RockTile(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("pyg/rock_tile.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-20, -20)


class WaterTile(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("pyg/water.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -20)


class HouseTile(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("pyg/house_tile.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -20)


class TreeTile(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("pyg/tree_tile.png")
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.inflate(-20, -40)


class DoorTile(pygame.sprite.Sprite):
    def __init__(self, pos, group, level):
        super().__init__(group)
        self.image = pygame.image.load("pyg/boss_tile_"+str(level)+".png")
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, 0)


class IronTile(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("pyg/iron_tile.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-20, -20)


class WallTile(pygame.sprite.Sprite):
    def __init__(self, pos, group, level):
        super().__init__(group)
        self.image = pygame.image.load("pyg/wall_"+str(level)+"_tile.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-10, -20)


class QWallTile(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("pyg/Qwall_tile.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-10, -20)


class LightTile(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("pyg/light_tile.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-20, -20)


class Floor1Tile(pygame.sprite.Sprite):
    def __init__(self, pos, group, level):
        super().__init__(group)
        self.image = pygame.image.load("pyg/floor_"+str(level)+"_tile.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -20)


class ATile(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("pyg/carpet_tile.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -20)


class PillarTile(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("pyg/pillar_tile.png")
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.inflate(-20, -20)


class TreasureTile(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("pyg/treasure_tile.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, 0)


# level
class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.l_no = 1
        self.obstacles = pygame.sprite.Group()
        self.tiles = CustomTileGroup()
        self.floor = CustomTileGroup()
        # self.door = DoorTile((-1000, -1000), [self.tiles, self.obstacles], self.l_no)
        self.treasure = TreasureTile((-1000, -1000), [self.tiles])
        self.isCut = True
        self.start = True
        self.map()
        self.ui = UI()

    def map(self):
        if self.isCut:
            pygame.mixer.music.load("pyg/Mus_amalgam.oga")
            pygame.mixer.music.play(-1)
        for row_index, row in enumerate(level_map[self.l_no]):
            for col_index, map_tile in enumerate(row):
                tile_x = col_index * 100
                tile_y = row_index * 100
                if map_tile == "'" or map_tile == "h":
                    continue
                Floor1Tile((tile_x, tile_y), [self.floor], self.l_no)
        for row_index, row in enumerate(level_map[self.l_no]):
            for col_index, map_tile in enumerate(row):
                tile_x = col_index * 100
                tile_y = row_index * 100
                if map_tile == "r":
                    RockTile((tile_x, tile_y), [self.tiles, self.obstacles])
                if map_tile == "v":
                    WaterTile((tile_x, tile_y), [self.tiles, self.obstacles])
                if map_tile == "t":
                    TreeTile((tile_x+50, tile_y), [self.tiles, self.obstacles])
                if map_tile == "i":
                    IronTile((tile_x, tile_y), [self.tiles, self.obstacles])
                if map_tile == "w":
                    WallTile((tile_x, tile_y), [self.tiles, self.obstacles], self.l_no)
                if map_tile == "l":
                    LightTile((tile_x, tile_y), [self.tiles, self.obstacles])
                if map_tile == "p":
                    self.player = Player((tile_x, tile_y), [self.tiles], self.obstacles)
                if map_tile == "x":
                    self.door = DoorTile((tile_x, tile_y), [self.tiles, self.obstacles], self.l_no)
                if map_tile == "h":
                    HouseTile((tile_x, tile_y), [self.tiles, self.obstacles])
                if map_tile == "q":
                    QWallTile((tile_x, tile_y), [self.tiles, self.obstacles])
                if map_tile == "a":
                    ATile((tile_x, tile_y), [self.floor])
                if map_tile == "c":
                    PillarTile((tile_x+50, tile_y), [self.tiles, self.obstacles])

    def clear(self):
        for tile in self.tiles:
            if tile.__class__ == Player:
                continue
            tile.remove(self.tiles)
        self.obstacles.empty()
        self.floor.empty()

    def draw(self):
        if self.start:
            pygame.mixer.music.load("pyg/Mus-"+str(self.l_no)+".oga")
            pygame.mixer.music.play(-1)
            self.start = False
        fight_ran = randint(0, 1000)
        if fight_ran <= 5 and "_idle" not in self.player.status:
            pygame.mixer.music.load("pyg/Mus_f_intro.ogg")
            pygame.mixer.music.play(-1)
            ran = randint(1, 2)
            if ran == 1:
                enemy = Enemy("eye", self.player, 75, 0.01, 3, 0.95, 20, 30)
                enemy.fight()
            elif ran == 2 and self.l_no >= 2:
                enemy = Enemy("flyer", self.player, 80, 0.07, 3.5, 0, 20, 30)

                self.door.remove(self.tiles)
                self.door = DoorTile((-1000, -1000), [self.tiles], self.l_no)
                enemy.fight()
            self.start = True
        if self.player.rect.colliderect(self.door.rect):
            pygame.mixer.music.load("pyg/Mus-boss-"+str(self.l_no)+".oga")
            pygame.mixer.music.play(-1)
            if self.l_no == 1:
                enemy = Enemy("darklet", self.player, 100, 0.1, 4, 0, 100, 120)
                enemy.fight()
            elif self.l_no == 2:
                enemy = Enemy("induk", self.player, 150, 0.05, 5, 0, 140, 170)
                enemy.fight()
            elif self.l_no == 3:
                enemy = Enemy("godzilla", self.player, 225, 0.05, 7, 0, 160, 200)
                enemy.fight()
            elif self.l_no == 4:
                enemy = Enemy("catagents", self.player, 300, 0, 6, 0, 0, 300)
                enemy.fight()
            elif self.l_no == 5:
                enemy = Enemy("jayawardenepuraKotte", self.player, 400, 0, 10, 0, 0, 0)
                enemy.fight()
            self.isCut = True
            if self.l_no != 5:
                self.player.energy = self.player.stats["energy"]
                self.player.hp = self.player.stats["hp"]
                self.player.rect.centerx -= 50
                self.player.boss += 1
                self.l_no += 1
                self.clear()
                self.map()
                self.start = True
        self.floor.custom_draw(self.player)
        self.tiles.custom_draw(self.player)
        self.tiles.update()
        self.ui.draw(self.player)


class CustomTileGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.move = pygame.math.Vector2()
        self.center_x = self.display.get_size()[0]//2
        self.center_y = self.display.get_size()[1] // 2

    def custom_draw(self, player):
        self.move.x = player.rect.centerx - self.center_x
        self.move.y = player.rect.centery - self.center_y
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            tile_pos = sprite.rect.topleft - self.move
            self.display.blit(sprite.image, tile_pos)


# UI
class UI:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.SysFont("Comic Sans MS", 30)

        self.hp_bar = pygame.Rect(20, 15, 100, 15)
        self.energy_bar = pygame.Rect(20, 35, 100, 15)

    def draw(self, player):
        pygame.draw.rect(self.screen, "red", self.hp_bar)
        curr_hp_width = 100*player.hp/player.stats["hp"]
        curr_hp_bar = pygame.Rect(20, 15, curr_hp_width, 15)
        pygame.draw.rect(self.screen, "green", curr_hp_bar)
        pygame.draw.rect(self.screen, "#222222", self.energy_bar)
        curr_energy_width = 100 * player.energy / player.stats["energy"]
        curr_energy_bar = pygame.Rect(20, 35, curr_energy_width, 15)
        pygame.draw.rect(self.screen, "light blue", curr_energy_bar)
        kill_count = self.font.render("Exp: " + str(player.exp), False, "white")
        self.screen.blit(kill_count, (20, 50))
        love = self.font.render("LV: " + str(player.love), False, "white")
        self.screen.blit(love, (20, 85))
