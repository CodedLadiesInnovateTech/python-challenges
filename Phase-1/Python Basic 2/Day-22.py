"""

1. Write a Python program to find the difference between the largest integer and the smallest integer which are created by 8 numbers from 0 to 9. The number that can be rearranged shall start with 0 as in 00135668.
Input:
Input an integer created by 8 numbers from 0 to 9.:
2345
Difference between the largest and the smallest integer from the given integer:
3087

2. Write a Python program to compute the sum of first n given prime numbers.
Input:
n ( n = 10000). Input 0 to exit the program.
Input a number (n=10000) to compute the sum:(0 to exit)
25
Sum of first 25 prime numbers:
1060

3. Write a Python program that accept an even number (>=4, Goldbach number) from the user and create a combinations that express the given number as a sum of two prime numbers. Print the number of combinations.
Goldbach number: A Goldbach number is a positive even integer that can be expressed as the sum of two odd primes.[4] Since four is the only even number greater than two that requires the even prime 2 in order to be written as the sum of two primes, another form of the statement of Goldbach's conjecture is that all even integers greater than 4 are Goldbach numbers.
The expression of a given even number as a sum of two primes is called a Goldbach partition of that number. The following are examples of Goldbach partitions for some even numbers:
6 = 3 + 3
8 = 3 + 5
10 = 3 + 7 = 5 + 5
12 = 7 + 5
...
100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53
Input an even number (0 to exit):
100
Number of combinations:
6

4. if you draw a straight line on a plane, the plane is divided into two regions. For example, if you pull two straight lines in parallel, you get three areas, and if you draw vertically one to the other you get 4 areas.
Write a Python program to create maximum number of regions obtained by drawing n given straight lines.
Input:
(1 = n = 10,000)
Input number of straight lines (o to exit):
5
Number of regions:
16

5. There are four different points on a plane, P(xp,yp), Q(xq, yq), R(xr, yr) and S(xs, ys). Write a Python program to test AB and CD are orthogonal or not.
Input:
xp,yp, xq, yq, xr, yr, xs and ys are -100 to 100 respectively and each value can be up to 5 digits after the decimal point It is given as a real number including the number of. Output:
Output AB and CD are not orthogonal! or AB and CD are orthogonal!.

6. Write a Python program to sum of all numerical values (positive integers) embedded in a sentence.
Write a Python program to create maximum number of regions obtained by drawing n given straight lines.
Input:
Sentences with positive integers are given over multiple lines. Each line is a character string containing one-byte alphanumeric characters, symbols, spaces, or an empty line. However the input is 80 characters or less per line and the sum is 10,000 or less.
Input some text and numeric values ( to exit):
Sum of the numeric values: 80
None
Input some text and numeric values ( to exit):
Sum of the numeric values: 17
None
Input some text and numeric values ( to exit):
Sum of the numeric values: 10
None

7. There are 10 vertical and horizontal squares on a plane. Each square is painted blue and green. Blue represents the sea, and green represents the land. When two green squares are in contact with the top and bottom, or right and left, they are said to be ground. The area created by only one green square is called "island". For example, there are five islands in the figure below.
Write a Python program to read the mass data and find the number of islands.
Input:
Input 10 rows of 10 numbers representing green squares (island) as 1 and blue squares (sea) as zeros
1100000111
1000000111
0000000111
0010001000
0000011100
0000111110
0001111111
1000111110
1100011100
1110001000
Number of islands:
5

8. When character are consecutive in a string , it is possible to shorten the character string by replacing the character with a certain rule. For example, in the case of the character string YYYYY, if it is expressed as # 5 Y, it is compressed by one character.
Write a Python program to restore the original string by entering the compressed string with this rule. However, the # character does not appear in the restored character string.
Note: The original sentences are uppercase letters, lowercase letters, numbers, symbols, less than 100 letters, and consecutive letters are not more than 9 letters.
Input:
The restored character string for each character on one line.
Original text: XY#6Z1#4023
XYZZZZZZ1000023
Original text: #39+1=1#30
999+1=1000

9. A convex polygon is a simple polygon in which no line segment between two points on the boundary ever goes outside the polygon. Equivalently, it is a simple polygon whose interior is a convex set. In a convex polygon, all interior angles are less than or equal to 180 degrees, while in a strictly convex polygon all interior angles are strictly less than 180 degrees.
Write a Python program that compute the area of the polygon . The vertices have the names vertex 1, vertex 2, vertex 3, ... vertex n according to the order of edge connections
Note: The original sentences are uppercase letters, lowercase letters, numbers, symbols, less than 100 letters, and consecutive letters are not more than 9 letters.

10. Internet search engine giant, such as Google accepts web pages around the world and classify them, creating a huge database. The search engines also analyze the search keywords entered by the user and create inquiries for database search. In both cases, complicated processing is carried out in order to realize efficient retrieval, but basics are all cutting out words from sentences.
Write a Python program to cut out words of 3 to 6 characters length from a given sentence not more than 1024 characters.
Input:
English sentences consisting of delimiters and alphanumeric characters are given on one line.
Input a sentence (1024 characters. max.)
The quick brown fox
3 to 6 characters length of words:
The quick brown fox
"""
