import unittest

from numbers import Number

def Fizz(x): 
    return 'Fizz' if isinstance(x,Number) and x % 3 == 0 else x

def Buzz(x):
    return 'Buzz' if isinstance(x, Number) and x % 5 == 0 else x

def FizzBuzz(x):
    return 'FizzBuzz' if isinstance(x, Number) and x % 15 == 0 else x

def jouer_FizzBuzz(start, end):
    output = []

    for x in range(start, end + 1):
        output.append(Buzz(Fizz(FizzBuzz(x))))

    return output

