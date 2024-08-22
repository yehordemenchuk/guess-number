from game import Game

def main():
    game = Game()

    try:
        game.play()

    except KeyboardInterrupt:
        print("\nGame were interrupted by user")

if __name__ == "__main__":
    main()
