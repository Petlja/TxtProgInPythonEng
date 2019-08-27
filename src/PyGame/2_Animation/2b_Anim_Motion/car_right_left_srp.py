import pygame as pg, petljapg
(sirina, visina) = (400, 300)
prozor = petljapg.open_window(sirina, visina, "Аутомобил")

auto_nadesno_slika = pg.image.load("car.png") 
# pravimo sliku kao u ogledalu (simetricnu u odnosu na vertikalnu osu)
auto_nalevo_slika = pg.transform.flip(auto_nadesno_slika, True, False)
auto_slike = (auto_nadesno_slika, auto_nalevo_slika)

# dimenzije slike automobila
(sirina_auta, visina_auta) = (auto_nalevo_slika.get_width(), auto_nalevo_slika.get_height()) 

fps = 50       # broj frejmova u sekundi
dt = 1 / fps   # trajanje jednog frejma u sekundama
auto_v = 100   # brzina automobila (broj piksela u sekundi)
auto_smer = 0  # smer kretanja - 0 za nadesno, 1 za nalevo (ujedno indeks odgovarajuce slike auta u torki) 
(auto_x, auto_y) = (0, visina - visina_auta) # polozaj auta (na pocetku donji levi ugao)

def nov_frejm():
    global auto_x, auto_v, auto_smer # menjaćemo položaj, brzinu i smer auta
    auto_x += auto_v * dt    # pomeramo auto 
    if auto_x > sirina or auto_x < -sirina_auta: 
        # ako je auto ispao van prozora nadesno ili nalevo
        auto_smer = 1 - auto_smer
        auto_v = -auto_v
        
    prozor.fill(pg.Color("skyblue"))                 # bojimo pozadinu u nebo-plavu
    prozor.blit(auto_slike[auto_smer], (auto_x, auto_y))   # prikazujemo sliku auta

petljapg.frame_loop(fps, nov_frejm)
