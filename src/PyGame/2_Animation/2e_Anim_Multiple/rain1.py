import random, pygame as pg, pygamebg

water = pg.image.load('water.png')
(width, height) = (water.get_width(), water.get_height())
canvas = pygamebg.open_window(width, height, "Rings")
MARGIN = 30
RAIN_COLOR = (46, 99, 113)

# Each ring is described by a tuple (x, y, r, r_max), where
# (x, y) is the center of the ring, r is the ring size that grows
# in each frame, and when r reaches r_max, the ring disappears.
def new_ring():
    x = random.randint(MARGIN, width - MARGIN)
    y = random.randint(MARGIN, height - MARGIN)
    r0 = 10
    r_max = random.randint(2, 5) * 10
    return (x, y, r0, r_max)

rings = []
for _ in range(20):
    rings.append(new_ring())
    
def new_frame():
    global rings
    for i in range(len(rings)):
        x, y, r, r_max = rings[i]
        if r > r_max:
            rings[i] = new_ring()
        else:
            rings[i] = (x, y, r + 10, r_max)
        
    canvas.blit(water, (0, 0))
    for ring in rings:
        x, y, r, r_max = ring
        ra, rb = r, r/3
        pg.draw.ellipse(canvas, RAIN_COLOR, (x-ra, y-rb, 2*ra, 2*rb), 1)

pygamebg.frame_loop(10, new_frame)
