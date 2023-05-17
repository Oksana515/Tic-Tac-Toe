import pygame as pg

pg.init()

clock = pg.time.Clock()

W = 1150
H = 900
screen = pg.display.set_mode((W, H))

BG = 0, 25, 51
cell_color = 0, 51, 102

# cell side size
a = 90

# loading images for x and o
x = pg.transform.scale(pg.image.load('x.png'), (a, a))
o = pg.transform.scale(pg.image.load('o.png'), (a, a))

# list of cell coordinates
cell_list = []
cell_x = 420
cell_y = 270
cell_gap = a + 5
cell_0 = (cell_x, cell_y)
cell_1 = (cell_x + cell_gap, cell_y)
cell_2 = (cell_x + 2 * cell_gap, cell_y)
cell_3 = (cell_x, cell_y + cell_gap)
cell_4 = (cell_x + cell_gap, cell_y + cell_gap)
cell_5 = (cell_x + 2 * cell_gap, cell_y + cell_gap)
cell_6 = (cell_x, cell_y + 2 * cell_gap)
cell_7 = (cell_x + cell_gap, cell_y + 2 * cell_gap)
cell_8 = (cell_x + 2 * cell_gap, cell_y + 2*cell_gap)

cell_list.extend((cell_0, cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8))


class Cell(pg.sprite.Sprite):
    def __init__(self, x0, y0):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((a, a))
        self.image.fill(cell_color)
        self.rect = self.image.get_rect()
        self.rect.x = x0
        self.rect.y = y0
        self.clicked = False

    def update(self, ev, pos):
        #print(self.clicked)
        # if someone clicks the mouse button
        if ev.type == pg.MOUSEBUTTONDOWN:
            # if mouse cursor is in the cell
            if self.rect.x < pos[0] < self.rect.x + a and self.rect.y < pos[1] < self.rect.y + a:
                self.clicked = True

    def draw(self):
        if self.clicked:
            self.image = x
        screen.blit(self.image, self.rect)

    def lightning(self, pos):
        if not self.clicked:
            if self.rect.x < pos[0] < self.rect.x + a and self.rect.y < pos[1] < self.rect.y + a:
                pg.draw.rect(screen, (255, 255, 255), pg.Rect(self.rect.x, self.rect.y, a, a))


cell_group = pg.sprite.Group()
for i in range(9):
    cell = Cell(cell_list[i][0], cell_list[i][1])
    cell_group.add(cell)


run = True

while run:

    clock.tick(60)

    screen.fill(BG)

    mouse_pos = pg.mouse.get_pos()

    for c in cell_group:
        c.draw()
        c.lightning(mouse_pos)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        cell_group.update(event, mouse_pos)

    pg.display.flip()

