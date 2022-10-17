### Trees

Trees are an essential data structure for storing hierarchical data with a directed flow.

Similar to linked lists and graphs, trees are composed of nodes which hold data. Nodes also store references to zero or more other tree nodes. Data moves down from node to node. We depict those references as lines drawn between rectangles.

- `root:` A node which has no parent. One per tree.
- `parent:` A node which references other nodes.
- `child:` Nodes referenced by other nodes.
- `sibling:` Nodes which have the same parent.
- `leaf:` Nodes which have no children.
- `level:` The height or depth of the tree. Root nodes are at level 1, their children are at level 2, and so on.


#### Tree varietals
- Trees come in various shapes and sizes depending on the dataset modeled.
Some are wide, with parent nodes referencing many child nodes.
- Some are deep, with many parent-child relationships.
Trees can be both wide and deep, but each node will only ever have at most one parent; otherwise, they wouldn’t be trees!
- Each time we move from a parent to a child, we’re moving down a level. Depending on the orientation we refer to this as the depth (counting levels down from the root node) or height (counting levels up from a leaf node).


#### Breadth-first search vs. depth-first search 

Each approach has unique characteristics but the process for each one is almost exactly the same. The only difference in their approach is how they store the nodes that need to be searched next. These nodes are known as the frontier.

- The queue and the stack are the two data structures that can be used for storing nodes in a search frontier. A queue follows “First In First Out” (FIFO) behavior, where the order the data goes in the queue is the order it leaves the queue. This equates to any line you may have stood on to wait for the bus or to grab a cup of coffee.

- A stack follows “Last In First Out” (LIFO) behavior which means that the most recent data added will be the first to leave. To get to a book at the bottom of a stack of books you must first remove the books that were more recently placed in the stack.

#### Breadth-first search

- A breadth-first search is when you inspect every node on a level starting at the top of the tree and then move to the next level. 

Storing the frontier nodes in a queue creates the level-by-level pattern of a breadth-first search. Child nodes are searched in the order they are added to the frontier. The nodes on the next level are always behind the nodes on the current level. Breadth-first search is known as a complete algorithm since no matter how deep the goal is in the tree it will always be located.


#### Depth-first search 
- A depth-first search is where you search deep into a branch and don’t move to the next one until you’ve reached the end.

Frontier nodes stored in a stack create the deep dive of a depth-first search. Nodes added to the frontier early on can expect to remain in the stack while their sibling’s children (and their children, and so on) are searched. Depth-first search is not considered a complete algorithm since searching an infinite branch in a tree can go on forever. In this situation, an entire section of the tree would be left un-inspected.

Depth-First Search has a time complexity of O(n) where n is the number of nodes in the tree. In the worst case, we will examine every node of a tree.