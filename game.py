from time import sleep
from human import Human
from ai import AI

class Game:

    def __init__(self):
        self.player_one = Human('Natalie')
        self.player_two = AI('Bot')

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
        number_of_players = input('\nHow many players? Enter [1], [2], or [3] for a surprise: ')
        
    def run_game(self):
        self.display_rules()
        self.how_many_humans()

