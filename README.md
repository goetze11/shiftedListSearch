README 
shiftedListSearch 
2/5/2018

--------
Problem
--------
Description: I was given a "shifted" list of integers. At a random index, the 
initial list was split, and the second half of the list was placed in front of
the first half in a new list. The order of the integers within the first and 
second half were both maintained. The goal of this coding assignment was to 
find the largest integer in the array, or in other words, the point where the 
two halves of the initial list were joined. 

--------
Solution
--------
Description: To solve this problem, I used recursion. I continually split the
list in half and compared the first and middle element. If the middle element
was greater than the first element, I knew that the entire first half of the 
list was in proper order, and was able to eliminiate that part of the list as 
a possible location for my target element. I recursively called the method with
smaller and smaller lists until the list contained only the largest element - 
my target element. 

----------
Reasoning
----------
Description: I decided to use recursion because I had a problem that was 
easily divided into smaller sub problems. This seemed to be a simpler and 
more efficient solution than the iterative alternative. However, recursion
does create a larger stack, which could be a potential problem for very
large lists. 

----------
Questions
----------
1. Some possible edge cases that need to be accounted for are: an empty list, 
a list with only one element, a list with non-unique elements, or something
that is not a list

2. The growth implications of my algorithm are not excessive because I do not
make unnecessary copies. Python list slicing does not copy a list, and so the
memory consumption is good. The time complexity of my algorithm is O(log(n)), 
since the problem is cut in half each time. 

3. If our initial list contained 1 million elements, a more effective solution
might involve multithreading. If the list could be split up into smaller
lists, each of them could be run simultaenously on separate threads, and
the results could be combined at the end to discover where the largest
element was. 
 
------------
Link to Code
------------
https://github.com/goetze11/shiftedListSearch.git