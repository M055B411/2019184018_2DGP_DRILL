from pico2d import *

open_canvas()

background = load_image('background.png')
character = load_image('character.png')

def idle_anim():
    y = 1
    print("IDLE")
    for frame in range(0, 4, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(frame * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        delay(0.15)
        get_events()

def running_anim():
    print("RUNNING")
    y = 1
    for frame in range(0, 8, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 4) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        if (frame+4 % 10)==9:
            y += 1
        delay(0.15)
        get_events()

def dash_anim():
    print("DASH")
    y = 2
    for frame in range(0, 2, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame+2) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        delay(0.15)
        get_events()

def defend_anim():
    print("DEFEND")
    y = 2
    for frame in range(0, 3, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 4) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        if(frame+4) % 10 == 5:
            delay(0.5)
        else:
            delay(0.15)
        get_events()

def jump_anim():
    print("JUMP")
    y = 2
    for frame in range(0, 3, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame+7) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        delay(0.15)
        get_events()

def landing_anim():
    print("LANDING")
    y= 3
    for frame in range(0, 5, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw((frame % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        delay(0.15)
        get_events()

def hit_anim1():
    print("HIT_1")
    y = 3
    for frame in range(0, 6, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame+6) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        if ((frame+6) % 10) == 9:
            y += 1
        delay(0.15)
        get_events()

def hit_anim2():
    print("HIT_2")
    y = 4
    for frame in range(0, 9, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 2) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        delay(0.15)
        get_events()

def hanging_anim():
    print("HANGING")
    y = 5
    for frame in range(0, 3, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 1) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        if (frame % 10) == 9:
            y += 1
        delay(0.15)
        get_events()

def cliffjump_anim():
    print("CLIFF_JUMP")
    y = 5
    for frame in range(0, 13, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 4) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        if (frame + 4 % 10) == 9:
            y += 1
        delay(0.15)
        get_events()

def highjump_anim():
    print("HIGH_JUMP")
    y = 6
    for frame in range(0, 6, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 8) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        if (frame + 8 % 10) == 9:
            y += 1
        delay(0.15)
        get_events()

def win_anim():
    print("WIN")
    y = 7
    for frame in range(0, 11, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 4) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        if (frame + 4 % 10) == 9:
            y += 1
        delay(0.15)
        get_events()

def defeat_anim():
    print("DEFEAT")
    y = 8
    for frame in range(0, 4, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 5) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        delay(0.15)
        get_events()

def standattack_anim():
    print("STAND_ATTACK")
    y = 8
    for frame in range(0, 6, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 9) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        if ((frame + 9) % 10) == 9:
            y += 1
        delay(0.15)
        get_events()

def dashattack_anim():
    print("DASH_ATTACK")
    y = 9
    for frame in range(0, 6, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 5) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        if ((frame + 5) % 10) == 9:
            y += 1
        delay(0.15)
        get_events()

def heavyattack_anim():
    print("HEAVY_ATTACK")
    y = 10
    for frame in range(0, 8, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 1) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        delay(0.15)
        get_events()

def throw_anim():
    print("THROW")
    y = 10
    for frame in range(0, 11, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 8) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        if ((frame + 8) % 10) == 9:
            y += 1
        delay(0.15)
        get_events()
        
def upperatt_anim():
    print("UPPERCUT")
    y = 11
    for frame in range(0, 8, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 9) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        if ((frame + 9) % 10) == 9:
            y += 1
        delay(0.15)
        get_events()

def highupper_anim():
    print("HIGH_UPPERCUT")
    y = 12
    for frame in range(0, 10, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 7) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        if ((frame + 7) % 10) == 9:
            y += 1
        delay(0.15)
        get_events()

def loweratt_anim():
    print("LOWER_ATTACK")
    y = 13
    for frame in range(0, 9, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 7) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        if ((frame + 7) % 10) == 9:
            y += 1
        delay(0.15)
        get_events()

def heavylower_anim():
    print("HEAVY_LOWER_ATTACK")
    y = 14
    for frame in range(0, 10, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 6) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        if ((frame + 6) % 10) == 9:
            y += 1
        delay(0.15)
        get_events()

def onairatt_anim():
    print("ON_AIR_ATTACK")
    y = 15
    for frame in range(0, 7, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 6) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        if ((frame + 6) % 10) == 9:
            y += 1
        delay(0.15)
        get_events()

def heavyonair_anim():
    print("ON_AIR_HEAVY_ATTACK")
    y = 16
    for frame in range(0, 6, 1):
        clear_canvas()
        background.draw(400,300)
        character.clip_draw(((frame + 4) % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        delay(0.15)
        get_events()

def all_anim(): #높이 확인용
    frame, y = 0, 1
    while True:
        clear_canvas()
        background.draw(400,300)
        character.clip_draw((frame % 10) * 178,2356 - 108 * y, 178, 108, 400, 300)
        update_canvas()
        frame += 1
        if (frame % 10) == 9:
            y += 1
        if (y == 17 and (frame % 10) == 5):
            break;
        delay(0.2)
        get_events()

while (True):
    idle_anim()
    running_anim()
    dash_anim()
    defend_anim()
    jump_anim()
    landing_anim()
    hit_anim1()
    hit_anim2()
    hanging_anim()
    cliffjump_anim()
    highjump_anim()
    win_anim()
    defeat_anim()
    standattack_anim()
    dashattack_anim()
    heavyattack_anim()
    throw_anim()
    upperatt_anim()
    highupper_anim()
    loweratt_anim()
    heavylower_anim()
    onairatt_anim()
    heavyonair_anim()
    #all_anim()


close_canvas()



