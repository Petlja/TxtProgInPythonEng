# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(400, 400, "Шах")
# -*- acsection: main -*-

tabla = pg.image.load("chess_table.png")  # slika table
beli_kralj =  pg.image.load("white_king.png")
beli_top =  pg.image.load("white_rook.png")
crni_kralj =  pg.image.load("black_king.png")
velicina_polja = 50

def stavi_figuru(fig, red, kol):
    prozor.blit(fig, (kol * velicina_polja, red * velicina_polja))
    
prozor.blit(tabla, (0, 0))
stavi_figuru(beli_kralj, 2, 6)
stavi_figuru(beli_top, 0, 5)
stavi_figuru(crni_kralj, 0, 7)

# -*- acsection: after-main -*-
petljapg.wait_loop()
