from blackjack_helper import *

user_hand = draw_starting_hand("YOUR")

while user_hand < 21:
    hit = input(f"You have {user_hand}. Hit (y/n)? ")
    if hit == "y":
        user_hand += draw_card()
    elif hit == "n":
        break
    else:
        print("Sorry I didn't get that.")

print_end_turn_status(user_hand)

dealer_hand = draw_starting_hand("DEALER")

while dealer_hand < 17:
        print(f"Dealer has {dealer_hand}.")
        dealer_hand += draw_card()

print_end_turn_status(dealer_hand)

print_end_game_status(user_hand, dealer_hand)
