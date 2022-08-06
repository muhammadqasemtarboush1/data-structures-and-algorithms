# Hashtables

<!-- Short summary or background information -->
It's a data structure that utilize key value pairs. This means every Node or Bucket has
both a key, and a value.

## Challenge
<!-- Description of the challenge -->
Implement a Hashtable Class with the following methods:
- set
- get
- contains
- key
- hash
## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Single-responsibility principle and chaining approach to resolve collisions using Linked list
## API
<!-- Description of each method publicly available in each of your hashtable -->

- HashTable:
  - It is a data structure that uses keys and values to store
    data to provide easy and fast access to its items.
  - Arguments: 
    - size: optional number will specify the length of the array
- HashTable/hash: 
  - Arguments: key 
  - return: index in the collection of buckets for that key.
- HashTable/set: 
  - Arguments: key, value
  - return : nothing
  - functionally: hash the key and set the value and key pair in the buckets,
          also handling the collisions as needed
- HashTable/get: 
  - Arguments: key
  - return : Referenced value by passed key
  - functionally: Used to find the value that is associated with the passed key.
- HashTable/contains:
  - Arguments: key
  - return : True if the key exists in the hashmap, and False if it doesn't exist 
  - functionally: Checks if the key exists in the hashmap
- HashTable/key:
  - Arguments: None
  - Returns: collections of all the keys in hashmap as an object







