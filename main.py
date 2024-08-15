import sys
import pygame
from level import Level

pygame.init()
pygame.font.init()
pygame.mixer.init()

# display creation
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("wild")

# set font
my_font = pygame.font.SysFont('Comic Sans MS', 30)

cutscenes = [
    [pygame.image.load("pyg/cutscene_1_1.png"), pygame.image.load("pyg/cutscene_1_2.png"),
     pygame.image.load("pyg/cutscene_1_3.png")],
    [pygame.image.load("pyg/cutscene_2_1.png"), pygame.image.load("pyg/cutscene_2_2.png")],
    [pygame.image.load("pyg/cutscene_3_1.png"), pygame.image.load("pyg/cutscene_3_2.png")],
    [pygame.image.load("pyg/cutscene_4_1.png"), pygame.image.load("pyg/cutscene_4_2.png")],
    [pygame.image.load("pyg/cutscene_6_1.png"), pygame.image.load("pyg/cutscene_6_2.png")],
    [pygame.image.load("pyg/cutscene_5_1.png"), pygame.image.load("pyg/cutscene_5_2.png"),
     pygame.image.load("pyg/cutscene_5_3.png"), pygame.image.load("pyg/cutscene_5_4.png"),
     pygame.image.load("pyg/cutscene_5_5.png"), pygame.image.load("pyg/cutscene_5_6.png")]
]

cut_no = 0
frame = 0
frame_vel = 0.003

level1 = Level()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if level1.isCut:
        screen.blit(cutscenes[cut_no][int(frame)], (0, 0))
        frame += frame_vel
        if frame >= len(cutscenes[cut_no]):
            frame = 0
            level1.isCut = False
            cut_no += 1
            if cut_no == 6:
                sys.exit()
        pygame.display.update()
    else:
        screen.fill("#000000", (0, 0, 1000, 750))
        level1.draw()
        pygame.display.update()

    clock.tick(60)
