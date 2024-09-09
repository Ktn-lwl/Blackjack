def name(card):
    if card == 1:
        return "Drew an Ace"
    elif card >= 2 and card <= 10:
        return f"Drew a{'n'*int(card == 8)} {card}"
    elif card == 11:
        return "Drew a Jack"
    elif card == 12:
        return "Drew a Queen"
    elif card == 13:
        return "Drew a King"

def value(card):
    if card in range(11, 14):
        return 10
    elif card == 1:
        return 11
    else:
        return card

def dealer(hand_val):
    while hand_val < 17:
        print(f"Dealer has {hand_val}.")
        card = randint(1, 13)
        hand_val += value(card)
        print(name(card))
    
    return hand_val

def player(hand_val):
    while hand_val < 21:
        hit = input(f"You have {hand_val}. Hit (y/n)? ")
        if hit == "y":
            card = randint(1, 13)
            hand_val += value(card)
            print(name(card))
        elif hit == "n":
            break
        else:
            print("Sorry I didn't get that.")

    return hand_val

def blackjack(deal_r=False):
    c1, c2 = randint(1, 13), randint(1, 13)
    print(name(c1), name(c2), sep="\n")

    hand_val = value(c1) + value(c2)

    if deal_r:
        hand_val = dealer(hand_val)
    else:
        hand_val = player(hand_val)

    print(f"Final hand: {hand_val}.")
    if hand_val == 21:
        print("BLACKJACK!")
        return (hand_val, True)
    elif hand_val > 21:    
        print("BUST.")
        return (hand_val, False)
    else:
        return(hand_val, True)

print("-----------\nYOUR TURN\n-----------")
you = blackjack()
print("-----------\nDEALER TURN\n-----------")
dilla = blackjack(True)
print("-----------\nGAME RESULT\n-----------")

"""
You win if you didn't bust AND:

- you have a 21 
OR
- you have greater than the dealer AND the dealer didn't bust.
OR
-  the dealer bust
"""

win_condition = (you[1] and ((you[0] == 21) or 
                             (you[0] > dilla[0] and dilla[1]) or
                             (not dilla[1])
                            )
                )
if win_condition:
    print("You win!")
elif you[1] and (you[0] == dilla[0]):
    print("Push.")
elif not you[1] or dilla[1]:
    print("Dealer wins!")
