# Binary Search 
Binary search is an algorithm we can use to find an element inside of an array. Unlike linear search, it requires a special condition be met beforehand, but it's so much more efficient if that condition is, in fact, met. 

We want to reduce the size of the search area by half each time in order to find a target number. **We can only leverage the power of eliminating half of the elements without even looking at them if the array is sorted.** 

## Pseudocode
1. Create 3 different variables: 
    1. Left index 
    2. Right index
    3. Midpoint (which is the the combination of both left and right divided by 2)
 - While left end is smaller than right end:

2. Compare whether the element at the midpoint index is equal to the target element.

- If yes - we found our target.
- If not theres 2 options:


    1. If the target element is lower than midpoint - repeat step 1,2 but that the right index is the index of the midpoint -1


    2. If the target element is higher than midpoint - repeat step 1,2 but that the left index is the index of the midpoint + 1


If left > right end - Element is not in the array. 






### Best case: 
We find element at the first midpoint - _O(1)_
### Worst case: 
We didnt find the element, so we keep searching at every iteration at only half the previous one.
In an array of 16 -> 8 -> 4 -> 2 -> 1 - 4 iteration for 16 elements results in logarithmic time complexity-  _O(logn)_



#### Use Cases
- Finding a word in the dictionary.
- Finding a name in a phone book.