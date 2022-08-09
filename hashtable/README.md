# Hashtables

<!-- Short summary or background information -->
It's a data structure that utilize key value pairs. This means every Node or Bucket has
both a key, and a value.

## Challenge

<!-- Description of the challenge -->
Implement a Hashtable Class with the following methods:

- set:
  - This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
  - Should a given key already exist, replace its value from the value argument given to this method.
- get:
  - Returns: Value associated with that key in the table
- contains:
  - Returns: Boolean, indicating if the key exists in the table already.
- key:
  - Returns: Collection of keys
- hash:
  - Returns: Index in the collection for that key


## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Single-responsibility principle and chaining approach to resolve collisions using Linked list

- Time Complexity:
  - set: O(1)
  - get: O(1)
  - contains:O(1)
  - key:O(1)
  - hash:O(1)

All the above is in best and  in average case but in  worst case they are O(n)

- Space Complexity:
  - set:O(k+ n)
  - get:O(k + n)
  - contains:O(k+ n)
  - key:O(n)
    - hash:O(k+n)
    - 
K is the size of the hashmap and n number of items they are in.
  - item: nodes from the linked_list not in the hash table

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







