"""
Main entry point for Blackjack game
Run this file to start the game
"""

from game import BlackjackGame


def main():
    """Main function to run the game"""
    try:
        game = BlackjackGame()
        game.play()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please report this issue.")


if __name__ == "__main__":
    main()
