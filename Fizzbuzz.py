import unittest
from unittest.case import TestCase

from fizzbuzz_romain import Fizz, Buzz, FizzBuzz

class fizzbuzz_programme (unittest.TestCase):

    def fonction_fizz ():
        
        def erreur_si_input_vide ():
            with unittest(TestCase) as exception_info:
                Fizz()
                assert exception_info.type == TestCase
                assert "1 argument requis manquant" in str(exception_info.value)

    def retourne_Fizz_si_multiple_3 ():
        # est un multiple de 3 ?
        assert Fizz(3) == 'Fizz'        # multiple de 3
        assert Fizz(2) == 2             # non multiple de 3
        assert Fizz(0) == 'Fizz'        # rien
        assert Fizz(-3) == 'Fizz'       # multiple negatif de 3
        assert Fizz(-4) == -4           # negatif non-multiple de 3
        assert Fizz('Buzz') == 'Buzz'   # test input de string   

#----------------------------
    def fonction_buzz ():
        
        def erreur_si_input_vide ():
            with unittest(TestCase) as exception_info:
                Buzz()
                assert exception_info.type == TestCase
                assert "1 argument requis manquant" in str(exception_info.value)
    

    def retourne_Buzz_si_multiple_5 ():
        # est un multiple de 3 ?
        assert Buzz(5) == 'Buzz'        # multiple de 5
        assert Buzz(2) == 2             # non multiple de 5
        assert Buzz(0) == 'Buzz'        # rien
        assert Buzz(-5) == 'Buzz'       # multiple negatif de 5
        assert Buzz(-4) == -4           # negatif non-multiple de 5
        assert Buzz('Fizz') == 'Fizz'   # test input de string    