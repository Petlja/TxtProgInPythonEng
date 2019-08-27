import random, pygame as pg, pygamebg
(width, height) = (800, 400)
canvas = pygamebg.open_window(width, height, "Snowflakes")

snowflake_image = pg.image.load("snowflake.png")  # a snowflake image
snowflake_height = snowflake_image.get_height()
num_flakes = 10 # total number of the snowflakes

# randomly generate snowflake positions
snowflakes = []
for i in range(num_flakes):
    x, y = random.randint(0, width), random.randint(0, height)
    snowflakes.append((x, y))

def new_frame():
    global snowflakes

    # move the flakes that have not fallen yet and put them into a new list
    new_flakes = []
    for x, y in snowflakes:
        if y + snowflake_height < height:
            new_flakes.append((x, y+1))
            
    # append the list with new snowflakes, 
    # which are starting to fall from the top of the window
    while len(new_flakes) < num_flakes:
        x, y = random.randint(0, width), random.randint(-snowflake_height, 0)
        new_flakes.append((x, y))
        
    snowflakes = new_flakes
    canvas.fill(pg.Color("white"))    # paint background
    for (x, y) in snowflakes:         # draw all the snowflakes
        canvas.blit(snowflake_image, (x, y))

pygamebg.frame_loop(50, new_frame)
