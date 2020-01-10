'''
Overview:

	Write a program to check whether a given number is an ugly number.

	Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
'''

class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for p in 2, 3, 5:
            while num % p == 0:
                num /= p
        return num == 1