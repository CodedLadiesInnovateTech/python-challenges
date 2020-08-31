"""
Python Challenges - 1 [ 41 Challenges ]

1. Write a Python program to check if a given positive integer is a power of two.
Input : 4
Output : True

2. Write a Python program to check if a given positive integer is a power of three.
Input : 9
Output : True

3. Write a Python program to check if a given positive integer is a power of four.
Input : 4
Output : True

4. Write a Python program to check if a number is a perfect square.
Input : 9
Output : True

5. Write a Python program to check if an integer is the power of another integer
Input : 16, 2
Output : True

6. Write a Python program to check if a number is a power of a given base
Input : 128,2
Output : True

7. Write a Python program to find a missing number from a list.
Input : [1,2,3,4,6,7,8]
Output : 5

8. Write a Python program to find missing numbers from a list.
Input : [1,2,3,4,6,7,10]
Output : [5, 8, 9]

9. Write a Python program to find three numbers from an array such that the sum of three numbers equal to zero.
Input : [-1,0,1,2,-1,-4]
Output : [[-1, -1, 2], [-1, 0, 1]]
Note : Find the unique triplets in the array.

10. Write a Python program to find three numbers from an array such that the sum of three numbers equal to a given number
Input : [1, 0, -1, 0, -2, 2], 0)
Output : [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

11. Write a Python program to compute and return the square root of a given 'integer'.
Input : 16
Output : 4
Note : The returned value will be an 'integer'

12. Write a Python program to find the single number in a list that doesn't occur twice
Input : [5, 3, 4, 3, 4]
Output : 5

13. Write a Python program to find the single element in a list where every element appears three times except for one
Input : [5, 3, 4, 3, 5, 5, 3]
Output : 4

14. Write a Python program to find the single element appears once in a list where every element appears four times except for one.
Input : [1, 1, 1, 2, 2, 2, 3]
Output : 3

15. Write a Python program to find two elements appear twice in a list where all the other elements appear exactly twice in the list.
Input : [1, 2, 1, 3, 2, 5]
Output :[5, 3]

16. Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.
Input : 48
Output : 3
For example given number is 59, the result will be 5.
Step 1: 5 + 9 = 14
Step 1: 1 + 4 = 5

17. Write a Python program to find whether it contains an additive sequence or not.
The additive sequence is a sequence of numbers where the sum of the first two numbers is equal to the third one.
Sample additive sequence: 6, 6, 12, 18, 30
In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
Also, you can split a number into one or more digits to create an additive sequence.
Sample additive sequence: 66121830
In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
Note : Numbers in the additive sequence cannot have leading zeros.


 
18. Write a Python program to reverse the digits of an integer.
Input : 234
Input : -234
Output: 432
Output : -432

19. Write a Python program to reverse the bits of an integer (32 bits unsigned).
Input : 1234
Output : 1260388352
For example, 1234 represented in binary as 10011010010 and returns 1260388352 which represents in binary as 1001011001000000000000000000000.

20. Write a Python program to check a sequence of numbers is an arithmetic progression or not.
Input : [5, 7, 9, 11]
Output : True
In mathematics, an arithmetic progression or arithmetic sequence is a sequence of numbers such that the difference between the consecutive terms is constant.
For example, the sequence 5, 7, 9, 11, 13, 15 ... is an arithmetic progression with common difference of 2.

21. Write a Python program to check a sequence of numbers is a geometric progression or not.
Input : [2, 6, 18, 54]
Output : True
In mathematics, a geometric progression or geometric sequence is a sequence of numbers where each term after the first is found by multiplying the previous one by a fixed, non-zero number called the common ratio.
For example, the sequence 2, 6, 18, 54, ... is a geometric progression with common ratio 3. Similarly, 10, 5, 2.5, 1.25, ... is a geometric sequence with common ratio 1/2.

22. Write a Python program to compute the sum of the two reversed numbers and display the sum in reversed form.
Input : 13, 14
Output : 27
Note : The result will not be unique for every number for example 31 is a reversed form of several numbers of 13, 130, 1300 etc. Therefore all the leading zeros will be omitted

23. Write a Python program where you take any positive integer n, if n is even, divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the process until you reach 1.
Input : 12
Output : [12, 6.0, 3.0, 10.0, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0]
According to Wikipedia, the Collatz conjecture is a conjecture in mathematics named after Lothar Collatz, who first proposed it in 1937. The conjecture is also known as the 3n + 1 conjecture.
The conjecture can be summarized as follows. Take any positive integer n. If n is even, divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the process (which has been called "Half Or Triple Plus One") indefinitely. The conjecture is that no matter what number you start with, you will always eventually reach 1.
Example :
For instance, starting with n = 12, one gets the sequence 12, 6, 3, 10, 5, 16, 8, 4, 2, 1.
n = 19, for example, takes longer to reach 1: 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.

24. Write a Python program to check whether a given number is an ugly number.
Input : 12
Output : True
Ugly numbers are positive numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...
shows the first 10 ugly numbers.
Note: 1 is typically treated as an ugly number

25. Write a Python program to get the Hamming numbers upto a given numbers also check whether a given number is an Hamming number.
Input : 7
Output : 0
Hamming numbers are numbers of the form
H = 2i x 3j x 5k
Where i, j, k = 0
The sequence of Hamming numbers 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27. . . consists of all numbers of the form 2i.3j.5k where i, j and k are non-negative integers.

26. Write a Python program to check if a given string is an anagram of another given string.
Input : 'anagram','nagaram'
Output : True
According to Wikipedia an anagram is direct word switch or word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; for example, the word anagram can be rearranged into nag-a-ram

27. Write a Python program to push all zeros to the end of a list.
Input : [0,2,3,4,6,7,10]
Output : [2, 3, 4, 6, 7, 10, 0]

28. Write a Python program to the push the first number to the end of a list.

29. Write a Python program to find majority element in a list.
Input : [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]
Output : 5
Note: The majority element is the element that appears more than n/2 times where n is the number of elements in the list.

30. Write a Python program to find the length of the last word.
Input : Python Exercises
Output : 9

31. Write a Python program to add two binary numbers.
Input : ('11', '1')
Output : 100

32. Write a Python program to find the single number which occurs odd numbers and other numbers occur even number.

33. Write a Python program to compute the sum of all the multiples of 3 or 5 below 500.
All the natural numbers below 12 that are multiples of 3 or 5, we get 3, 5, 6, 9 and 10. The sum of these multiples is 33.

34. Write a Python program to compute the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed one million.
Note: Fibonacci series is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

35. Write a Python program to find the largest prime factor of a given number.
The prime factors of 330 are 2, 3, 5 and 11. Therefore 11 is the largest prime factor of 330.

36. Write a Python program to find the largest palindrome made from the product of two 4-digit numbers.
According Wikipedia - A palindromic number or numeral palindrome is a number that remains the same when its digits are reversed. Like 16461, for example, it is "symmetrical". The term palindromic is derived from palindrome, which refers to a word (such as rotor or racecar) whose spelling is unchanged when its letters are reversed. The first 30 palindromic numbers (in decimal) are: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202,...
The largest palindrome made from the product of two 3-digit numbers is 913 * 993 = 906609.
Note: 9999 * 9901 = 906609

37. Write a Python program to find the smallest positive number that is evenly divisible by all of the numbers from 1 to 30.
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
Result: 2329089562800.0

38. Write a python program to find the difference between the sum of the squares of the first two hundred natural numbers and the square of the sum.
The sum of the squares of the first twenty natural numbers is,
12+22+32+.....+202 = 2870
The square of the sum of the first twenty natural numbers is,
(1 + 2 + ... + 10)2 = 44100
Hence the difference between the sum of the squares of the first twenty natural numbers and the square of the sum is 44100 - 2870 = 41230 Output: 401323300

39. Write a python program to find the 1000th prime number.
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. By Euclid's theorem, there are an infinite number of prime numbers. Subsets of the prime numbers may be generated with various formulas for primes. The first twenty prime numbers are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71.

40. Write a Python program to find the product xyz.
A Pythagorean triple consists of three positive integers a, b, and c, such that a2 + b2 = c2. Such a triple is commonly written (a, b, c), and a well-known example is (3, 4, 5). There exists exactly one Pythagorean triplet for which x + y + z = 1000.

41. Write a Python program to find the first triangle number to have over n(given) divisors.
From Wikipedia: A triangular number is a number that is the sum of all of the natural numbers up to a certain number. For example, 10 is a triangular number because 1 + 2 + 3 + 4 = 10. The first 25 triangular numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, and 351.
A triangular number is calculated by the equation: n(n+1)/2
The factors of the first five triangle numbers:
1: 1
3: 1, 3
6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
In the above list 6 is the first triangle number to have over four divisors.

"""