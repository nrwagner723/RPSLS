from player import Player
import random

class AI(Player):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def randomize_gesture(self):
        self.gesture = self.gesture_list[random.randint(0, 4)]
        print(self.gesture)