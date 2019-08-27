import random, pygame as pg, pygamebg

water = pg.image.load('water.png')
(width, height) = (water.get_width(), water.get_height())
canvas = pygamebg.open_window(width, height, "Rain")
water = pg.image.load('water.png')
MAX_NUM_DROPS = 50
MARGIN = 30
RAIN_COLOR = (46, 99, 113)
HORIZON_Y = int(height * 0.6)

drops = []
rings = []

def update_drops_and_rings(drops, rings):
    new_drops = []
    new_rings = []

    # move the drops down
    for i in range(len(drops)):
        x, y, y_max, d = drops[i]
        if y + 20 <= y_max:
            new_drops.append((x, y + 20, y_max, d))
        else:
            new_rings.append((x, y_max, 10, 4*d))
            
    # add new drops
    num_drops_added = min(5, MAX_NUM_DROPS - len(drops))
    for _ in range(num_drops_added):
        x, y = random.randint(MARGIN, width - MARGIN), 0
        y_max = random.randint(HORIZON_Y + MARGIN, height - MARGIN)
        d = random.randint(5, 15)
        new_drops.append((x, y, y_max, d))

    # increase the rings
    for i in range(len(rings)):
        x, y, r, r_max = rings[i]
        r += 5
        if r < r_max:
            new_rings.append((x, y, r, r_max))

    return new_drops, new_rings

def new_frame():
    global drops, rings
    drops, rings = update_drops_and_rings(drops, rings)
    
    canvas.blit(water, (0, 0))
    pg.draw.rect(canvas, pg.Color("skyblue"), (0, 0, width, HORIZON_Y)) # sky
    
    # draw the drops
    for x, y, y_max, d in drops:
        pg.draw.line(canvas, RAIN_COLOR, (x, y), (x, y+d), 1)

    # draw the rings
    for x, y, r, r_max in rings:
        ra, rb = r, r/3
        pg.draw.ellipse(canvas, RAIN_COLOR, (x-ra, y-rb, 2*ra, 2*rb), 1)

pygamebg.frame_loop(20, new_frame)
