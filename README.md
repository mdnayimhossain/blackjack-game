# 🎰 Blackjack Card Game

A Python-based Blackjack (21) card game with a clean command-line interface.

## Features
- ✅ Standard Blackjack rules
- ✅ Dealer AI (hits on 16, stands on 17)
- ✅ Flexible Ace values (11 or 1)
- ✅ Betting system with balance tracking
- ✅ Natural Blackjack detection (3:2 payout)

## Installation
```bash
git clone https://github.com/YOUR_USERNAME/blackjack-game.git
cd blackjack-game
```

## How to Play
```bash
python main.py
```

## Game Rules
- Get as close to 21 as possible without going over
- Face cards (J, Q, K) = 10 points
- Aces = 11 or 1 (automatically adjusted)
- Dealer must hit on 16 or below, stand on 17 or above

## Project Structure
```
blackjack-game/
├── main.py       # Entry point
├── game.py       # Game logic
├── deck.py       # Deck management
├── card.py       # Card class
├── hand.py       # Hand management
├── utils.py      # Utility functions
└── config.py     # Game configuration
```

## Requirements
- Python 3.6+
- No external dependencies required!

## License
MIT License
