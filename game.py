from random import randrange
from enum import Enum

class Game_state(Enum):
    LOOSE = 0
    WON = 1

class Game_difficulty(Enum):
    LOW = 0
    MIDDLE = 1
    HARDCORE = 2

class Game:
    __name = "Guess number"

    __possible_generation_regimes = [21, 51, 101]
    
    __possible_attempts_counts = [range(10), range(8), range(5)]

    def __init__(self):
        self.__game_state = Game_state.LOOSE

        self.__secret_number = 0

        self.__difficulty = Game_difficulty.LOW

        self.__attempts_count = range(0)

    def set_game_state(self, game_state): self.__game_state = game_state

    def is_game_won(self) -> int: return self.__game_state.value

    def set_difficulty(self):
        user_choice = ""

        while (user_choice != "0" and user_choice != "1" and user_choice != "2"):
            user_choice = input("Enter a difficulty(0-low/1-middle/2-hardcore): ")

        self.__difficulty = Game_difficulty(int(user_choice))

    def get_difficulty(self) -> Game_difficulty: return self.__difficulty
    
    def set_secret_number(self): 
        self.__secret_number = randrange(self.__possible_generation_regimes[self.__difficulty.value])

    def get_secret_number(self) -> int: return self.__secret_number

    def set_attempts_count(self):
        self.__attempts_count = self.__possible_attempts_counts[self.__difficulty.value]
    
    def get_attempts_count(self) -> range: return self.__attempts_count

    def __str__(self) -> str:
        return f"---{self.__name}---\nRules: try guess my number :)"

    def run(self):
        print("Welcome to game \"Guess number\"")

        self.set_difficulty()

        self.set_secret_number()

        self.set_attempts_count()

        attempts_count = self.__attempts_count

        for _ in attempts_count:
            user_guess = ""

            while user_guess.isdigit() == False:
                user_guess = input("Enter a random number: ")

            if int(user_guess) > self.__secret_number:
                print("No my number is smaller.")

            elif int(user_guess) < self.__secret_number:
                print("No my number is bigger")
            
            else:
                print("You guess!!!")

                self.set_game_state(Game_state.WON)

                break
        
        if self.is_game_won():
            print("You won, great!!!")

        else:
            print(f"You loose :(. My number was {self.__secret_number}")
    
    def play(self):
        while True:
            self.run()

            user_choice = ""

            while user_choice != "yes" and user_choice != "no":
                user_choice = input("Do you want to continue(yes/no): ")
            
            if user_choice == "no":
                break

            self.set_game_state(Game_state.LOOSE)
        
        print("Thank you for playing game!!!")