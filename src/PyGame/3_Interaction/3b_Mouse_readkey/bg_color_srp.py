import pygame as pg, petljapg
prozor = petljapg.open_window(400, 400, "Боја позадине")

nijansa = 128

def nov_frejm():
    global nijansa
    pritisnut_taster_misa = pg.mouse.get_pressed()
    if pritisnut_taster_misa[0] and nijansa < 255: # 0 je levi taster
        nijansa += 1
    if pritisnut_taster_misa[2] and nijansa > 0: # 2 je desni tater
        nijansa -= 1
            
    boja = (nijansa, nijansa, nijansa)
    prozor.fill(boja) 

petljapg.frame_loop(100, nov_frejm)
