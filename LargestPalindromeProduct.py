#LargestPalindromeProduct.py
#Name:Erick Andres
#Project Euler Problem 4
#Purpose: to find the biggest palindrome from multiplying 3 digit numbers


#Approach:
#I checked all numbers from 100 to 999 and mulilplied each pair.
#Then i used a function to see if the product was a palindrome.
#If it was bigger than the last one I found, I saved it>


def isPalindrome(num):
    """Returns True if num is a palindrome, False otherwise."""
    numStr = str(num)
    return numStr == numStr[::-1]

def largestPalindrome():
    """Finds and returns the largest palindrome from the product of two 3-digit numbers. """
    largest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j 
            if isPalindrome(product) and product > largest:
                largest = product
    return largest 

print("Largest palindrome product:", largestPalindrome())

