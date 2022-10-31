### Insertion sort

Insertion sort is one of the intutive sorting algorithm and is based on one assumption that a single element is always sorted.

Hence, the first element of array forms the sorted subarray while the rest create the unsorted subarray from which we choose an element one by one and "insert" the same in the sorted subarray. The same procedure is followed until we reach the end of the array.

In each iteration, we extend the sorted subarray while shrinking the unsorted subarray.


#### Steps of the algorithm

- Begin with a list of unsorted elements.
- Iterate through the list of unsorted elements, from the first item to last.
- The current element is compared to the elements in all preceding positions to the left in each step.
- If the current element is less than any of the previously listed elements, it is moved one position to the left.


#### Time complexity


The worst-case (and average-case) complexity of the insertion sort algorithm is `O(n^2)`.

Meaning that, in the worst case, the time taken to sort a list is proportional to the square of the number of elements in the list.

The best-case time complexity of insertion sort algorithm is O(n) time complexity. In this is the case when the list is already in the correct order. There’s only one iteration in this case since the inner loop operation is trivial when the list is already in order.


##### Example
Unsorted list: `[2,13,5,18,14]`

- 1st iteration:

    Key = a[2] = 13

    a[1] = 2 < 13

    Swap, no swap -> `[2,13,5,18,14]`
<br>
- 2nd iteration:
    Key = a[3] = 5
    a[2] = 13 > 5
    Swap 5 and 13 -> `[2,5,13,18,14]`
    - Next, a[1] = 2 < 13
    Swap, no swap -> `[2,5,13,18,14]`
<br>
- 3rd iteration:
    Key = a[4] = 18
    a[3] = 13 < 18,
    a[2] = 5 < 18,
    a[1] = 2 < 18
    Swap, no swap -> `[2,5,13,18,14]`
<br>
- 4th iteration:
    Key = a[5] = 14
    a[4] = 18 > 14
    Swap 18 and 14 -> `[2,5,13,14,18]`
    - Next, a[3] = 13 < 14,
    a[2] = 5 < 14,
    a[1] = 2 < 14
    So, no swap -> `[2,5,13,14,18]`
<br>
- Finally,
the sorted list is `[2,5,13,14,18]`