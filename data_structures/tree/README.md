### Trees

Trees are an essential data structure for storing hierarchical data with a directed flow.

Similar to linked lists and graphs, trees are composed of nodes which hold data. Nodes also store references to zero or more other tree nodes. Data moves down from node to node. We depict those references as lines drawn between rectangles.

- `root:` A node which has no parent. One per tree.
- `parent:` A node which references other nodes.
- `child:` Nodes referenced by other nodes.
- `sibling:` Nodes which have the same parent.
- `leaf:` Nodes which have no children.
- `level:` The height or depth of the tree. Root nodes are at level 1, their children are at level 2, and so on.

#### Operations (Binary tree)
- Insert: For inserting element as left child of 2, we have to traverse all elements. Therefore, insertion in binary tree has worst case complexity of O(n).
- Delete: For deletion of element 2, we have to traverse all elements to find 2 (assuming we do breadth first traversal). Therefore, deletion in binary tree has worst case complexity of O(n).
- Search:  For searching element 2, we have to traverse all elements (assuming we do breadth first traversal). Therefore, searching in binary tree has worst case complexity of O(n).

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
