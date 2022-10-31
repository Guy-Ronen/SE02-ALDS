#### Breadth-first search
A breadth-first search is when you inspect every node on a level starting at the top of the tree and then move to the next level. 

Storing the frontier nodes in a queue creates the level-by-level pattern of a breadth-first search. Child nodes are searched in the order they are added to the frontier. The nodes on the next level are always behind the nodes on the current level. Breadth-first search is known as a complete algorithm since no matter how deep the goal is in the tree it will always be located.

Breadth-First Search has a time complexity of O(n) where n is the number of nodes in the tree. In the worst case, we will examine every node of a tree.