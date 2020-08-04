'''
1. Write a Python program for counting sort.
According to Wikipedia "In computer science, counting sort is an algorithm for sorting a collection of objects according to keys that are small integers; that is,
it is an integer sorting algorithm. It operates by counting the number of objects that have each distinct key value, and using arithmetic on those counts to determine
the positions of each key value in the output sequence. Its running time is linear in the number of items and the difference between the maximum and minimum key values,
so it is only suitable for direct use in situations where the variation in keys is not significantly greater than the number of items. However, it is often used as a 
subroutine in another sorting algorithm, radix sort, that can handle larger keys more efficiently".

2. Write a Python code to create a program for Bitonic Sort.
Bitonic Sort: According to rutgers.edu - Bitonic sort is a comparison-based sorting algorithm that can be run in parallel. 
It focuses on converting a random sequence of numbers into a bitonic sequence, one that monotonically increases, then decreases. 
Rotations of a bitonic sequence are also bitonic. More specifically, bitonic sort can be modelled as a type of sorting network.
The initial unsorted sequence enters through input pipes, where a series of comparators switch two entries to be in either increasing or decreasing order.
The algorithm, created by Ken Batcher in 1968, consists of two parts. First, the unsorted sequence is built into a bitonic sequence; then, the series is split multiple
times into smaller sequences until the input is in sorted order.

3. Write a Python program to sort a list of elements using Bogosort sort.
In computer science, Bogosort is a particularly ineffective sorting algorithm based on the generation and test paradigm. 
The algorithm successively generates permutations of its input until it finds one that is sorted. It is not useful for sorting,
but may be used for educational purposes, to contrast it with other more realistic algorithms. Two versions of the algorithm exist:
a deterministic version that enumerates all permutations until it hits a sorted one, and a randomized version that randomly permutes its input.
An analogy for the working of the latter version is to sort a deck of cards by throwing the deck into the air, picking the cards up at random, 
and repeating the process until the deck is sorted. Its name comes from the word bogus.
'''
