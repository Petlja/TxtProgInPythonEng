import random, pygame as pg, pygamebg

water = pg.image.load('water.png')
(width, height) = (water.get_width(), water.get_height())
canvas = pygamebg.open_window(width, height, "Drops")
MAX_NUM_DROPS = 50
MARGIN = 30
RAIN_COLOR = (46, 99, 113)
HORIZON_Y = int(height * 0.6)

drops = []

# Each drop is a short vertical line, which descends in each frame.
# It is determined by the upper point (x, y), the end point y_max and the length d.
# When the drop reaches y_max, it disappears.
def new_frame():
    global drops
    new_drops = []
    for i in range(len(drops)):
        x, y, y_max, d = drops[i]
        if y + 20 <= y_max:
            new_drops.append((x, y + 20, y_max, d))
            
    num_drops_added = min(5, MAX_NUM_DROPS - len(drops))
    for _ in range(num_drops_added):
        x, y = random.randint(MARGIN, width - MARGIN), 0
        y_max = random.randint(HORIZON_Y + MARGIN, height - MARGIN)
        d = random.randint(5, 15)
        new_drops.append((x, y, y_max, d))
            
    drops = new_drops
    canvas.blit(water, (0, 0))
    pg.draw.rect(canvas, pg.Color("skyblue"), (0, 0, width, HORIZON_Y)) # sky
    for x, y, y_max, d in drops:
        pg.draw.line(canvas, RAIN_COLOR, (x, y), (x, y+d), 1)

pygamebg.frame_loop(20, new_frame)
