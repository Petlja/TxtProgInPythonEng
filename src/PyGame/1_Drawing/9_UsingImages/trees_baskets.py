# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(800, 600, "Apples")

# -*- acsection: main -*-

tree_image = pg.image.load("tree.png")  # image of a tree
basket_image = pg.image.load("basket.png")  # image of a basket
tree_positions = ((200, 70), (120, 150), (240, 290), (550, 170), (400, 200))

canvas.fill(pg.Color("darkgreen")) # paint background
for tree_x, tree_y in tree_positions:
    basket_x = tree_x  + tree_image.get_width() - basket_image.get_width()
    basket_y = tree_y + tree_image.get_height() - basket_image.get_height()
    canvas.blit(tree_image, (tree_x, tree_y))
    canvas.blit(basket_image, (basket_x, basket_y))
    
# -*- acsection: after-main -*-
pygamebg.wait_loop()
