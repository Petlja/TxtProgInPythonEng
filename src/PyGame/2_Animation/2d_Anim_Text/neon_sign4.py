import pygame as pg, pygamebg
tekst = "PYTHON"
(width, height) = (400, 100)
canvas = pygamebg.open_window(width, height, "Neon sign")

font = pg.font.SysFont("Arial", 80) # the font for displaying the text
text_image = font.render(tekst, True, pg.Color("yellow"))
x = width
y = (height - text_image.get_height()) // 2


def new_frame():
    global x
    x = x - 2
    if x + text_image.get_width() < 0:
        x = width
    canvas.fill(pg.Color("black")) # paint background to black
    canvas.blit(text_image, (x, y))

pygamebg.frame_loop(60, new_frame)
