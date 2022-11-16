## Table of content:

[TOC]

### Introduction

A queue is a data structure which contains an ordered set of data.

This data structure mimics a physical queue of objects like a line of people buying movie tickets. Each person has a name (the data). The first person to enqueue, or get into line, is both at the front and back of the line. As each new person enqueues, they become the new back of the line.

Queues can be implemented using a linked list as the underlying data structure. The front of the queue is equivalent to the head node of a linked list and the back of the queue is equivalent to the tail node.

Since operations are only allowed to affect the front or back of the queue, any traversal or modification to other nodes within the linked list is disallowed. Since both ends of the queue must be accessible, a reference to both the head node and the tail node must be maintained.

_The first person in the queue is the first to be served. Queues are a First In, First Out or FIFO structure._
![queue](queue.png)

<small>_Photo curtesy of: [Geeksforgeeks](https://www.geeksforgeeks.org/queue-data-structure/)_</small>

### Possible operations

Queues provide three methods for interaction:

1. Enqueue - adds data to the “back” or end of the queue
2. Dequeue - provides and removes data from the “front” or beginning of the queue
3. Peek - reveals data from the “front” of the queue without removing it.

### Advantages
- A large amount of data can be managed efficiently with ease.
Operations such as insertion and deletion can be performed with ease as it follows the first in first out rule.
Queues are useful when a particular service is used by multiple consumers.
- Queues are fast in speed for data inter-process communication.
- Queues can be used in the implementation of other data structures.
### Disadvantages

- The operations such as insertion and deletion of elements from the middle are time consuming.
Limited Space.
- In a classical queue, a new element can only be inserted when the existing elements are deleted from the queue.
- Searching an element takes O(N) time.
Maximum size of a queue must be defined prior.
- If a queue has a limit on the amount of data that can be placed into it, it is considered a bounded queue.

- Attempting to enqueue data onto an already full queue will result in a queue overflow. If you attempt to dequeue data from an empty queue, it will result in a queue underflow.

### Use cases
- ATM Booth Line
- Ticket Counter Line
- Key press sequence on the keyboard
- CPU task scheduling
- Waiting time of each customer at call centers.

### Python implementation

[You can see my python implementation in here](./queue.py)

### Time complexities

- Access: O(n)
- Insert: O(1)
- Delete: O(1)
- Search: O(n)
