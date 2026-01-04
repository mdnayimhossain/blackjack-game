"""
Main game logic for Blackjack
Handles game flow and rules
"""

from deck import Deck
from hand import Hand
from config import (
    STARTING_BALANCE,
    MINIMUM_BET,
    BLACKJACK_PAYOUT,
    DEALER_STAND_VALUE,
    BLACKJACK_VALUE,
    SEPARATOR_LINE
)
from utils import (
    clear_screen,
    display_welcome,
    display_hands,
    get_bet,
    get_player_choice,
    display_result,
    ask_play_again,
    display_goodbye
)


class BlackjackGame:
    """Main game logic for Blackjack"""
    
    def __init__(self):
        """Initialize the game"""
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_balance = STARTING_BALANCE
        self.current_bet = 0
    
    def deal_initial_cards(self):
        """Deals initial 2 cards to player and dealer"""
        self.player_hand.clear()
        self.dealer_hand.clear()
        
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())
    
    def player_turn(self):
        """
        Handles player's turn
        
        Returns:
            bool: True if player didn't bust, False if bust
        """
        while True:
            display_hands(self.player_hand, self.dealer_hand, hide_dealer_card=True)
            
            if self.player_hand.is_bust():
                print("\n💥 BUST! You went over 21!")
                return False
            
            if self.player_hand.get_value() == BLACKJACK_VALUE:
                print("\n🎉 You have 21!")
                return True
            
            choice = get_player_choice()
            
            if choice == 'h':
                card = self.deck.deal_card()
                self.player_hand.add_card(card)
                print(f"\n📥 You drew: {card}")
            elif choice == 's':
                print("\n✋ You stand.")
                return True
    
    def dealer_turn(self):
        """Handles dealer's turn (automatic)"""
        print("\n" + SEPARATOR_LINE)
        print("🤖 Dealer's turn...")
        print(SEPARATOR_LINE)
        
        display_hands(self.player_hand, self.dealer_hand, hide_dealer_card=False)
        
        while self.dealer_hand.get_value() < DEALER_STAND_VALUE:
            input("\nPress Enter to continue...")
            card = self.deck.deal_card()
            self.dealer_hand.add_card(card)
            print(f"📥 Dealer draws: {card}")
            display_hands(self.player_hand, self.dealer_hand, hide_dealer_card=False)
        
        if self.dealer_hand.is_bust():
            print("\n💥 Dealer BUSTS!")
        else:
            print(f"\n✋ Dealer stands at {self.dealer_hand.get_value()}")
    
    def determine_winner(self):
        """
        Determines winner and adjusts balance
        
        Returns:
            int: Winnings amount
        """
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()
        
        player_blackjack = self.player_hand.is_blackjack()
        dealer_blackjack = self.dealer_hand.is_blackjack()
        
        # Determine outcome
        if player_value > BLACKJACK_VALUE:
            message = "💔 You BUST! Dealer wins!"
            winnings = 0
        elif dealer_value > BLACKJACK_VALUE:
            message = "🎉 Dealer BUSTS! You WIN!"
            winnings = self.current_bet * 2
        elif player_blackjack and not dealer_blackjack:
            message = "🎰 BLACKJACK! You win 3:2!"
            winnings = int(self.current_bet * BLACKJACK_PAYOUT)
        elif dealer_blackjack and not player_blackjack:
            message = "💔 Dealer has BLACKJACK! You lose!"
            winnings = 0
        elif player_value > dealer_value:
            message = "🎉 You WIN!"
            winnings = self.current_bet * 2
        elif player_value < dealer_value:
            message = "💔 Dealer wins!"
            winnings = 0
        else:
            message = "🤝 It's a TIE! Bet returned."
            winnings = self.current_bet
        
        self.player_balance += winnings
        display_result(message, winnings, self.current_bet, self.player_balance)
        
        return winnings
    
    def play_round(self):
        """
        Plays a single round of blackjack
        
        Returns:
            bool: True to continue, False to quit
        """
        # Get bet
        bet = get_bet(self.player_balance, MINIMUM_BET)
        if bet is None:
            return False
        
        self.current_bet = bet
        self.player_balance -= bet
        
        # Shuffle and deal
        self.deck.shuffle()
        self.deal_initial_cards()
        
        # Check for immediate blackjacks
        if self.player_hand.is_blackjack() or self.dealer_hand.is_blackjack():
            display_hands(self.player_hand, self.dealer_hand, hide_dealer_card=False)
            if self.player_hand.is_blackjack():
                print("\n🎰 BLACKJACK!")
            self.determine_winner()
            return True
        
        # Player's turn
        if not self.player_turn():
            display_hands(self.player_hand, self.dealer_hand, hide_dealer_card=False)
            self.determine_winner()
            return True
        
        # Dealer's turn
        self.dealer_turn()
        
        # Determine winner
        self.determine_winner()
        
        return True
    
    def play(self):
        """Main game loop"""
        clear_screen()
        display_welcome(self.player_balance)
        
        while self.player_balance >= MINIMUM_BET:
            if not self.play_round():
                break
            
            if not ask_play_again():
                break
            
            clear_screen()
        
        if self.player_balance < MINIMUM_BET:
            print("\n💸 You don't have enough money to continue!")
        
        display_goodbye(self.player_balance)
