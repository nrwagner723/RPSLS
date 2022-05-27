class Player:
    
    def __init__(self):
        self.gesture = ''
        self.wins = 0
        self.gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    def gesture_choice(self, choice):
        if choice == 0:
            self.gesture = self.gesture_list[0]
        elif choice == 1:
            self.gesture = self.gesture_list[1]
        elif choice == 2:
            self.gesture = self.gesture_list[2]
        elif choice == 3:
            self.gesture = self.gesture_list[3]
        elif choice == 4:
            self.gesture =  self.gesture_list[4]
