from player import Player
import random

class AI(Player):

    def __init__(self, name):
        super().__init__()
        self.name = name