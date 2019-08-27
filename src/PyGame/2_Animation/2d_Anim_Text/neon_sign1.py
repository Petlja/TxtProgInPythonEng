import pygame as pg, pygamebg
text = "PYTHON"
(width, height) = (len(text) * 70, 100)
canvas = pygamebg.open_window(width, height, "Neon sign")

font = pg.font.SysFont("Arial", 80) # the font for displaying the text
text_image = font.render(text, True, pg.Color("yellow"))
x = (width - text_image.get_width()) // 2
y = (height - text_image.get_height()) // 2
turned_on = True

def new_frame():
    global turned_on    
    turned_on = not turned_on
    canvas.fill(pg.Color("black")) # paint background to black
    if turned_on: 
        canvas.blit(text_image, (x, y))

pygamebg.frame_loop(3, new_frame)
