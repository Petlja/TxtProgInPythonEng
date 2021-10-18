import pygame as pg
import pygamebg as pgbg

(width, height) = (800, 500)
window = pgbg.open_window(width, height, "Rocket")

pg.key.set_repeat(10,10)

# load images
rocket  = pg.image.load("rocket.png")
martian = pg.image.load("martian.png")
martian_heart = pg.image.load("martian_heart.png")
planet  = pg.image.load("planet.png")

# martian parameters - horizontal position and speed
martian_x = 0
martian_y = planet.get_height()
martian_speed = 3

# rocket position
rocket_x = 0
rocket_y = height - rocket.get_height()



# greeting positions
greetings = []

# handle events
def keydown(e):
    # variable that is changed
    global rocket_x
    # right and left arrow moves the rocket by 5 pixels
    if e.key == pg.K_RIGHT:
        rocket_x += 5
    elif e.key == pg.K_LEFT:
        rocket_x -= 5
    elif e.key == pg.K_SPACE:
        if len(greetings) == 0:
            greetings.append((rocket_x, rocket_y))

# draw sceen
def draw():
    # variables that are changed in this function
    global martian_x, martian_speed, greetings

    # clear screen
    window.fill(pg.Color("black"))

    # draw planets
    for i in range(8):
        window.blit(planet, (100*i, 0))
        
    # draw rocket
    window.blit(rocket, (rocket_x, rocket_y))
    
    # draw greetings
    font = pg.font.SysFont("Arial", 20)
    greeting = font.render("Hello!", True, pg.Color("white"))
    for (greeting_x, greeting_y) in greetings:
        window.blit(greeting, (greeting_x, greeting_y))

    # move greetings
    new_greetings = []
    for (greeting_x, greeting_y) in greetings:
        dy = 3
        if greeting_y >= dy:
            new_greetings.append((greeting_x, greeting_y - dy))
        greetings = new_greetings

    # move martian
    martian_x += martian_speed
    # change direction if it falls of screen
    if martian_x < 0 or martian_x > width - martian.get_width():
        martian_speed = -martian_speed

    # check if martian is hit by a greeting
    hit = False
    martian_rect = pg.Rect(martian_x, martian_y, martian.get_width(), martian.get_height())
    for (greeting_x, greeting_y) in greetings:
        greeting_rect = pg.Rect(greeting_x, greeting_y, greeting.get_width(), greeting.get_height())
        if martian_rect.colliderect(greeting_rect):
            hit = True

    # draw martian
    if not hit:
        window.blit(martian, (martian_x, martian_y))
    else:
        window.blit(martian_heart, (martian_x, martian_y))

pgbg.frame_loop(100, draw, {pg.KEYDOWN: keydown})
