import pygame as pg, pygamebg
(width, height) = (400, 400)
canvas = pygamebg.open_window(width, height, "Snakes")

a = 10                                          # square size
num_rows, num_cols = height // a, width // a # board size

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
keys_1 = (pg.K_w, pg.K_s, pg.K_a, pg.K_d)
keys_2 = (pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)
snake_body_1 = [(num_rows//2, num_cols//3)] * 20
snake_body_2 = [(num_rows//2, 2*num_cols//3)] * 20

#          color             position      dir     U D L R head index
snake_1 = [pg.Color('red'),  snake_body_1, (0,1),  keys_1,      0]
snake_2 = [pg.Color('blue'), snake_body_2, (0,-1), keys_2,      0]
snakes = [snake_1, snake_2]
done = False

def draw():
    canvas.fill(pg.Color("gray"))     # paint background to gray
    if done:
        font = pg.font.SysFont("Arial", 60)
        image_text = font.render("The end!", True, pg.Color("black"))
        x = (width - image_text.get_width()) // 2
        y = (height - image_text.get_height()) // 2
        canvas.blit(image_text, (x, y))
    else:
        # draw snakes
        for color, body, direction, keys, i_head in snakes:                
            for row, col in body:
                pg.draw.rect(canvas, color, (col*a, row*a, a, a))

def new_frame():
    global snakes, done
    pressed = pg.key.get_pressed()
    for i_snake in range(2):
        color, body, (d_row, d_col), keys, i_head = snakes[i_snake]
        if pressed[keys[LEFT]]:  (d_row, d_col) = (0, -1)
        if pressed[keys[RIGHT]]: (d_row, d_col) = (0, 1)
        if pressed[keys[UP]]:  (d_row, d_col) = (-1, 0)
        if pressed[keys[DOWN]]:  (d_row, d_col) = (1, 0)        
        row, col = body[i_head]
        i_head = (i_head + 1) % len(body)
        body[i_head] = (row + d_row, col + d_col)
        if col < 0 or col >= num_cols or row < 0 or row >= num_rows:
            done = True  # the snake came out of the board
        snakes[i_snake] = color, body, (d_row, d_col), keys, i_head

    draw()

pygamebg.frame_loop(3, new_frame)
