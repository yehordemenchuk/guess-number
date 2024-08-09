from game import Game

guess_number = Game()

try:
    guess_number.play()

except KeyboardInterrupt:
    print("\nGame were interrupted by user")