# Stacks and Queues
<!-- Short summary or background information -->

Stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle.

Queue is a container of objects (a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle.

## Challenge
<!-- Description of the challenge -->
Challenge Type: New Implementation

* Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
* Create a Stack class that has a top property. It creates an empty Stack when instantiated.
* This object should be aware of a default empty value assigned to top when the stack is created.
* Create a Queue class that has a front property. It creates an empty Queue when instantiated.
* This object should be aware of a default empty value assigned to front when the queue is created.
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* Stack 
  * push: O(1)
  * pop: O(1)
  * peek: O(1)
  * isEmpty: O(1)
* Queue: 
  * enqueue: O(1)
  * dequeue: O(1)
  * peek: O(1)
  * isEmpty: O(1)
## API
<!-- Description of each method publicly available to your Stack and Queue-->

> Stack 
  * push: 
    * functionally: adds a new node with that value to the top of the stack with an O(1) Time performance.
    * parameters: value 
    * return: None
  * pop:
    * functionally: Returns: the value from node from the top of the stack
Removes the node from the top of the stack and raise exception when called on empty stack
    * parameters: None
    * return: the value from node from the top of the stack
  * peek: 
    * functionally: 
    * parameters: None
    * return: Value of the node located at the top of the stack
  * isEmpty:
    * functionally: Checks if the stack is empty
    * parameters: None
    * return:Boolean indicating whether or not the stack is empty.
  
    > Queue:
    * enqueue: 
      * functionally: adds a new node with that value to the back of the queue with an O(1) Time performance.
      * parameters: value
      * return: None
    * dequeue: 
      * functionally: return the value from node from the front of the queue
Removes the node from the front of the queue and  raise exception when called on empty queue
      * parameters: None
      * return: the value from node from the front of the queue
    * peek: 
      * functionally: return the value at the front of the queue and  raise exception when called on empty stack
      * parameters:None
      * return: Value of the node located at the front of the queue
    * isEmpty:
      * functionally: Checks if the queue is empty
      * parameters: N/A
      * return:Boolean indicating whether or not the queue is empty.