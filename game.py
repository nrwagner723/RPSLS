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
        self.number_of_players = int(input('\nHow many players? Enter [1] or [2]: '))
        if self.number_of_players == 2:
            self.player_two = Human('Mandy')


    def play(self):
        while self.player_one.wins < 2 and self.player_two.wins < 2:
            print(f'\n{self.player_one.name}\'s turn:')
            self.player_one.choose_gesture()
            print(f'\n{self.player_two.name}\'s turn:')
            self.player_two.choose_gesture()
            if self.player_one.gesture == self.player_two.gesture:
                print(f'\n{self.player_one.name} chose {self.player_one.gesture}\n\n{self.player_two.name} chose {self.player_two.gesture}\n\nIt\'s a tie!\n\n\n')
            elif self.player_one.gesture == 'Rock' and ((self.player_two.gesture == 'Lizard') or (self.player_two.gesture == 'Scissors')):
                print(f'\n{self.player_one.name} chose {self.player_one.gesture}\n\n{self.player_two.name} chose {self.player_two.gesture}\n\n{self.player_one.name} wins!\n\n\n')
                self.player_one.wins += 1
            elif self.player_one.gesture == 'Paper' and ((self.player_two.gesture == 'Rock') or (self.player_two.gesture == 'Spock')):
                print(f'\n{self.player_one.name} chose {self.player_one.gesture}\n\n{self.player_two.name} chose {self.player_two.gesture}\n\n{self.player_one.name} wins!\n\n\n')
                self.player_one.wins += 1
            elif self.player_one.gesture == 'Scissors' and ((self.player_two.gesture == 'Paper') or (self.player_two.gesture == 'Lizard')):
                print(f'\n{self.player_one.name} chose {self.player_one.gesture}\n\n{self.player_two.name} chose {self.player_two.gesture}\n\n{self.player_one.name} wins!\n\n\n')
                self.player_one.wins += 1
            elif self.player_one.gesture == 'Lizard' and ((self.player_two.gesture == 'Paper') or (self.player_two.gesture == 'Spock')):
                print(f'\n{self.player_one.name} chose {self.player_one.gesture}\n\n{self.player_two.name} chose {self.player_two.gesture}\n\n{self.player_one.name} wins!\n\n\n')
                self.player_one.wins += 1
            elif self.player_one.gesture == 'Spock' and ((self.player_two.gesture == 'Scissors') or (self.player_two.gesture == 'Rock')):
                print(f'\n{self.player_one.name} chose {self.player_one.gesture}\n\n{self.player_two.name} chose {self.player_two.gesture}\n\n{self.player_one.name} wins!\n\n\n')
                self.player_one.wins += 1
            elif self.player_two.gesture == 'Rock' and ((self.player_one.gesture == 'Lizard') or (self.player_one.gesture == 'Scissors')):
                print(f'\n{self.player_one.name} chose {self.player_one.gesture}\n\n{self.player_two.name} chose {self.player_two.gesture}\n\n{self.player_two.name} wins!\n\n\n') 
                self.player_two.wins += 1
            elif self.player_two.gesture == 'Paper' and ((self.player_one.gesture == 'Rock') or (self.player_one.gesture == 'Spock')):
                print(f'\n{self.player_one.name} chose {self.player_one.gesture}\n\n{self.player_two.name} chose {self.player_two.gesture}\n\n{self.player_two.name} wins!\n\n\n') 
                self.player_two.wins += 1
            elif self.player_two.gesture == 'Scissors' and ((self.player_one.gesture == 'Paper') or (self.player_one.gesture == 'Lizard')):
                print(f'\n{self.player_one.name} chose {self.player_one.gesture}\n\n{self.player_two.name} chose {self.player_two.gesture}\n\n{self.player_two.name} wins!\n\n\n') 
                self.player_two.wins += 1
            elif self.player_two.gesture == 'Lizard' and ((self.player_one.gesture == 'Paper') or (self.player_one.gesture == 'Spock')):
                print(f'\n{self.player_one.name} chose {self.player_one.gesture}\n\n{self.player_two.name} chose {self.player_two.gesture}\n\n{self.player_two.name} wins!\n\n\n') 
                self.player_two.wins += 1
            elif self.player_two.gesture == 'Spock' and ((self.player_one.gesture == 'Scissors') or (self.player_one.gesture == 'Rock')):
                print(f'\n{self.player_one.name} chose {self.player_one.gesture}\n\n{self.player_two.name} chose {self.player_two.gesture}\n\n{self.player_two.name} wins!\n\n\n') 
                self.player_two.wins += 1

    def display_winner(self):
        if self.player_one.wins == 2:
            print(f'\n{self.player_one.name} has won the game!\n')
        elif self.player_two.wins == 2:
            print(f'\n{self.player_two.name} has won the game!\n')

    def run_game(self):
        self.display_rules()
        self.how_many_humans()
        self.play()
        self.display_winner()

