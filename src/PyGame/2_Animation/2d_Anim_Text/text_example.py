import pygame as pg, pygamebg
(width, height) = (500, 200)
canvas = pygamebg.open_window(width, height, "Text")

font = pg.font.SysFont("Arial", 30) # the font for displaying the text

text = "Example of displaying text"
text_image = font.render(text, True, pg.Color("green"))
x = (width - text_image.get_width()) // 2
y = (height - text_image.get_height()) // 2


canvas.fill(pg.Color("black"))
canvas.blit(text_image, (x, y))

pygamebg.wait_loop()
