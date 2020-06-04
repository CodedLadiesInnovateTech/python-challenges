"""
1. Arrange integers (0 to 99) as narrow hilltop, as illustrated in Figure 1. Reading such data representing huge, when starting from the top and proceeding according to the next rule to the bottom. Write a Python program that compute the maximum value of the sum of the passing integers.
Input:
A series of integers separated by commas are given in diamonds. No spaces are included in each line. The input example corresponds to Figure 1. The number of lines of data is less than 100 lines.
Output:
The maximum value of the sum of integers passing according to the rule on one line.
Input the numbers (ctrl+d to exit):
8
4, 9
9, 2, 1
3, 8, 5, 5
5, 6, 3, 7, 6
3, 8, 5, 5
9, 2, 1
4, 9
8
Maximum value of the sum of integers passing according to the rule on one line.
64

2. Write a Python program to find the number of combinations that satisfy p + q + r + s = n where n is a given number <= 4000 and p, q, r, s in the range of 0 to 1000.
Input a positive integer: (ctrl+d to exit)
252
Number of combinations of a,b,c,d: 2731135

3. Write a Python program which adds up columns and rows of given table as shown in the specified figure.
Input number of rows/columns (0 to exit)
4
Input cell value:
25 69 51 26
68 35 29 54
54 57 45 63
61 68 47 59
Result:
25 69 51 26 171
68 35 29 54 186
54 57 45 63 219
61 68 47 59 235
208 229 172 202 811
Input number of rows/columns (0 to exit)

4. Given a list of numbers and a number k, write a Python program to check whether the sum of any two numbers from the list is equal to k or not.
For example, given [1, 5, 11, 5] and k = 16, return true since 11 + 5 is 16.
Sample Output:
True
True
True
False

5. In mathematics, a subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. For example, the sequence (A,B,D) is a subsequence of (A,B,C,D,E,F) obtained after removal of elements C, E, and F. The relation of one sequence being the subsequence of another is a preorder.
The subsequence should not be confused with substring (A,B,C,D) which can be derived from the above string (A,B,C,D,E,F) by deleting substring (E,F). The substring is a refinement of the subsequence.
The list of all subsequences for the word "apple" would be "a", "ap", "al", "ae", "app", "apl", "ape", "ale", "appl", "appe", "aple", "apple", "p", "pp", "pl", "pe", "ppl", "ppe", "ple", "pple", "l", "le", "e", "".
Write a Python program to find the longest word in set of words which is a subsequence of a given string.
Sample Output:
Gren
exercises

6. From Wikipedia, the free encyclopaedia:
A happy number is defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
Write a Python program to check whether a number is "happy" or not.
Sample Output:
True
True

7. From Wikipedia,
A happy number is defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
Write a Python program to find and print the first 10 happy numbers.
Sample Output:
[1, 7, 10, 13, 19, 23, 28, 31, 32, 44]

8. Write a Python program to count the number of prime numbers less than a given non-negative number.
Sample Output:
4
25

9. In abstract algebra, a group isomorphism is a function between two groups that sets up a one-to-one correspondence between the elements of the groups in a way that respects the given group operations. If there exists an isomorphism between two groups, then the groups are called isomorphic.
Two strings are isomorphic if the characters in string A can be replaced to get string B
Given "foo", "bar", return false.
Given "paper", "title", return true.
Write a Python program to check if two given strings are isomorphic to each other or not.
Sample Output:
False
False
True
True
False
False
False

10. Write a Python program to find the longest common prefix string amongst a given array of strings. Return false If there is no common prefix.
For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".
Sample Output:
abc
w3r
P
"""
