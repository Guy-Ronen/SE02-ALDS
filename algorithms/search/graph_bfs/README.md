### Graph Depth-first search

DFS stands for depth-first search. The algorithm starts from the root node of the graph and explores as far as possible along each branch, and then after going at the depth most point possible, it backtracks.


#### Time complexity

Similar to that of BFS time complexity of DFS depends upon the data structure used to store the graph. If it's an adjacency list, then the time complexity is O(V + E); otherwise, if it's an adjacency matrix, the time complexity is O(V ^ 2). 
Reasons are the same as that of BFS as in this also we are traversing each node of the graph.

### Space complexity

We are using a stack to keep track of the last visited node. Thus it would take the size of the number of nodes (vertices) in the tree. Hence, the space complexity is O(V).