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
        self.num = int(input('\nChoose your gesture: '))
        if (self.num == 0) or (self.num == 1) or (self.num == 2) or (self.num == 3) or (self.num == 4):
            self.gesture = self.gesture_list[self.num]   
        else:
            print('Please enter a valid response')
            self.num = int(input('\nChoose your gesture: '))
            self.gesture = self.gesture_list[self.num]     

