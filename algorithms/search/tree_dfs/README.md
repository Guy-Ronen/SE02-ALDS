# Table of Contents

- [Introduction](#introduction)
- [How the algorithm works](#how-the-algorithm-works)
- [Python implementation](#python-implementation)
- [Analysis](#analysis)
### Introduction 
A depth-first search is where you search deep into a branch and don’t move to the next one until you’ve reached the end.

Frontier nodes stored in a stack create the deep dive of a depth-first search. Nodes added to the frontier early on can expect to remain in the stack while their sibling’s children (and their children, and so on) are searched. Depth-first search is not considered a complete algorithm since searching an infinite branch in a tree can go on forever. In this situation, an entire section of the tree would be left un-inspected.
### How the algorithm works
The algotithm picks a starting node and push all its adjacent nodes into a stack.
Then, it pops a node from stack in order to select the next node to visit and pushes all its adjacent nodes into a stack.
It repeats this process until the stack is empty. 
However, it ensures that the nodes that are visited are marked. This prevents the algorithm from visiting the same node more than once.

![tree_dfs](tree_dfs.webp)
<small>_Photo curtesy of: [Tutorial horizon](https://algorithms.tutorialhorizon.com/depth-first-searchtraversal-in-binary-tree/)_</small>


### Python implementation
[You can see my python implementation in here](./tree_dfs.py)
### Analysis
![tree_dfs_draw](./tree_dfs_draw.png)

- Best Case: Depth-First Search has a time complexity of `O(1)` if the first node was the target. 

- Worst Case: Depth-First Search has a time complexity of `O(n)` where n is the number of nodes in the tree. In the worst case, we will examine every node of a tree.