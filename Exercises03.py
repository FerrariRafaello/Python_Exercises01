#---------------------#
# Print a triangle of digits

def print_triangle(value):
    for n in range(value):
        n += 1
        print(str(n) * n)

value = int(input('Enter a number: '))
print_triangle(value)

#---------------------#
# Print increasing sequences in lines

def print_line(value):
    for n in range(1, value + 1):
        print(f'  {n} ', end='')
    print()

def print_sequence(value):
    for v in range(value + 1):
        print_line(v)

value = int(input('Enter a number: '))
print_sequence(value)

#---------------------#
# Print user's name with a message

def print_name(user_name):
    print('User:', user_name, 'wrote a message!')

name = input('Enter your name: ')
print_name(name)

#---------------------#
# Create random list and return stats

import random
def create_list(size):
    lst = []
    for _ in range(size):
        val = random.randint(1, 10)
        lst.append(val)
    return lst, max(lst), min(lst)

size = int(input('List size: '))
li, maxli, minli = create_list(size)
print('List:', li)
print('Max:', maxli)
print('Min:', minli)

#---------------------#
# Factorial calculation

def factorial(number):
    fat = 1
    while number > 0:
        fat *= number
        number -= 1
    print('Result:', fat)

number = int(input('Enter a number: '))
factorial(number)

#---------------------#
# Fibonacci up to n

def fib(n):
    a, b = 0, 1
    print(a)
    while b < n:
        print(b)
        a, b = b, a + b

n = int(input('Enter the value: '))
fib(n)

#---------------------#
# Fibonacci sequence as a list

def fib2(n):
    result = []
    a, b = 0, 1
    result.append(a)
    while b < n:
        result.append(b)
        a, b = b, a + b
    print(result)

fib2(8)

#---------------------#
# Function with default parameters

def greet(name, greeting='Hi', punctuation='!!'):
    return f'{greeting},{name}{punctuation}'

print(greet('John'))
print(greet('John', 'Congrats'))
print(greet('John', 'Oh', '...'))

#---------------------#
# Function with named and default arguments

def show_info(required, name='john', age=20):
    print('required:', required)
    print('name:', name)
    print('age:', age)

show_info("test")
show_info("test", 10)  # 10 will be assigned to 'name'

#---------------------#
# Recursive factorial

def recursive_factorial(num):
    if num == 1:
        return 1
    else:
        return num * recursive_factorial(num - 1)

print('Recursive factorial:', recursive_factorial(6))

#---------------------#
# Variable scope examples

def f():
    print(a)
a = 1
f()

#---------------------#
def f():
    a = 5
f()
print(a)

#---------------------#
def f():
    global a
    a = 5
f()
print(a)

#---------------------#
x = 'Spam'
def func():
    x = 'Ni'
    print(x)
func()
print(x)

#---------------------#
x = 'test'
def func():
    x = 'Ni'
    def nested():
        x = 'Spam'
        print(x)
    nested()
    print(x)
func()
print(x)

#---------------------#
def func():
    global x
    x = 5
    def new():
        x = 'n'
        print(x)
    new()
func()
print(x)

#---------------------#
x = 'test'
def func():
    x = 'ni'
    def nested():
        nonlocal x
        x = 'Spam'
        print(x)
    nested()
    print(x)
func()
print(x)

#---------------------#
# Example using random float (fixed import!)
import random
print(random.uniform(1, 10))  # random float between 1 and 10
