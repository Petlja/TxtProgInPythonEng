# -*- acsection: general-init -*-
import pygame as pg, pygamebg
width, height = 300, 300
canvas = pygamebg.open_window(width, height, "Cube")

# -*- acsection: main -*-
canvas.fill(pg.Color("gray"))
dx1, dy1 = 100, 0
dx2, dy2 = 0, 100
dx3, dy3 = 50, -40
A = (50, 150)
B = (A[0] + dx1, A[1] + dy1)
D, C = [(T[0] + dx3, T[1] + dy3) for T in [A, B]]
A1, B1, C1, D1 = [(T[0] + dx2, T[1] + dy2) for T in [A, B, C, D]]

for P, Q in [
    (A, A1), (B, B1), (C, C1), (D, D1),
    (A, B), (D, C), (A1, B1), (D1, C1),
    (A, D), (B, C), (A1, D1), (B1, C1)]:
        pg.draw.line(canvas, pg.Color("black"), P, Q, 1)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
