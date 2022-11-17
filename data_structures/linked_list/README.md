# Table of Contents

- [Introduction](#introduction)
- [Possible Operations](#possible-operations)
- [Advantages](#advantages)
- [Disadvantages](#disadvantages)
- [Use Cases](#use-cases)
- [Python Implementation](#python-implementation)
- [Time Complexities](#time-complexities)
## Introduction

The list is comprised of a series of nodes.
The head node is the node at the beginning of the list. Each node contains data and a link (or pointer) to the next node in the list.
The list is terminated when a node’s link is `null`. This last node is called the tail node.

![linked_list](linked_list.png)

<small>_Photo curtesy of: [Geeksforgeeks](https://www.geeksforgeeks.org/data-structures/linked-list/)_</small>

## Possible Operations
Possible operations you can perform on a linked list: 
- Traversal
- Insertion
- Deletion
- Searching
## Advantages

- Since the nodes use links to denote the next node in the sequence, the nodes are not required to be sequentially located in memory.
- These links also allow for quick insertion and removal of nodes.

## Disadvantages
- More memory is required in the linked list as compared to an array. Because in a linked list, a pointer is also required to store the address of the next element and it requires extra memory for itself.
- Traversal: In a Linked list traversal is more time-consuming as compared to an array.For accessing a node at position n, one has to traverse all the nodes before it.


## Use Cases

One example can be a one-way air travel itinerary. The trip could involve traveling through several airports (nodes) connected by air travel segments (links). In this example, the initial departure city is the head node and the final arrival city is the tail node.

## Python Implementation

[You can see my python implementation in here](./linked_list.py)

## Time Complexities

- Insertion: Adding a new node to the beginning of the list requires you to link your new node to the current head node. This way, you maintain your connection with the following nodes in the list. This has a time-complexity of `O(1)`.

- Deletion: If you accidentally remove the single link to a node, that node’s data and any following nodes could be lost to your application, leaving you with orphaned nodes. This has a time-complexity of `O(1)`.

- Traverse/search: both traversing and searching will have a time-complexity of `O(n)` at worst case in which we will have to traverse through the entire list.
