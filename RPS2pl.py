#!/usr/bin/env python3

import sys # imports sys module for interaction with system

player1 = raw_input('Player 1 what is your name?')
player2 = raw_input('Player 2 what is your name?')

player1_ans = raw_input("%s, Rock, Paper or Scissors?" % player1) #- %s for string from the input
player2_ans = raw_input("%s, Rock, Paper or Scissors?" % player2)

def compare(p1, p2):  #- compares player 1 and 2 answers
    if p1 == p2:
        return("It's a draw!")
    elif p1 == 'Rock':
        if p2 == 'Scissors':
            return ("Rock wins!")
        else:
            return("Paper wins!")
    elif p1 == 'Paper':
        if p2 == 'Rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    elif p1 == 'Scissors':
        if p2 == 'Paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    else:
        return("Wrong Invalid Input. You have not entered Rock, Paper or Scissors. Please Try again. Remember Cap sensitive. ")
        sys.exit()

print(compare(player1_ans, player2_ans))


