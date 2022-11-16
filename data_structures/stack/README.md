# Table of content:

[TOC]

## Introduction

A stack is a data structure which contains an ordered set of data.

Stacks mimic a physical “stack” of objects. Consider a set of gym weights:

Each plate has a weight (the data). The first plate you add, or push, onto the floor is both the bottom and top of the stack. Each weight added becomes the new top of the stack. The last plate that you put down becomes the first, and only, one that you can access.

Stacks can be implemented using a linked list as the underlying data structure because it’s more efficient than a list or array.

Depending on the implementation, the top of the stack is equivalent to the head node of a linked list and the bottom of the stack is equivalent to the tail node.

This is a Last In, First Out or LIFO structure. A less frequently used term is First In, Last Out, or FILO.

![stack](stack.webp)
<small>_Photo curtesy of: [Progamiz](https://www.programiz.com/dsa/stack)_</small>

## Possible operations
Stacks provide three methods for interaction:

- Push - adds data to the “top” of the stack
- Pop - returns and removes data from the “top” of the stack
- Peek - returns data from the “top” of the stack without removing it.


### Advantages
- Stack helps in managing data that follows the LIFO technique.
- Stacks are be used for systematic Memory Management.
It is used in many virtual machines like JVM.
- When a function is called, the local variables and other function parameters are stored in the stack and automatically destroyed once returned from the function. Hence, efficient function management.
- Stacks are more secure and reliable as they do not get corrupted easily.
- Stack allows control over memory allocation and deallocation.
- Stack cleans up the objects automatically.

## Disadvantages
- Stack memory is of limited size.
- The total of size of the stack must be defined before.
- If too many objects are created then it can lead to stack overflow.
- Random accessing is not possible in stack.
- If the stack falls outside the memory it can lead to abnormal termination.


## Use Cases
- CD/DVD stand.
- Stack of books in a book shop.
- Undo and Redo mechanism in text editors.
- The history of a web browser is stored in the form of a stack.
- Call logs, E-mails, and Google photos in any gallery are also stored in form of a stack.
- YouTube downloads and Notifications are also shown in LIFO format(the latest appears first).
## Python implementation

[You can see my python implementation in here](./stack.py)

## Time complexities

- Access: O(n)
- Insert: O(1)
- Delete: O(1)
- Search: O(n)
