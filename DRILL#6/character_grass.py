from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

while (True):
 
    while x < 800:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x += 2
        delay(0.001)
    while y < 600:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y += 2
        delay(0.001)
    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x -= 2
        delay(0.001)
        
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y -= 2
        delay(0.001)

    while x < 400:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x += 2
        delay(0.001)
        

        
        
    angle = -90
    while angle < 270:
        clear_canvas_now()
        grass.draw_now(400,30)
        ay = (210 * math.sin((angle/ 360 *2)*math.pi)) + 300
        ax = (210 * math.cos((angle/360 *2)*math.pi)) + 400
        character.draw_now(ax,ay)
        angle += 2
        delay(0.001)
        
    
close_canvas()
