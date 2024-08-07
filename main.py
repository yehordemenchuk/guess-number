from game import Game

try:
    guess_number = Game()

    guess_number.play()

except KeyboardInterrupt:
    print("\nGame were interrupted by user")