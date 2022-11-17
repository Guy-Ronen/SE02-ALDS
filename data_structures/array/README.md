# Table of Contents

- [Introduction](#introduction)
- [Possible Operations](#possible-operations)
- [Advantages](#advantages)
- [Disadvantages](#disadvantages)
- [Use Cases](#use-cases)
- [Python Implementation](#python-implementation)
- [Time Complexities](#time-complexities)
### Introduction
Array is a data structure consisting of a collection of elements, each identified by an Index, which can be computed by a mathematical formula. 
An array is stored in contiguous memory blocks.
Array is one of the Most fundamental data structure and the base of other data structures (Graph, Queues, Stacks).

![array](array.jpeg)

<small>_Photo curtesy of: [Lucas Magnum (medium)](https://lucasmagnum.medium.com/sidenotes-array-abstract-data-type-data-structure-b154140c8305)_</small>

### Possible operations
Possible operations you can perform on an array: 
- Traversal
- Insertion
- Deletion
- Searching

### Advantages
- Arrays can store multiple elements of the same type with the same name.
- You can randomly access elements in the array using an index number
- Array memory is predefined, so there is no extra memory loss.
- Arrays avoid memory overflow.

### Disadvantages
- The number of elements in an array should be predfined.
- An array is static. It cannot alter its size after declaration.
- Insertion and deletion in an array is tricky as the array stores elements in continuous form.
- Allocation exess memory than required may lead to memory wastage.

### Use Cases
-  A class of students where every student is the same data-type holding the same information (such as name and average grade)
- A catalog of product where is product has a name and a price. 

### Python Implementation
[You can see my python implementation in here](./array.py)

### Time Complexities
- Access: O(1)
- Search: O(n) 
- Insert: O(n)
- Delete: O(n) 
