import random
from colorama import Fore, Back, Style, init
init()
class RockPaperScissors:
    def __init__(self,):
        self.rock = "rock"
        self.paper = "paper"
        self.Scissors = "Scissors"  
        self.breaking = 0
        self.user_score = 0
        self.PC_score = 0
     
    def draw(self):
        mesg = Fore.WHITE + Style.BRIGHT + "It's a draw." + Style.RESET_ALL
        print(mesg)
        self.user_won = 0
    
    def win(self):
        mesg = Fore.GREEN + Style.BRIGHT + "You won!" + Style.RESET_ALL
        print(mesg)
        self.user_won = 2
    
    def lose(self):
        mesg = Fore.RED + Style.BRIGHT + "You lost!" + Style.RESET_ALL
        print(mesg)
        self.user_won = 1
       
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
                print(Fore.BLUE + Style.BRIGHT + "bye" + Style.RESET_ALL)
                quit()
            else:
                print(Fore.RED + Style.BRIGHT + "Error. This option does not exist, Please try again." + Style.RESET_ALL)
                continue   
        if self.user_input == "rock":
            self.user_input = self.rock
        elif self.user_input == "paper":
            self.user_input = self.paper
        elif self.user_input == "scissors":
            self.user_input = self.Scissors

    def beating(self, user, PC):
        magenta = Fore.MAGENTA + Style.BRIGHT
        reset = Style.RESET_ALL
        if user == self.rock and PC == self.rock:
            PC_choice = magenta + "I chose rock" + reset
            print(PC_choice)
            self.draw()
        elif user == self.rock and PC == self.paper:
            PC_choice = magenta + "I chose paper" + reset
            print(PC_choice)
            self.lose()
        elif user == self.rock and PC == self.Scissors:
            PC_choice = magenta + "I chose Scissors" + reset
            print(PC_choice)
            self.win()
        elif user == self.paper and PC == self.rock:
            PC_choice = magenta + "I chose rock" + reset
            print(PC_choice)
            self.win()
        elif user == self.paper and PC == self.paper:
            PC_choice = magenta + "I chose paper" + reset
            print(PC_choice)
            self.draw()
        elif user == self.paper and PC == self.Scissors:
            PC_choice = magenta + "I chose Scissors" + reset
            print(PC_choice)
            self.lose()
        elif user == self.Scissors and PC == self.rock:
            PC_choice = magenta + "I chose rock" + reset
            print(PC_choice)
            self.lose()
        elif user == self.Scissors and PC == self.paper:
            PC_choice = magenta + "I chose paper" + reset
            print(PC_choice)
            self.win()
        elif user == self.Scissors and PC == self.Scissors:
            PC_choice = magenta + "I chose Scissors" + reset
            print(PC_choice)
            self.draw()
    def claculating(self):
        if self.user_won == 0:
            self.user_score += 1
            self.PC_score += 1 
        elif self.user_won == 1:
            self.PC_score += 1
        elif self.user_won == 2:
            self.user_score += 1
        return f"Your score:{self.user_score} My Score:{self.PC_score}"
        self.user_won = None
    def Final(self):
        while True:
            Random_int =  self.random_selection()
            self.inputing()
            self.beating(self.user_input, Random_int)
            self.result = self.claculating()
            print(Fore.GREEN + Style.BRIGHT + self.result + Style.RESET_ALL)
if __name__ == "__main__":
    game = RockPaperScissors()
    game.Final()

# This code is a simple implementation of the Rock, Paper, Scissors game.
# The user can play against the computer, which randomly selects its choice.
# The game continues until the user decides to exit by typing "done".
# The game provides feedback on whether the user won, lost, or drew.
# to run this game, write : python playthis.py in the terminal. and then press enter.
# The game uses colorama for colored output in the terminal.
