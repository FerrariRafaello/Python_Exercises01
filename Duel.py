from random import randint
from operator import itemgetter

while True:
    print('\n--- Dice Duel ---')
    player1 = input('Enter your name, Player 1: ')
    player2 = input('Enter your name, Player 2: ')

    # Roll dice for each player
    rolls = {player1: randint(1, 6), player2: randint(1, 6)}
    for name, roll in rolls.items():
        print(f'{name} rolled a {roll}.')

    # Sort players by roll (descending)
    ranking = sorted(rolls.items(), key=itemgetter(1), reverse=True)
    for position, (name, roll) in enumerate(ranking, start=1):
        print(f'{position}° place: {name} with {roll}')

    # Decide winner or tie
    if ranking[0][1] == ranking[1][1]:
        print('It\'s a tie!')
    else:
        print(f'Winner: {ranking[0][0]}!')

    # Play again?
    again = input('Play again? [y/n]: ').strip().lower()
    if again != 'y':
        print('Good game!')
        break
