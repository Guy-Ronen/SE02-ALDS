# What is a linked list?

The list is comprised of a series of nodes. 
The head node is the node at the beginning of the list. Each node contains data and a link (or pointer) to the next node in the list. 
The list is terminated when a node’s link is `null`. This last node is called the tail node.


## Use Cases
One example can be a one-way air travel itinerary. The trip could involve traveling through several airports (nodes) connected by air travel segments (links). In this example, the initial departure city is the head node and the final arrival city is the tail node.


### Advantage
Since the nodes use links to denote the next node in the sequence, the nodes are not required to be sequentially located in memory.
 These links also allow for quick insertion and removal of nodes.


### Common Operations
- Adding nodes
- Removing nodes
- Finding a node
- Traversing (or traveling through) the linked list

#### 1. Adding nodes
Adding a new node to the beginning of the list requires you to link your new node to the current head node. This way, you maintain your connection with the following nodes in the list.


#### 2. Removing nodes
If you accidentally remove the single link to a node, that node’s data and any following nodes could be lost to your application, leaving you with orphaned nodes.

To properly maintain the list when removing a node from the middle of a linked list, you need to be sure to adjust the link on the previous node so that it points to the following node.


### Time complexities:
- Acess: O(n)
- Search: O(n)
- Insertion: O(1)
- Deletion: O(1)
