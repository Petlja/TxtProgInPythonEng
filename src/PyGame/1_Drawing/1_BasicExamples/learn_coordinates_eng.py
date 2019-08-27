# -*- acsection: general-init -*-
import pygame as pg

print(pg.__path__)

pg.init()
pg.display.set_caption("Pygame")
(width, height) = (300, 300)
canvas = pg.display.set_mode((width, height))

def draw_text(s, x, y):
    font = pg.font.SysFont("Arial", 25)
    text = font.render(s, True, pg.Color("red"))
    (text_width, text_height) = (text.get_width(), text.get_height())
    (x, y) = (x - text_width * (x / width), y - text_height * (y / height))
    canvas.blit(text, (x, y))
# -*- acsection: main -*-

# -*- acsection: after-main -*-
while True:
    event = pg.event.wait()

    if event.type == pg.QUIT:
        break
    elif event.type == pg.MOUSEMOTION:
        canvas.fill(pg.Color("white"))
        (x, y) = event.pos
        pg.draw.line(canvas, pg.Color("black"), (x, 0), (x, height))
        pg.draw.line(canvas, pg.Color("black"), (0, y), (width, y))
        s = "(" + str(x) + ", " + str(y) + ")"
        draw_text(s, x, y)
        s = "x: " + str(x) + " " + "y: " + str(y)
        pg.display.set_caption(s)
        pg.display.update()

pg.quit()
