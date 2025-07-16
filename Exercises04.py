#--------------------------#
# Compare two values and print the greater one

value1 = float(input('Enter the first value: '))
value2 = float(input('Enter the second value: '))
print(max(value1, value2))

#--------------------------#
# Check if a value is positive or negative

value = float(input('Enter a positive or negative value: '))
if value < 0:
    print('Negative value!')
else:
    print('Positive value!')

#--------------------------#
# Gender letter validation

letter = input('Enter the letter [f] or [m]: ').lower()
if letter not in ('f', 'm'):
    print('Invalid letter')
elif letter == 'f':
    print('Feminine')
else:
    print('Masculine')

#--------------------------#
# Vowel or consonant

letter = input('Enter a letter: ').lower()
if letter in ('a', 'e', 'i', 'o', 'u'):
    print('Vowel:', letter)
else:
    print('Consonant:', letter)

#--------------------------#
# Average grade and status

grade1 = float(input('Enter grade 1: '))
grade2 = float(input('Enter grade 2: '))
average = (grade1 + grade2) / 2

if average == 10:
    print('Approved with distinction!')
elif average >= 7:
    print('Approved!')
else:
    print('Failed!')

#--------------------------#
# Largest of three numbers

numbers = []
for i in range(1, 4):
    num = float(input(f'Enter number {i}: '))
    numbers.append(num)
print('Numbers:', numbers)
print('Maximum:', max(numbers))

#--------------------------#
# Largest and smallest of three numbers

numbers = []
for i in range(1, 4):
    num = float(input(f'Enter number {i}: '))
    numbers.append(num)
print('Numbers:', numbers)
print(f'Maximum: {max(numbers)}, Minimum: {min(numbers)}')

#--------------------------#
# Cheapest of three products

prices = []
for i in range(1, 4):
    price = float(input(f'Enter the price of product {i}: '))
    prices.append(price)
print('Prices:', prices)
print(f'You should buy the product costing {min(prices)}!')

#--------------------------#
# Sort 7 numbers descending

numbers = []
for i in range(1, 8):
    num = float(input(f'Enter number {i}: '))
    numbers.append(num)
print('Numbers:', numbers)
print('Sorted descending:', sorted(numbers, reverse=True))

#--------------------------#
# Greeting based on study shift

shift = input('Enter the initial of your study shift [M/V/N]: ').lower()
if shift == 'm':
    print('Good morning!')
elif shift == 'v':
    print('Good afternoon!')
elif shift == 'n':
    print('Good evening!')
else:
    print('Invalid value!')

#--------------------------#
# Salary adjustment based on salary

salary = float(input('Enter the salary amount: '))
if salary <= 280:
    percent = 20
elif salary <= 700:
    percent = 15
elif salary <= 1500:
    percent = 10
else:
    percent = 5
increase = salary * percent / 100
new_salary = salary + increase
print(f'Your previous salary: {salary:.2f}, new salary: {new_salary:.2f} (increase: {percent}%)')

#--------------------------#
# Triangle type

a = float(input('First side: '))
b = float(input('Second side: '))
c = float(input('Third side: '))

if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print('Not a triangle')
elif (a == b) and (b == c):
    print('Equilateral')
elif (a == b) or (a == c) or (b == c):
    print('Isosceles')
else:
    print('Scalene')

#--------------------------#
# Date validation

day = int(input('Day: '))
month = int(input('Month: '))
year = int(input('Year: '))

valid = False

# Months with 31 days
if month in (1, 3, 5, 7, 8, 10, 12):
    if 1 <= day <= 31:
        valid = True
# Months with 30 days
elif month in (4, 6, 9, 11):
    if 1 <= day <= 30:
        valid = True
# February, check leap year
elif month == 2:
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap and 1 <= day <= 29:
        valid = True
    elif not is_leap and 1 <= day <= 28:
        valid = True

if valid:
    print('Valid date')
else:
    print('Invalid date')

#--------------------------#
