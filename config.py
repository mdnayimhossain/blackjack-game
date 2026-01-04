"""
Configuration file for Blackjack game
Contains constants and game settings
"""

# Card suits with symbols
SUITS = ['♠', '♥', '♦', '♣']

# Card ranks
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Game settings
STARTING_BALANCE = 1000
MINIMUM_BET = 10
BLACKJACK_PAYOUT = 2.5  # 3:2 payout
DEALER_STAND_VALUE = 17
DEALER_HIT_VALUE = 16
BLACKJACK_VALUE = 21

# Face card values
FACE_CARD_VALUE = 10
ACE_HIGH_VALUE = 11
ACE_LOW_VALUE = 1

# Display settings
HIDDEN_CARD_SYMBOL = '🂠'
SEPARATOR_LINE = "=" * 50
