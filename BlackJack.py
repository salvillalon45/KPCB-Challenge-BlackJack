"""
<!--

blackjack_game/BlackJack.py
********************************************************************************
KPCB Fellows Application - Answer the challenge question (optional): Make your application stand out.
http://fellows.kleinerperkins.com/engineering/apply

Build a console-based (i.e. runs in terminal) unix-compatible interactive card game.
You can pick Blackjack, Solitaire, Memory, or any other game of your choosing
(please include game rules in this case).

BlackJack.py

This module serves as the answer to the challenge question

********************************************************************************

University of California, Irvine
Salvador Villalon's Personal Projects
Summer 2018

Salvador Villalon

 -->
"""

import random
import official_deck

class Card:
    def __init__(self, name:str = None , value:int = None ):
        # Name of the card object
        self.name = name

        # Value of the card
        self.value = value

class Bets:
    def __init__(self, player_funds:int, player_bet:int):
        # Set this to 100 in the main()
        self.player_funds = player_funds

        # Manages bets
        self.player_bet = player_bet


def make_card(name:str, value:int) -> Card:
    """
    This function accepts the name and value of the card and returns
    the constructed Card object with the name and value
    assigned to the values passed on to the function.
    """
    card_obj = Card(name,value)
    return card_obj



def make_card_deck_list(my_deck:[{str:int}]) -> [Card]:
    """
	This function takes in a dictionary of card name and value pairs,
    creates a list of Card objects and returns it
    """
    card_list = list()

    for name,value in my_deck.items():
        card_obj = make_card(name, value)
        card_list.append(card_obj)

    return card_list


def print_deck(card_deck_list:[Card]) -> None:
    """
    This function takes in as input the list of Card objects and
    prints the name and value of each card in the list
    """
    for card_obj in card_deck_list:
        print(card_obj.name, card_obj.value)


def generate_shuffled_deck(full_deck:[Card]) -> [Card]:
    """
    This function takes in as input the list of Card objects, shuffles them
	and returns the shuffled list.
    """
    random.shuffle(full_deck)
    return full_deck


def intro_message() -> None:
    """
    This function prints the intro message
    when the game is run for the first time
    """
    print("""
Hello and Welcome to the Friend Computer's BlackJack Table!
At the Friend Computer's BlackJack Tables the closest player to 21, with a value less than 21 wins!
If you exceed 21, you lose. If the computer has card values closer to 21, you lose.
If you are closer to 21 than the computer, then you win!
Note: Ace defaults to 11, but will change to 1, should you exceed 21.
Let's get started
""")


def draw_card(available_cards:[Card]) -> Card:
    """
    This function returns the last most Card in the list
    that is given as input and returns the Card
    """

    last_most_card = available_cards.pop(-1)
    return last_most_card


def create_starting_hand(available_cards:[Card], num_to_draw:int) -> [Card]:
    """
    This function takes in as input the list of available cards, the
    number of cards to draw and returns the list
    """
    starting_list = list()

    for card_obj in range(num_to_draw):
        starting_list.append(draw_card(available_cards))

    return starting_list


def print_hand(card_list:[Card]) -> None:
    """
    This function takes is a list of Card objects as input and prints
    the name and value of each card
    """
    for card_obj in card_list:
        print(card_obj.name, card_obj.value)


def eval_hand(card_list:[Card]) -> int:
    """
    This function takes in a list of Card objects and returns the
    value of all cards in the list
    """
    total = 0

    for card_obj in card_list:
        total = total + card_obj.value

    return total


def print_player_hand(player_hand:[Card]) -> None:
    """
    This function takes in as input the list of Card objects and prints
    the name, value of each card along with the value of all the cards
    in the list
    """
    print("")
    print("Your hand contains:")
    print("")
    for card_obj in player_hand:
        print(card_obj.name, card_obj.value)
    print("")
    print("For a total value of: ", eval_hand(player_hand))
    print("")


def print_computer_hand(computer_hand:[Card]) -> None:
    """
    This function takes in as input the list of Card objects and prints
    the name, value of each card along with the value of all the cards
    in the list
    """
    print("")
    print("The Friend Computer's hand contains:")
    print("")
    for card_obj in computer_hand:
        print(card_obj.name, card_obj.value)
    print("")
    print("For a total value of: ", eval_hand(computer_hand))
    print("")


def getH_or_Schoice() -> str:
    """
    This function asks the user whether he wants to Hit and Miss,
    takes in the character input by the user, checks if it is valid,
    it returns it else it keeps asking the user to enter a valid character
    """
    while 1:
        user_input = input("Would you like to Hit(H) or Stay(S)? ")
        if user_input.lower() == "h" or user_input.lower() == "s":
            return user_input.lower()
        else:
            print("Incorrect choice, choose either Hit(H) or Stay(S)")


def stay_or_hit(player_hand:[Card], available_cards:[Card]) -> bool:
    """
    This function calls the getH_or_Schoice() function, gets the input entered
    by the user, if the user entered a 'H', draws an extra card for the player
    and evaluates it to be a bust of not
    """
    user_input = getH_or_Schoice()

    if user_input == "h":
        new_card = draw_card(available_cards)
        player_hand.append(new_card)
        result = eval_hand(player_hand)
        
        print("You drew ", new_card.name, " which has a value of ", new_card.value)
        print("Your hand now has a total value of: ", result)
        print("")

        if  21 < result:
            print("Oh No !! Your hand has busted as it has exceeded 21")
            print("Your hand had a total value of: ", result)
            print("The Computer Player Won!")
            return False

    elif user_input == "s":
        print('You chose to stay/skip your turn')
        return True


def computer_turn(computer_hand:[Card], available_cards:[Card]) -> bool:
    """
    This function evaluates the hand of the computer, if it
    is less than 17 it hits else stays
    """
    result = eval_hand(computer_hand)

    if result < 17:
        print("The Friend Computer Hits.")

        new_card = draw_card(available_cards)
        computer_hand.append(new_card)
        result = eval_hand(computer_hand)

        if 21 < result:
            print("The computer has bust. You win this round !!")
            print_computer_hand(computer_hand)
            return False

    else:
        print("The Friend Computer Stays.")
        return True


if "__main__" == __name__:

    # Initial Round

    # Setting up the card deck
    deck_list = make_card_deck_list(official_deck.official_deck)
    available_cards = generate_shuffled_deck(deck_list)
    intro_message()

    # Each round begins with starting a hand for each player
    player_hand = create_starting_hand(available_cards,2)
    computer_hand = create_starting_hand(available_cards,2)

    while 1:
        # Print Players hand
        print_player_hand(player_hand)
        print_player_hand(computer_hand)

        # Each round is composed of a series of turns
        # Each Turn

        player_s_h = stay_or_hit(player_hand, available_cards)
        # Check to see if player bust, if they did
        # the player lost the game
        if player_s_h == False:
            break

        computer_s_h = computer_turn(computer_hand, available_cards)
        # Check to see if Computer Player bust, if they did
        # the Computer Player lost the game
        if computer_s_h == False:
            break

        print_player_hand(player_hand)

        # If both players stay
        if player_s_h == True and computer_s_h == True:
            player_result = eval_hand(player_hand)
            computer_result = eval_hand(computer_hand)

            print("All player have chosen to stay, so we will reveal hands.")
            print("Your hand had a final value of ", player_result)
            print('The Friend Computer had a final value of', computer_result)
            if player_result == 21 and computer_result == 21:
                print("This is a tie!")
                break

            elif player_result == 21:
                print("You Win!")
                break

            elif computer_result == 21:
                print("The Computer Player Won!")
                break

            elif player_result > 21:
                print("You bust! Computer Player wins!")
                break

            elif computer_result > 21:
                print("Computer Player bust! You win")
                break

            elif player_result <= 21:
                print("You win!")
                break

            elif computer_result <= 21:
                print("Computer Player wins!")
                break

            else:
                print("Tie")
                break
