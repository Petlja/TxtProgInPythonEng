import pygame as pg, petljapg
(sirina, visina) = (400, 300)
prozor = petljapg.open_window(sirina, visina, "Аутомобил")

auto_slika = pg.image.load("car.png")   # slika automobila
(sirina_auta, visina_auta) = (auto_slika.get_width(), auto_slika.get_height()) # dimenzije slike automobila

fps = 50       # broj frejmova u sekundi
dt = 1 / fps   # trajanje jednog frejma u sekundama
auto_v = 100   # brzina automobila (broj piksela u sekundi)
(auto_x, auto_y) = (0, visina - visina_auta) # polozaj auta (na pocetku donji levi ugao)

def nov_frejm():
    global auto_x               # menjaćemo samo x koordinatu auta
    auto_x += auto_v * dt       # pomeramo auto nadesno
    if auto_x > sirina:         # ako je ispao van prozora
        auto_x = - sirina_auta  #     vraćamo ga na početak

    prozor.fill(pg.Color("skyblue"))            # bojimo pozadinu u nebo-plavu
    prozor.blit(auto_slika, (auto_x, auto_y))   # prikazujemo sliku auta

petljapg.frame_loop(fps, nov_frejm)
