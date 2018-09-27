# KPCB-Challenge-BlackJack
[Personal Project] - Project: BlackJack

# Description
- This a one player versus Computer Black Jack game
- This game does not implement the idea of betting since it is a friendly introduction to the game of Black Jack

# Design Choices
- I created a class called Card with member variables of name and value. This will help differentiate the cards since they have repeated values (such as 10, 7, etc.) but different names.
  I can  then make Card objects for each card
- For functions, I had a total of 14 functions each that helped implement the game. You can read more about each function on the comments I made.
- Logic for the Computer Player. The Computer Player will hit (draw a card) wen the result of the evaluation of its card is less than 17. Otherwise it will stay and not draw a card.

# Instructions
- Clone the repository and run the BlackJack.py module. I am using Python 3.7.0 so make sure to be using the same version. 

# Modules and Files
- BlackJack.py
  - Contain all the code and content to run the game
- official_deck.py
  - Contains the official deck of 52 cards for the game

# Technologies and Tooling
- I used the following technologies and libraries
  - Random LIbrary:
    - I used this library to help create a random shuffle deck.
    - This shuffle deck will be used to give a starting hand to the computer and human player
  - Python 3.7.0
  - Git
  - GitHub
