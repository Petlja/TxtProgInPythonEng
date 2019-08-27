import random, pygame as pg, pygamebg
(width, height) = (500, 300)
canvas = pygamebg.open_window(width, height, "Balls")

colors = (
    pg.Color("red"), pg.Color("yellow"), pg.Color("blue"),
    pg.Color("cyan"), pg.Color("green"), pg.Color("purple")
)

# Make a list of 10 balls. The ball is determined by
#  position (x, y), displacement (dx, dy), size (r) and color.
x, y, dx, dy, r, color = [], [], [], [], [], []
for _ in range(10):
    r.append(random.randint(10, 30))
    x.append(random.randint(r[-1], width - r[-1]))
    y.append(random.randint(r[-1], height - r[-1]))
    color.append(random.choice(colors))
    kdx, kdy = 0, 0
    while kdx == 0 and kdy == 0: # we don't want the balls that stand still
        kdx = random.randint(-8, 8)
        kdy = random.randint(-8, 8)
    dx.append(kdx)
    dy.append(kdy)
    
def new_frame():
    global x, y, dx, dy, r, color
    for i in range(10):
        x[i] = x[i] + dx[i]
        y[i] = y[i] + dy[i]
        if x[i] - r[i] < 0 or x[i] + r[i] > width: 
            dx[i] = -dx[i]
        if y[i] - r[i] < 0 or y[i] + r[i] > height: 
            dy[i] = -dy[i]
        
    canvas.fill(pg.Color("darkgray"))
    for i in range(10):
        pg.draw.circle(canvas, color[i], (x[i], y[i]), r[i])

pygamebg.frame_loop(50, new_frame)
