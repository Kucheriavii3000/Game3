import pygame as pg
import os
import sys

pg.init()

SIZE_WINDOW = WIDHT, HEIGHT = 300, 300
BG_COLOR = (0, 128, 0)
FPS = 60
clock = pg.time.Clock()

screen = pg.display.set_mode(SIZE_WINDOW)

images = []
patch = 'Image/Bear'
for file_name in os.listdir(patch):
    image = pg.image.load(patch + os.sep + file_name)
    images.append(image)

class AnimateSprite(pg.sprite.Sprite):
    def __init__(self, x, y, img):
        pg.sprite.Sprite.__init__(self)
        self.images = img
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.index += 1
        self.image = self.images[int(self.index % len(self.images))]

bear = AnimateSprite(x=WIDHT // 2, y=HEIGHT // 2, img=images)
sprites = pg.sprite.Group(bear)

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit(0)

    screen.fill(BG_COLOR)

    sprites.update()
    sprites.draw(screen)

    pg.display.update()
    clock.tick(FPS)
