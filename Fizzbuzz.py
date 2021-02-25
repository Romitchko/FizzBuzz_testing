import unittest

from fizzbuzz_romain import Fizz, Buzz, FizzBuzz

class fizzbuzz_programme (unittest.TestCase):
    def returns_Fizz_if_x_is_multiple_of_3 ():
        # est un multiple de 3 ?
        assert Fizz(3) == 'Fizz'        # multiple de 3
        assert Fizz(2) == 2             # non multiple de 3
        assert Fizz(0) == 'Fizz'        # rien
        assert Fizz(-3) == 'Fizz'       # multiple negatif de 3
        assert Fizz(-4) == -4           # negatif non-multiple de 3
        assert Fizz('Buzz') == 'Buzz'   # test input de string      