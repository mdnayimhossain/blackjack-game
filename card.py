"""
Card class for Blackjack game
Represents a single playing card with suit and rank
"""

from config import FACE_CARD_VALUE, ACE_HIGH_VALUE


class Card:
    """Represents a playing card with suit and rank"""
    
    def __init__(self, suit, rank):
        """
        Initialize a card
        
        Args:
            suit (str): The suit of the card (♠, ♥, ♦, ♣)
            rank (str): The rank of the card (2-10, J, Q, K, A)
        """
        self.suit = suit
        self.rank = rank
    
    def get_value(self):
        """
        Returns the value of the card in Blackjack
        
        Returns:
            int: The numeric value of the card
        """
        if self.rank in ['J', 'Q', 'K']:
            return FACE_CARD_VALUE
        elif self.rank == 'A':
            return ACE_HIGH_VALUE  # Ace starts as 11, adjusted in Hand class if needed
        else:
            return int(self.rank)
    
    def __str__(self):
        """String representation of the card"""
        return f"{self.rank}{self.suit}"
    
    def __repr__(self):
        """Official string representation of the card"""
        return f"Card({self.suit}, {self.rank})"
