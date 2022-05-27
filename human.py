from player import Player
from time import sleep

class Human(Player):
    
    def __init__(self, name):
        super().__init__()
        self.name = name

    def choose_gesture(self):
        print('\nEnter [0] for Rock')
        sleep(0.2)
        print('Enter [1] for Paper')
        sleep(0.2)
        print('Enter [2] for Scissors')
        sleep(0.2)
        print('Enter [3] for Lizard')
        sleep(0.2)
        print('Enter [4] for Spock')
        sleep(0.2)
        self.gesture = int(input('\nChoose your gesture: '))

pla = Human('natalie')
pla.choose_gesture()