"""
Deck class for Blackjack game
Manages a standard 52-card deck
"""

import random
from card import Card
from config import SUITS, RANKS


class Deck:
    """Represents a deck of 52 playing cards"""
    
    def __init__(self):
        """Initialize a new deck of cards"""
        self.cards = []
        self.build_deck()
    
    def build_deck(self):
        """Creates a standard 52-card deck"""
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
    
    def shuffle(self):
        """Shuffles the deck randomly"""
        random.shuffle(self.cards)
    
    def deal_card(self):
        """
        Deals a single card from the deck
        If deck is empty, rebuilds and shuffles
        
        Returns:
            Card: A card object from the deck
        """
        if len(self.cards) == 0:
            print("♻️  Reshuffling deck...")
            self.build_deck()
            self.shuffle()
        return self.cards.pop()
    
    def cards_remaining(self):
        """
        Returns the number of cards remaining in the deck
        
        Returns:
            int: Number of cards left
        """
        return len(self.cards)
    
    def __len__(self):
        """Returns the number of cards in the deck"""
        return len(self.cards)
    
    def __str__(self):
        """String representation of the deck"""
        return f"Deck with {len(self.cards)} cards remaining"
