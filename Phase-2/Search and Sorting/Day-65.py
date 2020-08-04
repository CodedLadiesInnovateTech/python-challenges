'''
1. Write a Python program to sort a list of elements using Gnome sort.
Gnome sort is a sorting algorithm originally proposed by Dr. Hamid Sarbazi-Azad (Professor of Computer Engineering at Sharif University of Technology) 
in 2000 and called "stupid sort" (not to be confused with bogosort), and then later on described by Dick Grune and named "gnome sort". 
The algorithm always finds the first place where two adjacent elements are in the wrong order, and swaps them.
It takes advantage of the fact that performing a swap can introduce a new out-of-order adjacent pair only next to the two swapped elements.

2. Write a Python program to sort a list of elements using Cocktail shaker sort.
From Wikipedia, Cocktail shaker sort,[1] also known as bidirectional bubble sort,[2] cocktail sort, 
shaker sort (which can also refer to a variant of selection sort), ripple sort, shuffle sort,[3] or shuttle sort,
is a variation of bubble sort that is both a stable sorting algorithm and a comparison sort.
The algorithm differs from a bubble sort in that it sorts in both directions on each pass through the list.
This sorting algorithm is only marginally more difficult to implement than a bubble sort, and solves the problem of turtles in bubble sorts. 
It provides only marginal performance improvements, and does not improve asymptotic performance; 
like the bubble sort, it is not of practical interest (insertion sort is preferred for simple sorts), though it finds some use in education.

3. Write a Python program to sort a list of elements using Comb sort.
The Comb Sort is a variant of the Bubble Sort. Like the Shell sort, the Comb Sort increases the gap used in comparisons and exchanges.
Some implementations use the insertion sort once the gap is less than a certain amount. The basic idea is to eliminate turtles, or small values near the end of the list, 
since in a bubble sort these slow the sorting down tremendously. Rabbits, large values around the beginning of the list do not pose a problem in bubble sort.
In bubble sort, when any two elements are compared, they always have a gap of 1. The basic idea of comb sort is that the gap can be much more than 1.
'''
