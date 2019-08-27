import random, pygame as pg, pygamebg
(width, height) = (500, 300)
canvas = pygamebg.open_window(width, height, "Balls")

colors = (
    pg.Color("red"), pg.Color("yellow"), pg.Color("blue"),
    pg.Color("cyan"), pg.Color("green"), pg.Color("purple")
)
 
# The ball is determined by position (x, y), displacement (dx, dy), size (r) and color.
def new_ball():
    r = random.randint(10, 30)
    x = random.randint(r, width - r)
    y = random.randint(r, height - r)
    color = random.choice(colors)
    dx, dy = 0, 0
    while dx == 0 and dy == 0: # we don't want the balls that stand still
        dx = random.randint(-8, 8)
        dy = random.randint(-8, 8)
    return (x, y, dx, dy, r, color)


# make a list of 10 balls
balls = []
for _ in range(10):
    balls.append(new_ball())
    
def new_frame():
    global balls
    next_balls = [] # list that will contain the next position of each ball
    for x, y, dx, dy, r, color in balls:
        (x, y) = (x + dx, y + dy)
        if (x+r < 0 or x-r > width or y+r < 0 or y-r > height):
            x, y, dx, dy, r, color = new_ball()
            
        next_balls.append((x, y, dx, dy, r, color))
        
    balls = next_balls
    canvas.fill(pg.Color("darkgray"))
    for x, y, dx, dy, r, color in balls:
        pg.draw.circle(canvas, color, (x, y), r)

pygamebg.frame_loop(50, new_frame)
