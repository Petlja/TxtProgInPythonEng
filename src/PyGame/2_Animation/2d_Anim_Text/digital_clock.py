import pygame as pg, datetime, pygamebg
(width, height) = (200, 200)
canvas = pygamebg.open_window(width, height, "Digital clock")

font = pg.font.SysFont("Arial", 40)     # the font for displaying the text

def new_frame():
    time = datetime.datetime.now()           # determine the current time
    hours = str(time.hour).rjust(2, "0")      # number of hours as string, left-padded with a zero if necessary
    minutes = str(time.minute).rjust(2, "0")  # same for the number of minutes
    seconds = str(time.second).rjust(2, "0") # same for the number of seconds
    
    # build an image of the "time" message
    text_image = font.render(hours + ":" + minutes + ":" + seconds, True, pg.Color("black"))

    # position is determined so that the text is centered in the window
    (x, y) = ((width - text_image.get_width()) // 2, (height - text_image.get_height()) // 2)
    
    canvas.fill(pg.Color("white")) # paint background
    canvas.blit(text_image, (x, y)) # display image of the text

pygamebg.frame_loop(1, new_frame)
