from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def render_ALL(x, y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)

def run_RECT():
    print("RECTANGLE")
    x, y = 400, 90

    #bottom 1
    for x in range (400, 780, 10):
        render_ALL(x, y)
        delay(0.01)

    #right
    for y in range (90, 560, 10):
        render_ALL(x, y)
        delay(0.01)

    #upper
    for x in range (780, 20, -10):
        render_ALL(x, y)
        delay(0.01)

    #left
    for y in range (560, 80, -10):
        render_ALL(x, y)
        delay(0.01)


    #bottom 2
    for x in range (20, 400, 10):
        render_ALL(x, y)
        delay(0.01)

def run_CIRCLE():
    print ("CIRCLE")
    cx, cy, r = 400, 300, 210
    for deg in range(0, 360, 5):
        x = cx + r * math.cos((deg-90)/360 * 2 * math.pi)
        y = cy + r * math.sin((deg-90)/360 * 2 * math.pi)
        render_ALL(x,y)
    pass



while (True):
    run_RECT()
    run_CIRCLE()
    #break;
    
        
    
close_canvas()
