#10001stPrime.py
#Name: Erick Andres
#Project Euler Problem 7
#Purpose: Find the 10001st prime number.

#Approach:
#I counted primes starting from 2.
#Every time I found a prime using isPrime(), I added 1 to my count.
#When the count reached 10001, I saved that prime as the answer.

from NumberTests import isPrime

def findNthPrime(n):
    """Finds and returns the nth prime number using isPrime() from NumberTests."""
    count = 0
    num = 1
    while count < n:
        num += 1
        if isPrime(num):
            count += 1
    return num

print("The 10001st prime is:", findNthPrime(10001))