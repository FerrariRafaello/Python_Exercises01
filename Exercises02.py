#---------------------#
# Number triangle

def print_triangle(value):
    if not isinstance(value, int):
        return
    for x in range(1, value + 1):
        line = ''
        for y in range(1, x + 1):
            line += str(y) + '\t'
        print(line)

print_triangle(5)  # Example usage

#---------------------#
# Sum of three numbers

def sum_values(n1, n2, n3):
    print(n1 + n2 + n3)

sum_values(9, 4, 5)

#---------------------#
# Check sign (positive/negative)

def check_sign(var):
    if var >= 0:
        print('P')
    else:
        print('N')

value = float(input('Enter a value: '))
check_sign(value)

#---------------------#
# Add tax to a cost

def add_tax(cost, tax_percent):
    tax = (cost * tax_percent) / 100
    print(cost + tax)

cost = float(input('Enter the initial cost: '))
tax_rate = float(input('Enter the tax percentage: '))
add_tax(cost, tax_rate)

#---------------------#
# Print hour in 12-hour format

def convert_hour(hour):
    return hour - 12

def print_time(hour, minute):
    if hour <= 12:
        print(hour, minute, 'AM')
    else:
        print(convert_hour(hour), minute, 'PM')

hour = int(input('Enter the hour: '))
minute = int(input('Enter the minute: '))
print_time(hour, minute)

#---------------------#
# Count digits in a number

def count_digits(number):
    print('Number of digits:', len(str(abs(int(number)))))

number = int(input('Enter an integer: '))
count_digits(number)

#---------------------#
# Reverse a number (as string)

def reverse_str(n):
    return str(n)[::-1]

n = input('Enter a number: ').strip()
print('Reverse:', reverse_str(n))

#---------------------#
# Dice roll game

import random

def roll_dice():
    return random.randint(2, 12)

def dice_game():
    print('Press [s] to exit or <Enter> to roll the dice.')
    play = ''
    roll_count = 0
    point = 0

    while play != 's':
        roll_count += 1
        print(f'Roll {roll_count}')
        play = input('Awaiting action: ')
        if play == 's':
            break
        value = roll_dice()
        print(f'Dice value: {value}\n')
        if roll_count == 1:
            if value in (7, 11):
                print('Natural! You win!')
                return
            elif value in (2, 3, 12):
                print('Craps! You lose!')
                return
            else:
                point = value
        else:
            if value == 7:
                print('You rolled 7 before making your point—You lose!')
                return
            elif point == value:
                print('You made your point! You win!')
                return

dice_game()

#---------------------#
# Shuffle the letters of a word

from random import shuffle
def shuffle_word(word):
    a = list(word)
    shuffle(a)
    shuffled = ''.join(a)
    print(shuffled.lower())

word = input('Enter a word: ')
shuffle_word(word)

#---------------------#
# Print a rectangle of width and height

def print_rectangle(w, h):
    w = min(w, 20)
    h = min(h, 20)
    print('-+-' * w)
    for _ in range(h):
        print('|' + '   ' * (w - 1) + '|')
    print('-+-' * w)

width = int(input('Enter width: '))
height = int(input('Enter height: '))
print_rectangle(width, height)

#---------------------#
# FizzBuzz

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Buzz'
    if n % 5 == 0:
        return 'Fizz'
    return n

value = int(input('Enter a value: '))
print(fizzbuzz(value))
