# Table of content:
 - Introduction
 - Use cases
 - Advantages
 - Analysis

## Introduction

The list is comprised of a series of nodes. 
The head node is the node at the beginning of the list. Each node contains data and a link (or pointer) to the next node in the list. 
The list is terminated when a node’s link is `null`. This last node is called the tail node.

![linked_list](linked_list.png)
### Use Cases
One example can be a one-way air travel itinerary. The trip could involve traveling through several airports (nodes) connected by air travel segments (links). In this example, the initial departure city is the head node and the final arrival city is the tail node.


### Advantages
Since the nodes use links to denote the next node in the sequence, the nodes are not required to be sequentially located in memory.
 These links also allow for quick insertion and removal of nodes.


### Analysis
-  Adding nodes: Adding a new node to the beginning of the list requires you to link your new node to the current head node. This way, you maintain your connection with the following nodes in the list. This has a time-complexity of `O(1)`


- Removing nodes: If you accidentally remove the single link to a node, that node’s data and any following nodes could be lost to your application, leaving you with orphaned nodes. This has a time-complexity of `O(1)`

- Both traversing and searching will have a time-complexity of `O(n)` at worst case in which we will have to traverse through the entire list