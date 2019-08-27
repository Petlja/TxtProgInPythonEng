# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(400, 400, "Шах")
# -*- acsection: main -*-

tabla_slika = pg.image.load("chess_table.png")  # slika table
KRALJ, DAMA, TOP, LOVAC, SKAKAC, PESAK = 0, 1, 2, 3, 4, 5
fajlovi_crne_figure = [
    "black_king.png", "black_queen.png", "black_rook.png",
    "black_bishop.png", "black_knight.png", "black_pawn.png"
]
fajlovi_bele_figure = [
    "white_king.png", "white_queen.png", "white_rook.png",
    "white_bishop.png", "white_knight.png", "white_pawn.png"
]
crni = [pg.image.load(f) for f in fajlovi_crne_figure]
beli = [pg.image.load(f) for f in fajlovi_bele_figure]

prozor.blit(tabla_slika, (0, 0))
red_figura = [TOP, SKAKAC, LOVAC, DAMA, KRALJ, LOVAC, SKAKAC, TOP]
x = 0
for figura in red_figura:
    prozor.blit(crni[figura], (x, 0))
    prozor.blit(crni[PESAK], (x, 50))
    prozor.blit(beli[PESAK], (x, 300))
    prozor.blit(beli[figura], (x, 350))
    x += 50

# -*- acsection: after-main -*-
petljapg.wait_loop()
