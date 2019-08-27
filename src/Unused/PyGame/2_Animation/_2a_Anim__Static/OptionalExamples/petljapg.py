import pygame as pg
import inspect

pg_is_initialized = False
keys = []

def frames(rate, width=None, height=None, caption=None, event_handler=None):
    global pg_is_initialized
    if pg_is_initialized: #pg.get_init():
        if width is not None:
            raise ValueError("Argument 'width' is not expected when pygame is allready initialized")
        if height is not None:
            raise ValueError("Argument 'height' is not expected when pygame is allready initialized")
        if caption is not None:
            raise ValueError("Argument 'caption' is not expected when pygame is allready initialized")
        surf = None
    else:
        pg.init()
        if width is not None and height is not None:
            # could raise an error if only one of (w, h) is not None
            surf = pg.display.set_mode((width, height))
        else:
            surf = pg.display.set_mode((500,500))
        if caption is not None:
            pg.display.set_caption(caption)
        pg.key.set_repeat(500, 10)  
        pg_is_initialized = True

    sat = pg.time.Clock() 
    kraj = False
    while not kraj:
        for dogadjaj in pg.event.get():
            if dogadjaj.type == pg.QUIT:
                kraj = True
            else:
                if event_handler:
                    event_handler(dogadjaj)
        yield True
        pg.display.update()
        sat.tick(rate)
    if pg_is_initialized:
        pg.quit()

def init(width=None, height=None, caption=None):
    global pg_is_initialized
    pg.init()
    if width is not None:
        surf = pg.display.set_mode((width,height))
    else:
        surf = pg.display.set_mode((500,500))
    if caption is not None:
        pg.display.set_caption(caption)
    pg.key.set_repeat(500, 10)
    pg_is_initialized = True
    return surf

def pause():
    for frm in frames(60):
        pass

def run(rate, process_frame, process_event = None):
    for frm in frames(rate, event_handler = process_event):
        if process_frame:
            process_frame()


