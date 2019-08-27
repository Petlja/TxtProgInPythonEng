# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(800, 600, "Apples")

# -*- acsection: main -*-
tree_image = pg.image.load("tree.png")  # image of a tree
apple_image = pg.image.load("apple_small.png")  # image of an apple
basket_image = pg.image.load("basket.png")  # image of a basket
apples_on_tree_positions = ((43,191), (61, 158), (124, 145), (134, 175), (160, 180))
apples_in_basket_positions = ((15, 38), (60, 41), (22, 43), (49, 45), (34, 48))
tree_positions = ((200, 70), (120, 150), (240, 290), (550, 170), (400, 200))

def tree_basket_apples(tree_x, tree_y):
    basket_x = tree_x  + tree_image.get_width() - basket_image.get_width()
    basket_y = tree_y + tree_image.get_height() - basket_image.get_height()
    canvas.blit(tree_image, (tree_x, tree_y))
    canvas.blit(basket_image, (basket_x, basket_y))
    for x, y in apples_on_tree_positions:
        canvas.blit(apple_image, (tree_x + x, tree_y + y))
    for x, y in apples_in_basket_positions:
        canvas.blit(apple_image, (basket_x + x, basket_y + y))
    
canvas.fill(pg.Color("darkgreen"))
for tree_x, tree_y in tree_positions:
    tree_basket_apples(tree_x, tree_y)
    
# -*- acsection: after-main -*-
pygamebg.wait_loop()
