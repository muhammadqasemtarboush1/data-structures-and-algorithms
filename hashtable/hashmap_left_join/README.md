# Hashmap LEFT JOIN
<!-- Short summary or background information -->
returns all rows from the left table, even if there are no matches in the right table. This means that if the ON clause matches 0 (zero) records in the right table; the join will still return a row in the result, but with NULL in each column from the right table.

This means that a left join returns all the values from the left table, plus matched values from the right table or NULL in case of no matching join predicate.
## Challenge
<!-- Description of the challenge -->
Write a function that LEFT JOINs two hashmaps into a single data structure.
Write a function called left join
Arguments: two hash maps
The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->


## Solution
<!-- Embedded whiteboard image -->
### Algorithm:
declare new function that takes 2 hashmap

store the keys of the first hashmap in variable

declare new dictionary

iterate over the array 

check if the second hash contains the keys of the first hash:

if yes: Do stor the key and the value of it and get the list of values from the first and second hashmaps 

if not stor the key and the value of the first hashmap and get the rest and replace the second hash values with No_match

return the dictionary

[ Code](https://github.com/muhammadqasemtarboush1/data-structures-and-algorithms/blob/main/hashtable/hashmap_left_join/README.md) 

[Test ](https://github.com/muhammadqasemtarboush1/data-structures-and-algorithms/blob/main/tests/test_hashmap_left_join.py)         


> For testing
>
> you can run :
>
> pytest -v




