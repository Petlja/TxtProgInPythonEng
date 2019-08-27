import pygame as pg, pygamebg, random
(width, height) = (600, 400)
canvas = pygamebg.open_window(width, height, "Typing - shooting")

def write(message, x, y):
    font = pg.font.SysFont("Arial", 32) # font for displaying the message
    text_image = font.render(message, True, pg.Color("green"))
    canvas.blit(text_image, (x, y)) # display the image

def draw():
    canvas.fill(pg.Color("black"))    # paint canvas
    if not game_over:
        # if the game is still running, 
        # display the falling letters and the number of points
        for letter, x, y in falling_letters:
            write(letter, x, y)
        write('score: ' + str(score), 0, height - 40)
    else:
        # otherwise write a message
        write('Game over', 100, 100)
        write('you scored ' + str(score) + ' points', 100, 200)

def new_frame():
    global falling_letters, time_until_next_letter, next_x
    global choice_starting_letter, letters_to_chose_from, game_over
    # move all falling letters two pixels down, check whether the game is still running
    new_letters = []
    for letter, x, y in falling_letters:
        if y < height - 40: 
            new_letters.append((letter, x, y + 2))
        else:
            # if a letter has reached the bottom of the window, the game is over
            game_over = True 
            
    # update list of falling letters
    time_until_next_letter -= 1
    if time_until_next_letter <= 0: # if another falling letter needs to be added...
        time_until_next_letter = 20
        next_x += 20
        if next_x >= width:
            # row of letteres is filled, update letters to chose from
            next_x -= width
            if choice_starting_letter + NUM_LETTERS_TO_CHOSE_FROM < len(letters):
                choice_starting_letter += 1
                letters_to_chose_from = letters[choice_starting_letter : choice_starting_letter + NUM_LETTERS_TO_CHOSE_FROM]
        # add one more falling letter
        letter = random.choice(letters_to_chose_from)
        new_letters.append((letter, next_x, 0))

    falling_letters = new_letters
    draw()
    
def handle_event(event):
    global falling_letters, score
    if event.type == pg.KEYDOWN: # keystroke on the keyboard
        key_typed = chr(event.key).upper()
        if len(falling_letters) > 0: # if there are falling letters
            letter, x, y = falling_letters[0] # lowest falling letter
            if key_typed == letter:
                del falling_letters[0]
                score += 10 # reward for typing the lowest letter
            else:
                score -= 4  # penalty for the wrong letter
            
letters = 'ASDFJKL;EIRUTYGHWOQPC,VMBNXZ.-'
NUM_LETTERS_TO_CHOSE_FROM = 4
choice_starting_letter = 0
letters_to_chose_from = letters[choice_starting_letter : choice_starting_letter + NUM_LETTERS_TO_CHOSE_FROM]
falling_letters = []
time_until_next_letter = 0
next_x = 0
score = 0
game_over = False

pygamebg.frame_loop(30, new_frame, handle_event)
