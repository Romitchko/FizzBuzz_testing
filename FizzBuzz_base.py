from fizzbuzz_romain import Fizz, Buzz, FizzBuzz

x = int(input("Entrer un chiffre de 1 à 100"))
if x < 1:
    print("erreur")
elif(x % 3 == 0 and x % 5 != 0):
    print("fizz")
elif(x % 5 == 0 and x % 3 != 0):
    print("buzz")
elif(x % 15 == 0):
    print("fizzbuzz")
else:
    print(x)

    