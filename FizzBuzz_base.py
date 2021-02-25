from fizzbuzz_romain import Fizz, Buzz, FizzBuzz

nombreAlice = "Le nombre de Alice : "

x = int(input("Bob : entre un chiffre de 1 à 100"))
if x < 1:
    print("erreur")
elif(x % 3 == 0 and x % 5 != 0):
    print("fizz")
elif(x % 5 == 0 and x % 3 != 0):
    print("buzz")
elif(x % 3 == 0 and x % 5 == 0):
    print("fizzbuzz")
else:
    print("{}{}".format(nombreAlice, x))

    