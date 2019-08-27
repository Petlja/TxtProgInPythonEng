import pygame as pg, pygamebg
(width, height) = (400, 300)
canvas = pygamebg.open_window(width, height, "Car")

car_rightwards_image = pg.image.load("car.png") 
# creating flipped image (symmetric with respect to the vertical axis)
car_leftwards_image = pg.transform.flip(car_rightwards_image, True, False)
car_images = (car_rightwards_image, car_leftwards_image)

# car image size
(car_width, car_height) = (car_leftwards_image.get_width(), car_leftwards_image.get_height()) 

fps = 50       # number of frames per second
dt = 1 / fps   # duration of one frame in seconds
car_v = 100   # car speed (pixels per second)
car_dir = 0  # direction - 0 for right, 1 for left (also index of the corresponding car image in the tuple)
(car_x, car_y) = (0, height - car_height) # car position (lower left corner initially)

def new_frame():
    global car_x, car_v, car_dir # will be changing car position, speed and direction
    car_x += car_v * dt    # moving the car
    if car_x > width or car_x < -car_width: 
        # if car has gone out of the canvas to the left or right
        car_dir = 1 - car_dir
        car_v = -car_v
        
    canvas.fill(pg.Color("skyblue"))                 # paint background to sky-blue
    canvas.blit(car_images[car_dir], (car_x, car_y))   # display car image

pygamebg.frame_loop(fps, new_frame)
