"""
Utility functions for Blackjack game
Contains helper functions for display and input
"""

import os
from config import SEPARATOR_LINE, HIDDEN_CARD_SYMBOL


def clear_screen():
    """Clears the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_welcome(balance):
    """
    Displays welcome message
    
    Args:
        balance (int): Player's current balance
    """
    print(SEPARATOR_LINE)
    print("🎰  WELCOME TO BLACKJACK  🎰".center(50))
    print(SEPARATOR_LINE)
    print(f"\n💰 Your Balance: ${balance}")
    print("\nRules: Get as close to 21 as possible without going over!")
    print("Dealer must hit on 16 and below, stand on 17 and above.\n")


def display_hands(player_hand, dealer_hand, hide_dealer_card=True):
    """
    Displays current hands for player and dealer
    
    Args:
        player_hand (Hand): The player's hand
        dealer_hand (Hand): The dealer's hand
        hide_dealer_card (bool): Whether to hide dealer's second card
    """
    print("\n" + SEPARATOR_LINE)
    
    if hide_dealer_card and len(dealer_hand.cards) > 0:
        print(f"🎴 Dealer's Hand: {dealer_hand.cards[0]}  {HIDDEN_CARD_SYMBOL}")
    else:
        print(f"🎴 Dealer's Hand: {dealer_hand}")
        print(f"   Value: {dealer_hand.get_value()}")
    
    print(f"\n🎴 Your Hand: {player_hand}")
    print(f"   Value: {player_hand.get_value()}")
    print(SEPARATOR_LINE)


def get_bet(balance, minimum_bet):
    """
    Gets bet amount from player with validation
    
    Args:
        balance (int): Player's current balance
        minimum_bet (int): Minimum allowed bet
        
    Returns:
        int or None: Bet amount, or None if player wants to quit
    """
    while True:
        try:
            print(f"💰 Current Balance: ${balance}")
            bet_input = input(f"Place your bet (minimum ${minimum_bet}, or 'q' to quit): ")
            
            if bet_input.lower() == 'q':
                return None
            
            bet = int(bet_input)
            
            if bet < minimum_bet:
                print(f"❌ Minimum bet is ${minimum_bet}!")
            elif bet > balance:
                print("❌ Insufficient funds!")
            else:
                return bet
        except ValueError:
            print("❌ Please enter a valid number!")


def get_player_choice():
    """
    Gets player's choice to hit or stand
    
    Returns:
        str: 'h' for hit or 's' for stand
    """
    while True:
        choice = input("\n[H]it or [S]tand? ").lower()
        if choice in ['h', 's']:
            return choice
        print("❌ Invalid choice! Please enter 'H' or 'S'")


def display_result(message, winnings, bet, new_balance):
    """
    Displays the result of a round
    
    Args:
        message (str): Result message (win/lose/tie)
        winnings (int): Amount won
        bet (int): Amount bet
        new_balance (int): Player's new balance
    """
    print("\n" + SEPARATOR_LINE)
    print("🏆  FINAL RESULTS  🏆".center(50))
    print(SEPARATOR_LINE)
    print(message)
    
    if winnings > 0:
        profit = winnings - bet
        if profit > 0:
            print(f"\n💰 You won ${profit}!")
        else:
            print(f"\n🤝 Your bet of ${bet} was returned!")
    
    print(f"💰 New Balance: ${new_balance}")
    print(SEPARATOR_LINE)


def ask_play_again():
    """
    Asks if player wants to play another round
    
    Returns:
        bool: True if player wants to continue, False otherwise
    """
    choice = input("\nPlay another round? [Y/N]: ").lower()
    return choice == 'y'


def display_goodbye(final_balance):
    """
    Displays goodbye message
    
    Args:
        final_balance (int): Player's final balance
    """
    print("\n" + SEPARATOR_LINE)
    print("👋 Thanks for playing!")
    print(f"💰 Final Balance: ${final_balance}")
    print(SEPARATOR_LINE)
