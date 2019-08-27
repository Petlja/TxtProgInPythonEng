import pygame as pg, pygamebg, random
(width, height) = (300, 300)
canvas = pygamebg.open_window(width, height, "paper rock scissors")

PAPER, ROCK, SCISSORS = 0, 1, 2
images = [
    pg.image.load("paper.png"), 
    pg.image.load("rock.png"), 
    pg.image.load("scissors.png")
]
image_x = width // 4 - images[0].get_width() // 2
image_y = height // 2 - images[0].get_height() // 2

# the meaning of the elements in the lists 'human' and 'computer'
NAME, CHOICE, SCORE, IMAGE_X, IMAGE_Y, TEXT_X, TEXT_Y = 0, 1, 2, 3, 4, 5, 6
human =   ["Human",   -1, 0, image_x,             image_y,         0, 0]
computer = ["Computer", -1, 0, image_x + width//2, image_y, width//2, 0]
font = pg.font.SysFont("Arial", 20)

def display_player(player):
    if player[CHOICE] >= 0:
        canvas.blit(images[player[CHOICE]], (player[IMAGE_X], player[IMAGE_Y]))
    text = player[NAME] + ": " + str(player[SCORE])
    text_image = font.render(text, True, pg.Color("black"))
    canvas.blit(text_image, (player[TEXT_X], player[TEXT_Y]))
    
def new_frame():
    canvas.fill(pg.Color("white"))
    display_player(human)
    display_player(computer)
    
def handle_event(event):
    global human, computer
    if event.type == pg.KEYDOWN:
        pkm = {pg.K_p : PAPER, pg.K_r : ROCK, pg.K_s : SCISSORS}
        if event.key in pkm.keys():
            human[CHOICE] = pkm[event.key]
            computer[CHOICE] = random.randint(0, 2)
            if computer[CHOICE] == (human[CHOICE] + 1) % 3:
                human[SCORE] += 1
            elif human[CHOICE] == (computer[CHOICE] + 1) % 3:
                computer[SCORE] += 1
    
pygamebg.frame_loop(15, new_frame, handle_event)
