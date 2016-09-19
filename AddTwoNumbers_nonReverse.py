"""
Question: 
What if the the digits in the linked list are stored in non-reversed order? For example:

(3 -> 4 -> 2) + (4 -> 6 -> 5) = 8 -> 0 -> 7 (3→4→2)+(4→6→5)=8→0→7

Pseudocode:
Step 1. Traverse the linked lists and push the elements in two different stacks
Step 2. Pop the top elements from both the stacks 
Step 3. Add the elements (+ any carry from previous additions) and store the carry in a temp variable
Step 4. Create a node with the sum and insert it into beginning of the result list
"""