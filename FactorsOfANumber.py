__author__ = 'Abdullah AlOfi'

def Factors(number):
    factors = []
    for i in range((number), 0, -1):
        if number % i == 0:
            factors.extend([i])
    factors.sort()
    if len(factors) == 2:
        print ('{0} is a prime number. Thus, it has no factors but itself and one'.format(number))
    else:
        print('{0} has {1} factors. They are:'.format(number, len(factors)))
        print(factors)

Factors(int(input('Insert the number you wanna factor: \n')))