import random, pygame as pg, pygamebg
(width, height) = (500, 300)
canvas = pygamebg.open_window(width, height, "Stars")
cx, cy = width // 2, height // 2

# A star is determined by its position (x, y) and size (r).
def new_star():
    r = random.randint(1, 3)
    x = random.randint(r, width - r)
    y = random.randint(r, height - r)
    return (x, y, r)

# Create a list of stars.
num_stars = 40
stars = []
for _ in range(num_stars):
    stars.append(new_star())
    
def new_frame():
    global stars
    next_stars = [] # list that will contain the next state
    for x, y, r in stars:
        x += 0.01 * (x-cx) # x moves away from the center of the window
        y += 0.01 * (y-cy) # y moves away from the center of the window
        r *= 1.01          # we see the star as bigger because we are "approaching"
        # if at least part of the star is in the window, we'll keep it
        if (x+r > 0 and x-r < width and y+r > 0 and y-r < height):
            next_stars.append((x, y, r))
            
    while len(next_stars) < num_stars:
        next_stars.append(new_star())

    stars = next_stars
    canvas.fill(pg.Color("black"))
    for x, y, r in stars:
        ix, iy, ir = int(x), int(y), int(r)
        pg.draw.circle(canvas, pg.Color('white'), (ix, iy), ir)

pygamebg.frame_loop(60, new_frame)
