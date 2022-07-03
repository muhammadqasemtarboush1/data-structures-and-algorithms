# Trees
A Binary search tree (referred to as BST hereafter) is a type of binary tree. 
It can also be defined as a node-based binary tree. BST is also referred to as ‘Ordered Binary
Tree’. In BST, all the nodes in the left subtree have values that are less than the value of 
the root node.

## Challenge
<!-- Description of the challenge -->
Create a Node class that has properties for the value stored in the node, the left child node,
 and the right child node.
Create a Binary Tree class
Define a method for each of the depth first traversals:
pre order
in order
post order which returns an array of the values, ordered appropriately.
Binary Search Tree
Create a Binary Search Tree class
This class should be a sub-class (or your languages equivalent) of the Binary Tree Class

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
> I used the recursion in the binary tree class methods and return the values with hepler function
that returns them in array

> I used the looping way in the binary search tree class its easyer to move around with it and reaching for
 all the data in the tree

Time complexity and Space complexity:
* post_order O(n)/ O(n)
* in_order  O(n) / O(n)
* pre_order  O(n) /O(n)
---
* add O(n) / O(1)
* contains O(n)/ O(1)

## API
<!-- Description of each method publicly available in each of your trees -->
> Binary Tree:
>
> post_order 
> parameters: N/A 
> 
> functionality: post order which returns an array of the values, ordered appropriately.

--- 
> Binary Search Tree:
> 
> add 
> parameters: value 
> 
> functionality: Adds a new node with that value in the correct location in the binary search tree.
>
> contains 
> parameters: value
> 
> functionality: Returns: boolean indicating whether or not the value is in the tree at least once.
> 


---
> For testing
> 
> you can run :
> 
> pytest -v    / 72 test passed 
> 
> or 
> 
>  pytest .\tests\test_binary_tree.py    / 11 test passed 

