
### Introduction

The basic idea of Selection Sort is find the smallest element in the unsorted array and add it to the front of the array.
In Selection Sort, we maintain two parts:

- Sorted sub-array
- Unsorted sub-array

In sorted sub-array, all elements are in sorted order and are less than all elements of the unsorted sub-array.

Selection Sort is as follows:

### How the algorithm works
At the beginning, the size of sorted sub-array is 0 and the size of unsorted sub-array is n.

At each step, the size of sorted sub-array increases by 1 and size of unsorted sub-array decreases by 1.

![selection_sort](selection_sort.png)

<small>_Photo curtesy of: [Hackerearth](https://www.hackerearth.com/practice/algorithms/sorting/selection-sort/tutorial/)_</small>

### Python implementation
[You can see my python implementation in here](./selection_sort.py)
### Analysis
![selection_sort_draw](./selection_sort_draw.png)

The time-complexity of finding the smallest element in a list of n elements is `O(n)`. 

**This is true for all worst case, average case and best case.**

therefore, the time complexity in order to find the smallest number at every interation of n elements of in selection sort is `(1+2+...+n−2+n−1)` which will result in time-complexity of `O(n^2)`.

The space complexity of Selection Sort is `O(1)`. This is because we use only constant extra space such as:

- 2 variables to enable swapping of elements.
  One variable to keep track of smallest element in unsorted array.

Selection Sort has an optimal space-complexity as the memory requirements remain same for every input.
