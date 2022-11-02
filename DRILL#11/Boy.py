from pico2d import *

#define event
RD, LD, RU, LU, TIMER, AUTO = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): AUTO
}


class IDLE:
    @staticmethod
    def enter(self, event):#Entry Action
        print("Enter IDLE")
        self.dir = 0
        self.timer = 600
        pass

    @staticmethod
    def exit(self):#Exit Action
        print("Exit IDLE")
        pass

    @staticmethod
    def do(self):#Running Action
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)
        pass

    @staticmethod
    def draw(self): #draw
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass

class RUN:
    @staticmethod
    def enter(self, event):  # Entry Action
        print("Enter RUN")
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        pass

    @staticmethod
    def exit(self):  # Exit Action
        print("Exit RUN")
        self.face_dir = self.dir
        pass

    @staticmethod
    def do(self):  # Running Action
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 5
        self.x = clamp(0, self.x, 800)
        pass

    @staticmethod
    def draw(self):  # draw
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass

class SLEEP:
    @staticmethod
    def enter(self, event):#Entry Action
        print("Enter SLEEP")
        self.frame = 0
        pass

    @staticmethod
    def exit(self):#Exit Action
        print("Exit SLEEP")
        pass

    @staticmethod
    def do(self):#Running Action
        self.frame = (self.frame + 1) % 8
        pass

    @staticmethod
    def draw(self): #draw
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592/2, '', self.x + 25, self.y - 35, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592/2, '', self.x + 25, self.y - 35, 100, 100)
        pass

class AUTO_RUN:
    @staticmethod
    def enter(self, event):  # Entry Action
        print("Enter AUTO")
        self.dir = self.face_dir
        pass

    @staticmethod
    def exit(self):  # Exit Action
        print("Exit AUTO")
        self.dir = 0
        pass

    @staticmethod
    def do(self):  # Running Action
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 5
        self.x = clamp(0, self.x, 800)
        if self.x == 800:
            self.dir = -1
        elif self.x == 0:
            self.dir = 1
        pass

    @staticmethod
    def draw(self):  # draw
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y + 30, 200, 200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y + 30, 200, 200)
        pass

#3 state changer
next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AUTO: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, AUTO: AUTO_RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN},
    AUTO_RUN: {RU: IDLE, LU: IDLE, RD: RUN, LD: RUN, AUTO: IDLE}
}




class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)



    def draw(self):
        self.cur_state.draw(self)




    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1