from random import randrange
from enum import Enum

class Game_state(Enum):
    NOT_WON = 0
    WON = 1

class Game_difficulty(Enum):
    LOW = 0
    MIDDLE = 1
    HARDCORE = 2

class Game:
    __name = "Guess number"

    __possible_secret_number_upper_bounds = [21, 51, 101]
    
    __possible_attempts_counts = [range(10), range(8), range(5)]

    def __init__(self):
        self.__game_state = Game_state.NOT_WON

        self.__difficulty = Game_difficulty.LOW

        self.__secret_number = 0

        self.__attempts_count = range(0)

    def set_game_state(self, game_state): self.__game_state = game_state

    def is_game_won(self) -> int: return self.__game_state.value

    def set_difficulty(self):
        user_choice = ""

        while (user_choice != "0" and user_choice != "1" and user_choice != "2"):
            user_choice = input("Enter a difficulty(0-low/1-middle/2-hardcore): ")

        self.__difficulty = Game_difficulty(int(user_choice))

    def set_secret_number(self): 
        self.__secret_number = randrange(self.__possible_secret_number_upper_bounds[self.__difficulty.value])

    def set_attempts_count(self):
        self.__attempts_count = self.__possible_attempts_counts[self.__difficulty.value]

    def __str__(self) -> str:
        return f"---{self.__name}---\nRules: try guess my number :)"

    def run(self):
        self.set_difficulty()

        self.set_secret_number()

        self.set_attempts_count()

        attempts_count = self.__attempts_count

        print()

        for _ in attempts_count:
            user_guess = ""

            while not user_guess.isdigit():
                user_guess = input("Enter a random number: ")
                
            user_guess_value = int(user_guess)

            if user_guess_value > self.__secret_number:
                print("No my number is smaller.")

            elif user_guess_value < self.__secret_number:
                print("No my number is bigger")
            
            else:
                print("\nYou guess!!!")

                self.set_game_state(Game_state.WON)

                break
        
        if self.is_game_won():
            print("\nYou won, great!!!\n")

        else:
            print(f"\nYou loose :(. My number was {self.__secret_number}\n")
    
    def play(self):
        print("Welcome to game \"Guess number\"\n")

        while True:
            self.run()

            user_choice = ""

            while user_choice != "yes" and user_choice != "no":
                user_choice = input("Do you want to continue(yes/no): ")

                user_choice = user_choice.lower()
            
            if user_choice == "no":
                break

            self.set_game_state(Game_state.NOT_WON)

            print()
        
        print("\nThank you for playing game!!!")