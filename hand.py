"""
Hand class for Blackjack game
Represents a hand of cards for player or dealer
"""

from config import BLACKJACK_VALUE, ACE_LOW_VALUE


class Hand:
    """Represents a hand of cards for player or dealer"""
    
    def __init__(self):
        """Initialize an empty hand"""
        self.cards = []
    
    def add_card(self, card):
        """
        Adds a card to the hand
        
        Args:
            card (Card): The card to add to the hand
        """
        self.cards.append(card)
    
    def get_value(self):
        """
        Calculates total value of hand, adjusting for Aces
        
        Returns:
            int: The total value of the hand
        """
        value = sum(card.get_value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'A')
        
        # Adjust for Aces if busting (convert from 11 to 1)
        while value > BLACKJACK_VALUE and aces > 0:
            value -= (card.get_value() - ACE_LOW_VALUE) if card.rank == 'A' else 0
            value -= 10  # Reduce by 10 (difference between 11 and 1)
            aces -= 1
        
        return value
    
    def is_blackjack(self):
        """
        Checks if hand is a natural blackjack (21 with first 2 cards)
        
        Returns:
            bool: True if natural blackjack, False otherwise
        """
        return len(self.cards) == 2 and self.get_value() == BLACKJACK_VALUE
    
    def is_bust(self):
        """
        Checks if hand value exceeds 21
        
        Returns:
            bool: True if bust, False otherwise
        """
        return self.get_value() > BLACKJACK_VALUE
    
    def clear(self):
        """Clears all cards from the hand"""
        self.cards = []
    
    def __str__(self):
        """String representation of the hand"""
        return ' '.join(str(card) for card in self.cards)
    
    def __len__(self):
        """Returns the number of cards in the hand"""
        return len(self.cards)
    
    def __repr__(self):
        """Official string representation of the hand"""
        return f"Hand({self.cards})"
