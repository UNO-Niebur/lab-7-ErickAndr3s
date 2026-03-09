#SummationOfPrimes.py
#Name:Erick Andres
#Project Euler Problem 10
#Purpose: Find the sum of all prime numbers below a given number.

#Approach:
#I looped through all numbers from 2 up to the given limit.
#For each number, I checked if it was prime using isPrime().
#If it was prime, I added it to a total sum.
#At the end, I returned the sum of all primes found.


from NumberTests import isPrime

def sumPrimes(limit):
    """Returns the sum of all prime numbers below the given limit."""
    total = 0
    for num in range(2, limit):
        if isPrime(num):
            total += num
    return total

print("Sum of primes below 2500(example):", sumPrimes(2500))
