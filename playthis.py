import random
from colorama import Fore, Back, Style, init
init()
class RockPaperScissors:
    def __init__(self,):
        self.rock = "rock"
        self.paper = "paper"
        self.Scissors = "Scissors"  
        self.breaking = 0
    def draw(self):
        mesg = "It's a draw."
        print(mesg)
        
    def win(self):
        mesg = "You won!"
        print(mesg)
        
    def lose(self):
        mesg = "You lost!"
        print(mesg)
        
    def random_selection(self):
        global list_class  
        list_class = [self.rock, self.paper, self.Scissors]
        self.randomized = random.choice(list_class)
        return self.randomized
    def inputing(self):
        while True:
            self.user_input = input(Fore.BLUE + Style.BRIGHT + "Your choice(rock/paper/scissors):" + Style.RESET_ALL)
            if self.user_input in list_class:
                break
            elif self.user_input == "done":
                print("bye")
                quit()
            else:
                print(Fore.RED + Style.BRIGHT + "Error. This option does not excist, Please try again." + Style.RESET_ALL)
                continue   
        if self.user_input == "rock":
            self.user_input = self.rock
        elif self.user_input == "paper":
            self.user_input = self.paper
        elif self.user_input == "scissors":
            self.user_input = self.Scissors

    def beating(self, user, PC):
        if user == self.rock and PC == self.rock:
            PC_choice = "I chose rock"
            print(PC_choice)
            self.draw()
        elif user == self.rock and PC == self.paper:
            PC_choice ="I chose paper"
            print(PC_choice)
            self.lose()
        elif user == self.rock and PC == self.Scissors:
            PC_choice ="I chose Scissors"
            print(PC_choice)
            self.win()
        elif user == self.paper and PC == self.rock:
            PC_choice = "I chose rock"
            print(PC_choice)
            self.win()
        elif user == self.paper and PC == self.paper:
            PC_choice ="I chose paper"
            print(PC_choice)
            self.draw()
        elif user == self.paper and PC == self.Scissors:
            PC_choice ="I chose Scissors"
            print(PC_choice)
            self.lose()
        elif user == self.Scissors and PC == self.rock:
            PC_choice = "I chose rock"
            print(PC_choice)
            self.lose()
        elif user == self.Scissors and PC == self.paper:
            PC_choice ="I chose paper"
            print(PC_choice)
            self.win()
        elif user == self.Scissors and PC == self.Scissors:
            PC_choice ="I chose Scissors"
            print(PC_choice)
            self.draw()
    def Final(self):
        while True:
            Random_int =  self.random_selection()
            self.inputing()
            self.beating(self.user_input, Random_int)
if __name__ == "__main__":
    game = RockPaperScissors()
    game.Final()
# This code is a simple implementation of the Rock, Paper, Scissors game.
# The user can play against the computer, which randomly selects its choice.
# The game continues until the user decides to exit by typing "done".
# The game provides feedback on whether the user won, lost, or drew.
# to run this game, write : python playthis.py in the terminal. and then press enter.

