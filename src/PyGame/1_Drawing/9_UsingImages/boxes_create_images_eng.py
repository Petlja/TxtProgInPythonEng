# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          
pg.display.set_caption("Boxes")    
width, height = 800, 600           
canvas = pg.display.set_mode((width, height))
# -*- acsection: main -*-

box_image = pg.image.load("box.png")  # image of a box

canvas.fill(pg.Color("lightgray"))
for i in range(4):
    canvas.blit(box_image, (60+120*i, 400))
pg.display.update()
pg.image.save(canvas, 'x4.png')


canvas.fill(pg.Color("lightgray"))
for i in range(4):
    canvas.blit(box_image, (420, 400-95*i))
pg.display.update()
pg.image.save(canvas, 'y4.png')


canvas.fill(pg.Color("lightgray"))
for ix in range(4):
    for iy in range(ix+1):
        canvas.blit(box_image, (60+120*ix, 400-95*iy))
pg.display.update()
pg.image.save(canvas, 'x4yi.png')

# -*- acsection: after-main -*-

while pg.event.wait().type != pg.QUIT:
    pass

pg.quit()
