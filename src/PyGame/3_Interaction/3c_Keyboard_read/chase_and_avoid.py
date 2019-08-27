import pygame as pg, pygamebg, random
num_rows, num_cols = 15, 15
a = 30 # square size
(width, height) = (a* num_cols, a * num_rows)
canvas = pygamebg.open_window(width, height, "Chase and avoid")
font = pg.font.SysFont("Arial", 30) # font to display text

(player_row, player_col) = (num_rows // 2, num_cols // 2)

num_bots = 8
bots = []
for _ in range(num_bots):
    bot_pos = (random.randint(0,num_rows-1), random.randint(0,num_rows-1))
    bots.append(bot_pos)

(target_row, target_col) = (random.randint(0,num_rows-1), random.randint(0,num_rows-1))
the_end, won = False, False

def new_frame():
    global player_row, player_col, bots, the_end, won

    # move the player
    pressed = pg.key.get_pressed()
    if pressed[pg.K_LEFT] and (player_col > 0):           player_col -= 1
    if pressed[pg.K_RIGHT] and (player_col < num_cols-1): player_col += 1
    if pressed[pg.K_UP] and (player_row > 0):             player_row -= 1
    if pressed[pg.K_DOWN] and (player_row < num_rows-1):  player_row += 1
    
    # move bots
    for i in range(num_bots):
        d_row, d_col = 0, 0
        if random.randint(1,5) == 1:
            d_row, d_col = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        bot_row, bot_col = bots[i]
        bot_row += d_row
        bot_col += d_col
        if (bot_col >= 0 and bot_col < num_cols and
            bot_row >= 0 and bot_row < num_rows):
            bots[i] = bot_row, bot_col 

    # are there any collisions?
    for bot_row, bot_col in bots:
        if bot_row == player_row and bot_col == player_col:
            the_end, won = True, False
    if target_row == player_row and target_col == player_col:
        the_end, won = True, True

    canvas.fill(pg.Color("gray"))   # paint canvas to gray

    if the_end:
        if won: 
            sl = font.render('Well done!', True, pg.Color("red"))
        else:
            sl = font.render('What a pity!', True, pg.Color("blue"))
        canvas.blit(sl, (0, 0))
    else:
        # draw player
        (x, y) = (player_col * a + a//2, player_row * a + a//2)
        pg.draw.circle(canvas, pg.Color('yellow'), (x, y), a // 3)
        
        (x, y) = (target_col * a + a//2, target_row * a + a//2)
        pg.draw.circle(canvas, pg.Color('white'), (x, y), a // 5)
        
        # draw bots
        for bot_row, bot_col in bots:
            (x, y) = (bot_col * a + a//2, bot_row * a + a//2)
            pg.draw.circle(canvas, pg.Color('black'), (x, y), a // 5)
    
pygamebg.frame_loop(15, new_frame)
