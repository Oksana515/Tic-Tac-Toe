import pygame as pg

pg.init()

clock = pg.time.Clock()

W = 1150
H = 900
screen = pg.display.set_mode((W, H))

# define colors
BG = 0, 25, 51
cell_color = 0, 51, 102
dark_red1 = 102, 0, 0
dark_green1 = 0, 102, 0

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
        self.status = None

    def update(self, ev, pos):
        global turn
        # if someone clicks the mouse button
        if ev.type == pg.MOUSEBUTTONDOWN:
            # if mouse cursor is in the cell
            if self.rect.x < pos[0] < self.rect.x + a and self.rect.y < pos[1] < self.rect.y + a and not self.clicked:
                self.clicked = True
                turn *= -1
                if turn == 1:
                    self.status = 1
                else:
                    self.status = 2

    def draw(self):
        if self.clicked:
            if self.status == 1:
                self.image = x
            else:
                self.image = o
        screen.blit(self.image, self.rect)

    def lightning(self, pos):
        global turn
        if not self.clicked:
            if self.rect.x < pos[0] < self.rect.x + a and self.rect.y < pos[1] < self.rect.y + a:
                if turn == -1:
                    pg.draw.rect(screen, dark_red1, pg.Rect(self.rect.x, self.rect.y, a, a))
                elif turn == 1:
                    pg.draw.rect(screen, dark_green1, pg.Rect(self.rect.x, self.rect.y, a, a))


cell_group = pg.sprite.Group()
for i in range(9):
    cell = Cell(cell_list[i][0], cell_list[i][1])
    cell_group.add(cell)

turn = -1

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

