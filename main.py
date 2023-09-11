
import random
def print_separator(ui_width, char='-'):
    print(char * ui_width)

def print_centered_text(text, ui_width, char='-'):
    formatted_text = f'{char} {text} {char}'
    print(formatted_text.center(ui_width))

ui_width = 50

print_separator(ui_width)
print_centered_text('BLACK JACK', ui_width)
print_separator(ui_width)

underStand = input("Do you know the rules of playing Black jack?(yes/no) ").lower()
if underStand == "yes":
    print("Tha is great. We will now continue") #Have a fuction here that continues to the game.
elif underStand == "no":
    print("\nRules of Blackjack:")
    print("1. The goal is to beat the dealer without going over 21.")
    print("2. You can 'hit' to draw more cards or 'stand' to keep your current total.")
    print("3. Face cards are worth 10, Aces are worth 11 (or 1 if it helps you).")
    print("4. If you go over 21, you lose ('bust').")
    print("5. The dealer must hit until they have 17 or higher.")
    print("6. You can 'quit' at any time to end the game.")
# Dictionary for a deck of cards
deck_of_cards = {
    'Hearts': {
        'Ace': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
    },
    'Diamonds': {
        'Ace': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
    },
    'Clubs': {
        'Ace': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
    },
    'Spades': {
        'Ace': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
    }
}
def ur_deck():
    player_deck = random.deck_of_cards
    print(player_deck)
    conti_nue = input("Do you want to add more cards? (hit or stand) > ")
    if conti_nue == "hit" :
        update_player_deck = player_deck + random.deck_of_cards


print(ur_deck())
