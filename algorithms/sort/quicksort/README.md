# Quicksort 
Quicksort is an algorithm where we pick a random element from the array as the "pivot" and then traverse the array and check if each element is less than or greater than the selected pivot. 

The array get partitioned this way to 2 sub-arrays:
- `less than`: the elements less than the pivot.
-  `more than`: the elements more than the pivot.

Once the first partition is being made, we recursively repeat the process until there's 1 or 0 elements in both `less than` and `more than` sub-array.

Once we have all items paritioned, all items are actully sorted.


### Time complexity
In an evenly distributed paritions to their sub-arrays - we traverse the element n iterations * `log(N)` levels to given n size array (because we always split the array in 2).
That would  result in a time complexity of `O(nlog(n))`

In the worst case, we always pick either the smallest or largest element in each iteration, which will result in all remaining elements to split into the same subarray and result in `n` number on levels for an element for an element size of n. 

That will result in time complexity of n iteration over n level = O(n^2)
