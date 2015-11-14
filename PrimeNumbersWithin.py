__author__ = 'Abdullah AlOfi'


def PrimeNumbersWithin(number):
    primes = []
    for j in range((number), 1, -1):
        factors = 0
        for i in range(j - 1, 1, -1):
            if j % i == 0:
                factors += 1
        if factors == 0:
            primes.extend([j])
    primes.sort()
    print('There are {0} prime numbers below {1}. and they are:'.format(len(primes),(number)))
    print(primes)


PrimeNumbersWithin(int(input('Enter the Number you want to find the primes below: \n')))
