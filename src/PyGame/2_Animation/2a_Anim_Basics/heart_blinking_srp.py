import pygame as pg, petljapg
prozor = petljapg.open_window(200, 181, "Срце")

# slike manjeg i veceg srca
srce_slike = [
    pg.image.load("heart_smaller.png"),  
    pg.image.load("heart_bigger.png")
]

indeks_slike = 0 # redni broj slike koju cemo prikazati

def nov_frejm():
    global indeks_slike
    indeks_slike = 1 - indeks_slike       # biramo onu drugu sliku

    prozor.fill(pg.Color("blue"))         # bojimo pozadinu u plavo
    prozor.blit(srce_slike[indeks_slike], (0, 0))

petljapg.frame_loop(2, nov_frejm)
