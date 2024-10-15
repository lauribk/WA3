My approach:
With a desired time complexity of O(log(m+n)), I knew there must be a divide and conquer/binary searching portion to the problem.
This led me to draw out the arrays and explore how I could possibly find the median with a certain partition.
By chosen approach was to split the arrays and compare the left and right element of the partition to see if both left sides could be only lesser elements and the right be onl larger elements.
This was possible since the arrays given are pre-sorted.
If the partition is not correct, then the partition would change depending on what side was unexpectedly greater/lesser until a correct partition is found.

Challenges:
It was hard for me to make the just from a brute force algorithm with time complexity O(m+n) to the O(log(m+n)) algorithm. I overcame this by spending lots of time working through example visualizations to understand the desired algorithm.
Drawing out the arrays and working through the algorithm helped me find direction. I also used what I knew about log to give my code a divide and conquer direction.

