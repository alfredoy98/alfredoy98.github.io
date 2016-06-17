# calc.py

# Import modules
import math
import re

# Welcome
print('Welcome to calc.py.')

# Pythagorean Theorem. Calculate Hypotenuse
def pyth(a, b):
    return a**2 + b**2

# Quadratic formula.
def quad(a, b, c):
    negative = False
    positive = False
    # Check if imaginary
    try:
        negative = (-b+math.sqrt(b**2-4*a*c))/2*a
        positive = (b+math.sqrt(b**2-4*a*c))/2*a
    except ValueError:
        return "The result was imaginary. This calculator does not support imaginary numbers."
    return 'The results are %s and %s.' % (negative, positive)

# App State
running = True

# Instructions
print('Please enter your desired task. ie: (pyth 1 4, quad 1 -4 4, or stop)')

# Loop through
while running:
    expType = input('What type of expression should I parse? (pyth or quad) => ')
    # If pythagorean expression
    if expType == 'pyth':
        a = eval(input('Value for a => '))
        b = eval(input('Value for b => '))
        print(pyth(a, b))
    # If quadratic expression
    elif expType == 'quad':
        a = eval(input('Value for a => '))
        b = eval(input('Value for b => '))
        c = eval(input('Value for c => '))
        print(quad(a, b, c))
    # If stop loop
    elif expType == 'stop':
        print('Goodbye!')
        running = False
    else:
        print('This program does not support your statement.')
