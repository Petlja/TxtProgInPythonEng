import pygame as pg, petljapg
(sirina, visina) = (500, 200)
prozor = petljapg.open_window(sirina, visina, "Текст")

font = pg.font.SysFont("Arial", 30) # font kojim će biti prikazan tekst

tekst = "Пример исписивања текста"
slika_teksta = font.render(tekst, True, pg.Color("green"))
x = (sirina - slika_teksta.get_width()) // 2
y = (visina - slika_teksta.get_height()) // 2


prozor.fill(pg.Color("black"))
prozor.blit(slika_teksta, (x, y))

petljapg.wait_loop()
