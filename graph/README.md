# Graph

<!-- Short summary or background information -->
Graphs in data structures are non-linear data structures made up of a finite number of nodes or vertices and the edges
that connect them. Graphs in data structures are used to address real-world problems in which it represents the problem
area as a network like telephone networks, circuit networks, and social networks. For example, it can represent a single
user as nodes or vertices in a telephone network, while the link between them via telephone represents edges.

## Challenge

<!-- Description of the challenge -->
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following
methods:

- add node
  - Arguments: value
  - Returns: The added node 
  - Add a node to the graph 
- add edge 
  - Arguments: 2 nodes to be connected by the edge, weight (optional)
  - Returns: nothing 
  - Adds a new edge between two nodes in the graph 
  - If specified, assign a weight to the edge 
  - Both nodes should already be in the Graph 
- get nodes 
  - Arguments: none 
  - Returns all of the nodes in the graph as a collection (set, list, or similar)
- get neighbors 
  - Arguments: node 
  - Returns a collection of edges connected to the given node 
  - Include the weight of the connection in the returned collection 
- size 
  - Arguments: none
  - Returns the total number of nodes in the graph

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

- Time Complexity:
    - add node: O(1)
    - add edges: O(1)
    - get neighbors :O(n)
    - get nodes:O(n)
    - size:O(1)

- Space Complexity:
    - add node: O(n)
    - add edges: O(n)
    - get neighbors :O(n)
    - get nodes:O(n)
    - size:O(1)



[Code](https://github.com/muhammadqasemtarboush1/data-structures-and-algorithms/blob/main/graph/graph.py)
[Test](https://github.com/muhammadqasemtarboush1/data-structures-and-algorithms/blob/main/tests/test_graph.py)


> For testing
>
> you can run :
>
> pytest -v
>
> or
>
>  pytest .\tests\test_graph.py


