from random import randint

def print_card_name(card_rank: int):
    """
    Prints the given card's official name in the form "Drew a(n) ___".
    If the input card is invalid, prints "BAD CARD"
    Parameters:    card_rank -> The numeric representation of a card (1-13)
    Return:   None
 """
    if card_rank == 1:
        print("Drew an Ace")
    elif card_rank in range(2,11):
        print(f"Drew a{'n'*(card_rank == 8)} {card_rank}")
    elif card_rank == 11:
        print("Drew a Jack")
    elif card_rank == 12:
        print("Drew a Queen")
    elif card_rank == 13:
        print("Drew a King")
    else:
        print("BAD CARD")

def draw_card():
    """
    Draws a new random card, prints its name, and returns its value.
    Parameters:   none
    Return:  an int representing the value of the card. All cards are worth
             the same as the card_rank except Jack, Queen, King, and Ace.
    """
    card = randint(1, 13)
    print_card_name(card)
    if card in range(11, 14):
        return 10
    elif card == 1:
        return 11
    else:
        return card


def print_header(message: str):
    """
    Prints the given message formatted as a header. A header looks like:
    -----------
    message
    -----------
    
    Parameters:    message -> the string to print in the header
    Return:    None
    """
    print(f"-----------\n{message}\n-----------")
    
def draw_starting_hand(name):
    """
    Prints turn header and draws a starting hand, which is two cards.
    Parameters:    name -> The name of the player whose turn it is.
    Return:    The hand total, which is the sum of the two newly drawn cards.
    """
    print_header(f"{name} TURN")
    return draw_card() + draw_card()
    

def print_end_turn_status(hand_value):
    """
    Prints the hand total and status at the end of a player's turn.
    Parameters:    hand_value -> the sum of all of a player's cards at the end of their turn.
    Return:    none
    """
    print(f"Final hand: {hand_value}.")
    if hand_value == 21:
        print("BLACKJACK!")
    elif hand_value > 21:
        print("BUST.")
    

def print_end_game_status(user_hand, dealer_hand):
    """
     Parameters:    user_hand -> the sum of all cards in the user's hand
                    dealer_hand -> the sum of all cards in the dealer's hand
    Return:    none
    """
    print_header("GAME RESULT")
    if user_hand > 21:
        print("Dealer wins!")
    elif user_hand == dealer_hand:
        print("Push.")
    elif user_hand == 21:
        print("You win!")
    elif dealer_hand > user_hand and dealer_hand <= 21:
        print("Dealer wins!")
    elif dealer_hand > user_hand and dealer_hand >= 21:
        print("You win!")
    elif user_hand > dealer_hand:
        print("You win!")

