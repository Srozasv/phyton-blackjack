from card import Card
from deck import Deck
from chips import Chips
from hand import Hand
from utils import clear_console

def place_bet(player):
    bet = 10000000
    while player.total < bet:
        bet = int(input('Place your bet:'))
        if bet > player.total:
            print("You don't have enough chips, Try again!")
        else:
            player.bet = bet
    return player.bet

def hit(deck,hand):
    dealt_card = deck.deal_card()
    hand.add_card(dealt_card)

def hit_or_stand(deck,hand):
    global playing
    while playing:
        response = input('Do you want to Hit(H) or Stand(S)?').upper()
        if response == 'S':
            playing = False
            break
        else:
            hit(deck,hand)
            break

def show_some(player,dealer):
    print('Player hand:')
    for card in player.cards:
        print(card)
    print('Dealer hand:')
    print('<Hiden Card>')
    print(dealer.cards[1])

def show_all(player,dealer):
    print('Player hand:')
    for card in player.cards:
        print(card)
    print('Dealer hand:')
    for card in dealer.cards:
        print(card)

def player_busts(chips):
    print('Player busted! You lost!')
    chips.lose_bet()

def dealer_busts(chips):
    print('Dealer Busted! You won!')
    chips.win_bet()

def player_win(chips):
    print('Player won')
    chips.win_bet()

def dealer_win(chips):
    print('Dealer won!')
    chips.lose_bet()

def push():
    print('Its a tie!')


# Start of the game loop
playing = True
player_chips = Chips()
while True:
    # Print an opening statement
    print('Welcome to the blackjack table!')
    
    # Create & shuffle the deck, deal two cards to each player
    game_deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    
    game_deck.shuffle_deck()
    hit(game_deck,player_hand)
    hit(game_deck,player_hand)
    hit(game_deck,dealer_hand)
    hit(game_deck,dealer_hand)    
    
    # Prompt the Player for their bet
    print(f'Your total chips:{player_chips.total}')
    place_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        # Prompt for Player to Hit or Stand
        hit_or_stand(game_deck, player_hand)
        clear_console()
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(game_deck, dealer_hand)
        # Show all cards
        clear_console()
        show_all(player_hand,dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_win(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_win(player_chips)
        else:
            push()
    # Inform Player of their chips total 
    print(f"Now you have {player_chips.total} chips to bet")
    # Ask to play again
    if player_chips.total == 0:
        print("You don't have enough chips to keep playing. Better luck next time!")
        break
    new_game = input('Do you want to play again?:')
    if new_game.upper() == 'Y':
        playing = True
        continue
    else:
        print('Thanks for playing!')
        break
