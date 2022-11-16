# Table of content:
[TOC]

### Introduction
Array is a data structure consisting of a collection of elements, each identified by an Index, which can be computed by a mathematical formula. 
An array is stored in contiguous memory blocks.
One of the Most fundamental data structure, the base of other other data structures (Graph, Queues, Stacks)

![array](array.jpeg)
<small>_Photo curtesy of: [Lucas Magnum (medium)](https://lucasmagnum.medium.com/sidenotes-array-abstract-data-type-data-structure-b154140c8305)_</small>
The array main advatnage is tha ability to read data fast, takes only 'one step'. The disadvantage is that an array is static and not dynamic.

### Possible operations
Possible operations you can perform on an array: 
- Traversal
- Insertion
- Deletion
- Searching
- Sorting

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

### Use cases
-  A class of students where every student is the same data-type holding the same information (such as name and average grade)
- A catalog of product where is product has a name and a price. 

### Python implementation
[You can see my python implementation in here](./array.py)

### Time complexities
- Access: O(1)
- Search: O(n) 
- Insert: O(n)
- Delete: O(n) 