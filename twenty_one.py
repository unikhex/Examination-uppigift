import random

class Twentyone:
    def __init__(self):
        """
        Defines the card deck. 
        """
        self.ui_width = 50
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
        self.ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        self.values = {
            'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 11, 'King': 12, 'Ace': 14,
          '2': 2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10
          }
        
        self.initial_deck = self.create_deck()
        self.dealer_hand = [self.draw_card(), self.draw_card()]
        self.player_hand = [self.draw_card(), self.draw_card()]

    def print_separator(self, char='-'):
        print(char * self.ui_width)

    def print_centered_text(self, text, char='-'):
        formatted_text = f'{char} {text} {char}'
        print(formatted_text.center(self.ui_width))

# Function to create a new deck
    def create_deck(self):
        """
        Goes into self.rank and self.suit which ressults in the player getting a random first card.
        """
        deck = [{'rank': rank, 'suit': suit} for rank in self.ranks for suit in self.suits]
        random.shuffle(deck)
        return deck
    
    def draw_card(self):
        """
        This is a function that removes the initial card gotten from the deck.
        Thus allowing a more realistic play.
        """
        return self.initial_deck.pop()
    
    def calculate_hand_value(self,hand):
        """
        It checks the value of the player's hand and the dealers hand by going into self.value array and
        cross checks the value with the value's rank. Then it adds them
        """
        total_value = sum(self.values[card['rank']] for card in hand)
        num_aces = sum(1 for card in hand if card['rank'] == 'Ace')
        while total_value > 21 and num_aces > 0: 
            """
            Automatically checks value of a hand and if you currently have an ace or more than one ace and subtracts their value if neccesssary.
            """
            total_value -=14
            num_aces -= 1
        return total_value
    def play(self):
        self.print_separator()
        self.print_centered_text('TWENTY ONE GAME')
        self.print_separator
    
        underStand = input("Do you know the rules of playing Twenty One?(yes/no) ").lower()
        if underStand == "no":
            print("\nRules of Twenty One:")
            print("1. The goal is to beat the dealer without going over 21.")
            print("2. You can 'hit' to draw more cards or 'stand' to keep your current total.")
            print("3. Face cards are worth 10, Aces are worth 14 (or 1 if it helps you).")
            print("4. If you go over 21, you lose ('bust').")
            print("5. The dealer must hit until they have 17 or higher.")
            print("6. If the dealer and you have the same value at the end, the dealer wins")
            print("7. You can 'quit' at any time to end the game.")
        while True:
            print("\nHere is your hand: " )
            for card in self.player_hand:
                """
                Prints the value and rank of the cards in your hand
                """
                print(f"{card['rank']} of {card['suit']}")
            print("\n Dealer's hand:")
            print(f"{self.dealer_hand[0]['rank']} of {self.dealer_hand[0]['suit']}")
            # prints only one card in the dealer's hand. Maintain the suspense.
            print("One card face down")
            
            while True:
                choice = input("Do you want to hit or stay > ").lower()
                if choice == 'hit':
                    """
                    If the input is hit. it randomily generate a new card using drawcard function.
                    Then it proceeds to append the value of that card to the player's current hand.
                    """
                    new_card = self.draw_card()
                    self.player_hand.append(new_card)
                    
                    print("\n Here is your hand")
                    for card in self.player_hand:
                        print (f"{card['rank']} of {card['suit']}")
                    if self.calculate_hand_value(self.player_hand) > 21:
                        """
                        Calculates the value of the hand
                        """
                        print("Your hand value is over 21. You lose")
                    break # This was better than return in this situation as it allowed the player to continue with the game.
                elif choice == 'stay':
                    """
                    Player stops playing. Goes to the dealers turn until the end of the game.
                    """
                    break
                
                else:
                    print("Invalid choice. Please enter (hit) or (stay)")

            while self.calculate_hand_value(self.dealer_hand) < 17:
                """
                As per the rules, the dealer will continue drawing cards if their deck is below a value of 17.
                The value is then added to the dealer's hand
                """
                self.dealer_hand.append(self.draw_card())

            print("\nDealer's hand:")
            for card in self.dealer_hand:
                print(f"{card['rank']} of {card['suit']}")


            player_value = self.calculate_hand_value(self.player_hand)
            dealer_value = self.calculate_hand_value(self.dealer_hand)

            if player_value > 21:
                print("\nDealer wins.")
            elif dealer_value > 21:
                print("\nPlayer wins.")
            elif player_value > dealer_value:
                print("\nPlayer wins.")
            elif dealer_value > player_value:
                """
                This brings up an error if the value of both the player and the dealer are bigger than 21.
                And if the dealer value is bigger than the player, it shows that the dealer wins.
                """
                print("\nDealer wins.")
            elif dealer_value and player_value > 21:
                print("Both lost. it's a bust")
            else:
                print("\nIt's a tie! Dealer wins.")

            print("Player's hand value:", player_value)
            print("Dealer's hand value:", dealer_value)
            return
if __name__ == "__main__":
    game = Twentyone()
    game.play()