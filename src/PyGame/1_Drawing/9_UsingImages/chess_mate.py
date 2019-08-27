# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(400, 400, "Chess")
# -*- acsection: main -*-

board = pg.image.load("chess_table.png")  # image of a chessboard
white_king =  pg.image.load("white_king.png")
white_rook =  pg.image.load("white_rook.png")
black_king =  pg.image.load("black_king.png")
square_size = 50

def put_piece(piece, row, column):
    canvas.blit(piece, (column * square_size, row * square_size))
    
canvas.blit(board, (0, 0))
put_piece(white_king, 2, 6)
put_piece(white_rook, 0, 5)
put_piece(black_king, 0, 7)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
