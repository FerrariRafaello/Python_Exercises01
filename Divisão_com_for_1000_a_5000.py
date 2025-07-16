'''
Count and print all numbers between 1000 and 5000 that are divisible by both 3 and 5.
'''

count = 0
for x in range(1000, 5001):
    # Check if x is divisible by both 3 and 5
    if x % 3 == 0 and x % 5 == 0:
        print(f'{x} is divisible by both 3 and 5')
        count += 1

print(f'There are {count} numbers divisible by both 3 and 5 between 1000 and 5000.')
