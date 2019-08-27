# -*- acsection: general-init -*-
import pygame as pg, pygamebg, random
(width, height) = (400, 400)
canvas = pygamebg.open_window(width, height, "Snake")

snake_color = (255, 0, 0)          # color of the snake
a = 10                             # square size
num_rows, num_cols = height // a, width // a # board size
(d_row, d_col) = (0, 1) # initially one column to the right (per frame)
center = (num_rows // 2, num_cols // 2) # coordinates of the center of the board
snake = [center] * 10 # initially a snake curled up in the center
i_head = 0 # index of the snakes head in the list
done = False

def draw():
    canvas.fill(pg.Color("gray")) # paint background
    if done:
        # Display the game over mesage
        font = pg.font.SysFont("Arial", 60)
        text_image = font.render("Game over.", True, pg.Color("black"))
        x = (width - text_image.get_width()) // 2
        y = (height - text_image.get_height()) // 2
        canvas.blit(text_image, (x, y))
    else:
        # draw snake
        for row, col in snake:
            pg.draw.rect(canvas, snake_color, (col*a, row*a, a, a))


def new_frame():
    global snake, i_head, d_row, d_col, done
# -*- acsection: main -*-

    pressed = pg.key.get_pressed()
    if pressed[pg.K_LEFT]:  (d_row, d_col) = (0, -1)
    if pressed[pg.K_RIGHT]: (d_row, d_col) = (0, 1)
    if pressed[pg.K_UP]:    (d_row, d_col) = (-1, 0)
    if pressed[pg.K_DOWN]:  (d_row, d_col) = (1, 0)
    
# -*- acsection: after-main -*-
    # compute the new position of the snake head
    row, col = snake[i_head]
    i_head = (i_head + 1) % len(snake)
    snake[i_head] = (row + d_row, col + d_col)
    if col < 0 or col >= num_cols or row < 0 or row >= num_rows:
        done = True  # snake came out of the board
    
    draw()


pygamebg.frame_loop(10, new_frame)
