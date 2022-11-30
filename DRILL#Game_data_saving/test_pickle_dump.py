import pickle

class NPC:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y

    def show(self):
        print(f'Name:{self.name} @ ({self.x}, {self.y})')

yuri = NPC('yuri', 100, 200)
print(yuri.__dict__)
yuri.show()
with open('npc.pickle', 'wb') as f:
    pickle.dump(yuri, f)