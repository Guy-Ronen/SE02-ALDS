# Table of content:
- Introduction
- How the algorithm works
- Analysis

### Introduction

The basic idea of Selection Sort is find the smallest element in the unsorted array and add it to the front of the array.
In Selection Sort, we maintain two parts:

- Sorted sub-array
- Unsorted sub-array

In sorted sub-array, all elements are in sorted order and are less than all elements of the unsorted sub-array.

Selection Sort is as follows:

#### How the algorithm works
At the beginning, the size of sorted sub-array is 0 and the size of unsorted sub-array is n.

At each step, the size of sorted sub-array increases by 1 and size of unsorted sub-array decreases by 1.

![selection_sort](selection_sort.png)
<small>_Photo curtesy of: [Hackerearth](https://www.hackerearth.com/practice/algorithms/sorting/selection-sort/tutorial/)_</small>
#### Analysis

The time-complexity of finding the smallest element in a list of n elements is `O(n)`. This is constant for all worst case, average case and best case.

Hence, the time complexity of Selection Sort is `O(n^2)`.

The space complexity of Selection Sort is `O(1)`. This is because we use only constant extra space such as:

- 2 variables to enable swapping of elements.
  One variable to keep track of smallest element in unsorted array.

Selection Sort has an optimal space-complexity as the memory requirements remain same for every input.

**Example:**
Unsorted list:`[5 2 1 4 3]`

- 1st iteration:
  Smallest = 5 - 2 < 5, smallest = 2 - 1 < 2, smallest = 1 - 4 > 1, smallest = 1 - 3 > 1, smallest = 1 - Swap 5 and 1 -> `[1 2 5 4 3]`
  <br>
- 2nd iteration:
  Smallest = 2 - 2 < 5, smallest = 2 - 2 < 4, smallest = 2 - 2 < 3, smallest = 2 - No Swap ->`[1 2 5 4 3]`
  <br>

- 3rd iteration:
  Smallest = 5 - 4 < 5, smallest = 4 - 3 < 4, smallest = 3 - Swap 5 and 3 -> `[1 2 3 4 5]`
  <br>

- 4th iteration:
  Smallest = 4 - 4 < 5, smallest = 4 - No Swap -> `[1 2 3 4 5]`
  <br>
- Finally,
  the sorted list is `[1 2 3 4 5]`
