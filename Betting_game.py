import random

'''
Simple betting game:
The user bets on a number between 1 and 10.
If the random number matches the bet, they win!
Otherwise, the house wins.
'''

while True:
    try:
        bet = int(input('Place your bet (choose a number between 1 and 10): '))
    except ValueError:
        print('Please enter a valid integer!')
        continue

    if not (1 <= bet <= 10):
        print('Bet must be between 1 and 10!')
        continue

    drawn = random.randint(1, 10)
    print(f'The drawn number was: {drawn}')

    if drawn == bet:
        print('Congratulations, you won!')
    else:
        print('The house always wins!')

    again = input('Do you want to bet again? Press [s] to continue or [n] to exit: ').lower()
    if again != 's':
        break

print('See you next time, player!')
