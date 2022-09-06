# What is a node?

Nodes are the fundamental building blocks of many computer science data structures. They form the basis for linked lists, stacks, queues, trees, and more.

Nodes contain 2 things: 
1. Data: String, Integer, Decimal, array, etc.
2. A pointer to the next node

Typically, data structures implement nodes with one or more links. If these links are null, it denotes that you have reached the end of the particular node or link path you were previously following.


## Node linking
Often, due to the data structure, nodes may only be linked to a single other node. This makes it very important to consider how you implement modifying or removing nodes from a data structure.