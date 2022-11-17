# Table of Contents

- [Introduction](#introduction)
- [How the algorithm works](#how-the-algorithm-works)
- [Python implementation](#python-implementation)
- [Analysis](#analysis)
### Introduction

Insertion sort is one of the intutive sorting algorithm and is based on one assumption that a single element is always sorted.

Hence, the first element of array forms the sorted subarray while the rest create the unsorted subarray from which we choose an element one by one and "insert" the same in the sorted subarray. The same procedure is followed until we reach the end of the array.

In each iteration, we extend the sorted subarray while shrinking the unsorted subarray.

### How the algorithm works

- Begin with a list of unsorted elements.
- Iterate through the list of unsorted elements, from the first item to last.
- The current element is compared to the elements in all preceding positions to the left in each step.
- If the current element is less than any of the previously listed elements, it is moved one position to the left.

![insertion_sort](insertion_sort.png)

<small>_Photo curtesy of: [Hackerearth](https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/tutorial/)_</small>

### Python implementation
[You can see my python implementation in here](./insertion_sort.py)
### Analysis
![insertion_sort_draw](./insertion_sort_draw.png)

Insertion sort performs two operations:
1. It scans through the list. 
2. It's comparing each pair of elements, and it swaps elements if they are out of order.
Each operation contributes to the running time of the algorithm. If the input array is already in sorted order, insertion sort compares O(n) elements and performs no swaps.Therefore, in the best case, insertion sort runs in `O(n)` time.

- The worst case for insertion sort will occur when the input list is in decreasing order. To insert the last element, we need at most `n-1` comparisons and at most `n-1` swaps. To insert the second to last element, we need at most `n-2` comparisons and at most `n-2` swaps, and so on. The number of operations will be therefore `2×(1+2+...+n−2+n−1)` - which will result in a worst (and average) time complexity of `O(n^2)`.
