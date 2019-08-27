# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(400, 400, "Chess")
# -*- acsection: main -*-

board_image = pg.image.load("chess_table.png")  # image of a chessboard
KING, QUUEN, ROOK, BISHOP, KNIGHT, PAWN = 0, 1, 2, 3, 4, 5
image_files_black_pieces = [
    "black_king.png", "black_queen.png", "black_rook.png",
    "black_bishop.png", "black_knight.png", "black_pawn.png"
]
image_files_white_pieces = [
    "white_king.png", "white_queen.png", "white_rook.png",
    "white_bishop.png", "white_knight.png", "white_pawn.png"
]
black = [pg.image.load(f) for f in image_files_black_pieces]
white = [pg.image.load(f) for f in image_files_white_pieces]

canvas.blit(board_image, (0, 0))
first_last_rank = [ROOK, KNIGHT, BISHOP, QUUEN, KING, BISHOP, KNIGHT, ROOK]
x = 0
for piece in first_last_rank:
    canvas.blit(black[piece], (x, 0))
    canvas.blit(black[PAWN], (x, 50))
    canvas.blit(white[PAWN], (x, 300))
    canvas.blit(white[piece], (x, 350))
    x += 50

# -*- acsection: after-main -*-
pygamebg.wait_loop()
