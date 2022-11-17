# Table of Contents

- [Introduction](#introduction)
- [How the algorithm works](#how-the-algorithm-works)
- [Python implementation](#python-implementation)
- [Analysis](#analysis)

### Introduction

BFS stands for breadth-first search. It starts from the root of the given graph and then traverse all nodes at the current depth level before moving on to nodes at the next depth level.

![graph_bfs](graph_bfs.png)
<small>_Photo curtesy of: [freeCodeCamp](https://www.freecodecamp.org/news/breadth-first-search-a-bfs-graph-traversal-guide-with-3-leetcodeexamples/)_</small>

### How the algorithm works
BFS selects a single node (initial or source point) in a graph and then visits all the nodes adjacent to the selected node. BFS accesses these nodes one by one.

The visited and marked data is placed in a queue by BFS. A queue works on a first in first out basis. Hence, the element placed in the graph first is deleted first.

### Python implementation
[You can see my python implementation in here](./graph_bfs.py)

### Analysis
![new_graph_bfs_draw](./new_graph_bfs_draw.png)
The time complexity of BFS depends upon the data structure used to store the graph.

If, for example, an adjacency list is used to store the graph.

In adjacency, the list node keeps track of all of its neighboring edges. Let's say that there are V nodes and E edges in the graph.

We can find all the neighbors of a node just by traversing its adjacency list only once, that too in linear time.

The sum of the sizes of the adjacency lists of all nodes in a directed graph is E. Thus, for a directed graph, the time complexity is O(V) + O(E) = `O(V + E)`.

In an undirected graph, each edge appears twice. Once at either end of the adjacency list for the edge. Thus, in this case, the time complexity is O(V) + O (2E) ~ `O(V + E)`.

If we use an adjacency matrix to store the graph, then.

To find all the neighboring nodes, we have to traverse a full row of length V in the matrix.

Each row in an adjacency matrix corresponds to a node in the graph, and each row stores information about the edges that emerge from that node. As a result, in this situation, the time complexity of BFS is O(V * V) = `O(V ^ 2)`.

Because we're using a queue (FIFO architecture) to keep track of the visited nodes, the queue would take the size of the graph's nodes (or vertices). As a result, the space complexity is `O (V)`.