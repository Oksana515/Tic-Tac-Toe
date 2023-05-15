import pygame as pg

pg.init()

clock = pg.time.Clock()

W = 1150
H = 900
screen = pg.display.set_mode((W, H))

BG = 0, 25, 51

run = True

while run:

    clock.tick(60)

    screen.fill(BG)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()


