
import random
def print_separator(ui_width, char='-'):
    print(char * ui_width)

def print_centered_text(text, ui_width, char='-'):
    formatted_text = f'{char} {text} {char}'
    print(formatted_text.center(ui_width))

ui_width = 50

print_separator(ui_width)
print_centered_text('TWENTY ONE', ui_width)
print_separator(ui_width)

underStand = input("Do you know the rules of playing Twenty One?(yes/no) ").lower()
if underStand == "yes":
    print("That is great. We will now continue") #Have a fuction here that continues to the game.
elif underStand == "no":
    print("\nRules of Twenty One:")
    print("1. The goal is to beat the dealer without going over 21.")
    print("2. You can 'hit' to draw more cards or 'stand' to keep your current total.")
    print("3. Face cards are worth 10, Aces are worth 14 (or 1 if it helps you).")
    print("4. If you go over 21, you lose ('bust').")
    print("5. The dealer must hit until they have 17 or higher.")
    print("6. If the dealer and you have the same value at the end, the dealer wins")
    print("7. You can 'quit' at any time to end the game.")

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11,
          '2': 2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10
          }

# Function to create a new deck
def create_deck():
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def draw_card(deck):
    return deck.pop()


def calculate_hand_value(hand):
    total_value = sum(values[card['rank']] for card in hand)
    num_aces = sum(1 for card in hand if card['rank'] == 'Ace')
    while total_value > 21 and num_aces > 0:
        total_value -=10
        num_aces -= 1
    return total_value


initial_deck = create_deck()

player_hand = [draw_card(initial_deck), draw_card(initial_deck)]

dealer_hand = [draw_card(initial_deck), draw_card(initial_deck)]

"""
Create a class for hit or staying
"""


print("Here is your hand: " )
for card in player_hand:
    print(f"{card['rank']} of {card['suit']}")


print("\n Delaer's hand:")
print(f"{dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")
print("One card face down") #might not need this just want the player to know ho many rounds it has been


while True:
    choice = input("Do you want to hit oe stay > ").lower()
    if choice == 'hit':
        new_card = draw_card(initial_deck)
        player_hand.append(new_card)
        print("\n Here is your hand")
    for card in player_hand:
        print (f"{card['rank']} of {card['suit']}")
    if calculate_hand_value(player_hand) > 21:
        print("Your hand value is over 21. You lose")
        break
    elif choice == 'stay':
        break
    else:
        print("Invalid choice. Please enter (hit) or (stay)")

while calculate_hand_value(dealer_hand) < 17:
    dealer_hand.append(draw_card(initial_deck))

print("\nDealer's hand:")
for card in dealer_hand:
    print(f"{card['rank']} of {card['suit']}")


player_value = calculate_hand_value(player_hand)
dealer_value = calculate_hand_value(dealer_hand)

if player_value > 21:
    print("\nDealer wins. Player busts.")
elif dealer_value > 21:
    print("\nPlayer wins. Dealer busts.")
elif player_value > dealer_value:
    print("\nPlayer wins.")
elif dealer_value > player_value:
    print("\nDealer wins.")
else:
    print("\nIt's a tie! Dealer wins.")

print("Player's hand value:", player_value)
print("Dealer's hand value:", dealer_value)
