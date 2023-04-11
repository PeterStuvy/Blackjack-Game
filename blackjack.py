import random
import sys

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']

def choose_initial_cards():
    
    cards = {}
    
    for deal in range(2):
        
        face = random.choice(numbers)
        suit = random.choice(suits)
        
        cards[deal] = (face, suit)
    
    return cards


dealer_hand = choose_initial_cards()

player_hand = choose_initial_cards()


def calculate_value(hand):
    
    value_sum = 0
    
    for deal in hand:
        
        if isinstance(hand[deal][0], int):
            value = hand[deal][0]
        
        elif hand[deal][0] == 'Ace':
            
            if value_sum < 11:
                value = 11
                
            else:  
                value = 1
            
        else:
            value = 10
        
        value_sum = value_sum + value
        
    return value_sum


dealer_value = calculate_value(dealer_hand)

player_value = calculate_value(player_hand)


def print_cards(holder):
    
    if holder == 'dealer':
        hand = dealer_hand
    
    else:
        hand = player_hand
        
    for cards in hand:

        face = hand[cards][0]
        suit = hand[cards][1]
        
        print(f'{face} of {suit}')
        
def print_all():
    
    print('')
    print('The Dealers Cards Are: ')
    print_cards('dealer')
    print(f'Value: {dealer_value}')
    print('')
    print('----------')
    print('')
    print('Your Cards Are: ')
    print_cards('player')
    print('')
    print(f'Value: {player_value}')
    print('')

print_all()

if dealer_value == 21 and player_value != 21:
    
    print('The Dealer Got Blackjack! You Lose.')
    sys.exit()
    
elif player_value == 21:
    
    print('You Got Blackjack! You Win!')
    sys.exit()

def hit_decision():
    
    decision = input('Would you like to hit? (y/n): ').lower()
    
    if decision == 'y':
        decision = True
    else:
        decision = False
        
    return decision


player_decision = hit_decision()


def deal_additional_card():
    
    face = random.choice(numbers)
    suit = random.choice(suits)
    
    card = (face, suit)
    
    return card


while player_decision:
    
    player_hand[len(player_hand)] = deal_additional_card()
    player_value = calculate_value(player_hand)
    
    if player_value > 21:    
        break
    
    else:
        print_all()
    
    player_decision = hit_decision()
    
if player_value > 21:
    print_all()
    print('Too Many - You Lose.')
    sys.exit()

    
while dealer_value < 17:
    
    dealer_hand[len(dealer_hand)] = deal_additional_card()
    dealer_value = calculate_value(dealer_hand)
    
    if dealer_value > 21:
        print_all()
        print('The Dealer Busts - You Win!')
        sys.exit()
        

if dealer_value == player_value:
    
    print_all()
    print('Its a Tie - Push')
    
elif dealer_value > player_value:
    
    print_all()
    print('Dealer wins.')
    
else:
    
    print_all()
    print('You win!')
    
