# Linear Search 
Linear search is an algoritem we can use to search for an element through an array.

## Analysis 
At each step, it compares the element at the index to the elememt we want to find. Once we found the element or we went through the entire array without finding the element - the algoritm finishes.

- Best case: We found the array at the first try - _O(1)_
- Worst case: We traversed through the entire array and couldnt find the element. in an array of 5 elemets it will be: 
5 -> 4 -> 3 -> 2 -> 1.

5 iteration for a 5 size array results in a linear time complexity - _O(n)_