from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 40.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1, dir = 1):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0
        self.dir = dir

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw((int(self.frame) % 5) * 184, (int(self.frame) // 5) * 168, 180, 168, 0, 'h', self.x, self.y, 183, 168)
        elif self.dir == 1:
            self.image.clip_draw((int(self.frame) % 5) * 184, (int(self.frame) // 5) * 168, 180, 168, self.x, self.y)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * self.velocity * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 1600:
            self.dir = -1
        elif self.x < 0:
            self.dir = 1
