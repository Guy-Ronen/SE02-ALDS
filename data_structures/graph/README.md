# Table of Contents

- [Introduction](#introduction)
- [Types of Graphs](#types-of-graphs)
- [Weights](#weights)
- [Adjacency Matrix](#adjacency-matrix)
- [Adjacency List](#adjacency-list)
- [Possible Operations](#possible-operations)
- [Advantages](#advantages)
- [Disadvantages](#disadvantages)
- [Use Cases](#use-cases)
- [Python Implementation](#python-implementation)
## Introduction

Graphs are the perfect data structure for modeling networks. They’re composed of nodes, or vertices, which hold data, and edges, which are a connection between two vertices. 
A single node is a vertex.

Some examples for a use of a graph can be a map of the area where you live. As a graph, we could model bus stops as vertices, with bus routes between stops functioning as the edges.

Web pages can be vertices, and the hyperlinks which connect them are edges.

## Types of Graphs:

- **Directed:** a directed graph means that two vertices's are connected in a specific way. the fact that vertex A is connected to B doesn't mean that B is connected to A. Instegram is a practical example for that, the fact that a user following someone, doesn't mean that this someone following him   

- **Undirected:** an undirected graph means that the connection between A to B is the same. A practical example is adding a friend on Facebook, both user sharing the same connection.

## Weights

A weighted graph is a graph where edges have a number or cost associated with traveling between the vertices. When tallying the cost of a path, we add up the total cost of the edges used.

These costs are essential to algorithms that find the shortest distance between two vertices.

![graph](graph.png)

<small>_Photo curtesy of: [@saringyaswift (medium)](https://medium.com/@sarinyaswift/intro-to-the-graph-data-structure-a8277c6a2ad9)_</small>

We typically represent the vertex-edge relationship of a graph in two ways: an adjacency list or an adjacency matrix.
## Adjacency Matrix

An adjacency matrix is a table. Across the top, every vertex in the graph appears as a column. Down the side, every vertex appears again as a row. Edges can be bi-directional, so each vertex is listed twice.

To find an edge between B and P, we would look for the B row and then trace across to the P column. The contents of this cell represent a possible edge.

Our diagram uses 1 to mark an edge, 0 for the absence of an edge. In a weighted graph, the cell contains the cost of that edge.

### Time complexity 

Assuming the graph has `n` vertices, the time complexity to build such a matrix is `O(n^2)`. The space complexity is also `O(n^2)`. Given a graph, to build the adjacency matrix, we need to create a square `n` times `n` matrix and fill its values with 0 and 1. It costs us `O(n^2)` space.

To fill every value of the matrix we need to check if there is an edge between every pair of vertices. That is why the time complexity of building the matrix is `O(n^2)`.

- Advantages: 
1. Good for graph with many edges. 
2. Adjacency matrix allow us to find out if an edge is present in constant time.

- Disadvantages: 
1. It takes a lot of space, since also the non-existing edges are represented by 0. 
2. If we want to find out which vertices are adjacent to a given vertex, you would have to go over all of the row.


## Adjacency List

In an adjacency list, each vertex contains a list of the vertices where an edge exists. To find an edge, one looks through the list for the desired vertex.

### Time Complexity 

If `m` is the number of edges in a graph, then the time complexity of building such a list is `O(m)`. The space complexity is `O(n + m)`. But, in the worst case of a complete graph, which contains `n/2` edges, the time and space complexities reduce to `O(n^2)`.

`Advantages:` 
1. We can get to each vertex's adjacency list in constant time 
2. does not take a lot of space.

## Possible operations
Possible operations you can perform on an graph: 
- Traversal
- Insertion (edge/vertex)
- Deletion (edge/vertex)
- Searching

## Advantages
- By using graphs we can easily find the shortest path, neighbors of the nodes, and many more.
- It is used to find minimum spanning tree which has many practical applications.
- Because of its non-linear structure, helps in understanding complex problems and their visualization.

## Disadvantages
- Graphs use lots of pointers which can be complex to handle.
- It can have large memory complexity. (Adjacency Matrix)
- If the graph is represented with an adjacency matrix then it does not allow parallel edges and multiplication of the graph is also difficult. 
## Use Cases
- Graphs are used in social networking sites where users act as nodes and connection between them acts as edges.
- Graphs are used in Google maps to find the shortest route.
- Graphs are used in solving puzzles with only one solution, such as mazes.

## Python Implementation
[You can see my python implementation in here](./graph.py)