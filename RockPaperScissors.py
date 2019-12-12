#!/usr/bin/env python3

import random # - For randomness

# Set up variables
draws = 0
wins = 0
losses = 0
is_ended = False
prompt = "Choose Rock(r), Choose Paper(p), Choose Scissors(s). 'q' to quit: "

while True: #- Loop till break
    user_choice = input(prompt)
    while user_choice not in ['r', 'p', 's', 'q']:
        user_choice = input(prompt) #- if user does not select one of the 4 letters, repeat the prompt message
    if user_choice == 'q':
        break # - ends loops if you enter q
    else:
        computer_choice = random.choice(['r', 'p', 's'])
        if computer_choice == 'r':
            move = 'rock'
        elif computer_choice == 'p':
            move = 'paper'
        else:
            move = 'Scissors'
        print('Computer gives a ' + move)

    if computer_choice == user_choice:
        print('Draw')
        draws += 1
    elif    (computer_choice == 'r' and user_choice == 'p') or \
            (computer_choice == 'p' and user_choice == 's') or \
            (computer_choice == 's' and user_choice == 'r'):
            print('You win!')
            wins += 1
    else:
        print('You lose!')
        losses += 1
print('You have ' + str(wins) + ' wins, ' + str(draws) + ' draws, and ' + str(losses) + ' losses.')

