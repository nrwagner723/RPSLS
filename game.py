from time import sleep

class Game:

    def __init__(self):
        pass

    def display_rules(self):
        print('\nWelcome to Rock Paper Scissors Lizard Spock\n\nYou have to win 2 out of 3 rounds to win the game\nUse the number keys to enter your choices')
        sleep(0.2)
        print('\nHere\'s how it works:\n')
        sleep(0.2)
        print('Scissors cut Paper')
        sleep(0.2)
        print('Paper covers Rock')
        sleep(0.2)
        print('Rock crushes Lizard')
        sleep(0.2)
        print('Lizard poisons Spock')
        sleep(0.2)
        print('Spock smahes Scissors')
        sleep(0.2)
        print('Scissors decapitates Lizard')
        sleep(0.2)
        print('Lizard eats Paper')
        sleep(0.2)
        print('Paper disproves Spock')
        sleep(0.2)
        print('Spock vaporizes Rock')
        sleep(0.2)
        print('Rock crushes Scissors')

    def how_many_humans(self):
        number_of_players = input('How many players? Enter [1], [2], or [3] for a surprise ')
        self.players = number_of_players

    def choose_gesture(self):
        gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        print('[0] for Rock')
        sleep(0.2)
        print('[1] for Paper')
        sleep(0.2)
        print('[2] for Scissors')
        sleep(0.2)
        print('[3] for Lizard')
        sleep(0.2)
        print('[4] for Spock')
        sleep(0.2)
        gesture = input('\nChoose your gesture: ')
        self.gesture = gesture

test = Game()
test.display_rules()
test.choose_gesture()