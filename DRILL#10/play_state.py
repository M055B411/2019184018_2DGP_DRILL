from pico2d import *
import game_framework
import title_state
import item_state
import add_delete_boy

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('animation_sheet.png')
        self.dir = 1

        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')
        self.item = None

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1 * self.dir
        if self.x > 800:
            self.dir = -1
        elif self.x < 0:
            self.dir = 1

    def draw(self):
            if self.dir == -1:
                self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
            elif self.dir == 1:
                self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
            if self.item == 'BigBall':
                self.big_ball_image.draw(self.x+10, self.y+50)
            elif self.item == 'Ball':
                self.ball_image.draw(self.x+10, self.y+50)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
            elif event.key == SDLK_b:
                game_framework.push_state(add_delete_boy)

boy_list = list()
boy = None
grass = None
running = None

# 초기화
def enter():
    global grass, running ,boy_list
    boy_list.append(Boy())
    grass = Grass()
    running = True

# 종료
def exit():
    global boy, grass
    del boy
    del grass

def update():
    for r in boy_list:
        r.update()

def draw_world():
    grass.draw()
    for r in boy_list:
        r.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass


