from game import Game

game = Game()

try:
    game.play()

except KeyboardInterrupt:
    print("\nGame were interrupted by user")