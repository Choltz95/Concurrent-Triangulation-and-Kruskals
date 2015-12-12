 === CSC 254 A6: Concurrency ===
Chester Holtz - 28264729 - choltz2@u.rochester.edu
Lee Murphy - 28250920 - lmurp14@u.rochester.edu

In this assignment we were required to implement a generic ordered set abstraction given some base code for an integer set. 

== Source Files ==
README.txt - This file
writeup.pdf - our preformance analysis
MST.java - source to implement test code
Coordinator.java
run - File to build and run the test program

== Description ==
This assignent tasked us with implementing a generic ordered set library in C++. This oset template library contains functionaility for various set operations for elements of arbitrary type. We also implement an iterator to iterate over elements in the set and allow for a comparator to be taken as ordered set constructor parameter.

== Approach ==
This project successfully implements all required components of the assignment. Ordered sets are implemented as linked lists of nodes. Nodes have a value and point to the next element in the ordered set. Iterator operations support prefix and postfix iteration as well as equality checking (==/!=). 

-- Set operations --
Linear time generic set union, difference, and intersection are implemented with a two iterator approach using a while loop. For the union of sets A and B, we initialize iterators i and j for both sets and increment them according to the comparison of values at both iterator positions. If the value of both nodes as position i and j are equal, we increment i and j. If the value of j is greater than that of i we increment i. Otherwise, we increment j and insert the node at position j into the i+1 position of A. Additionally, for union, we also have to deal with the case where A is empty and B contains some elemnts. In this case, since the head of A is a garbage node, we simply return B. For set difference, we can implement the same algorithm, but alter the definition such that if the value of nodes at i (A) and j (B) are equal, we delete the ith node of A and return A after iteration. For intersection, we define a temporary list to add nodes common to both A and B and return the temporary list once we have completed iteration, clearing list A.

--Templating--
To implement our library as a template, we follow the process of defining generic classes and associated methods + parameters, naming our generic type T.

--Non standard comparators--
We provide functionality for non standard comparators by allowing them to be passed as constructor arguments when sets are initialized. 

== Instructions ==
From the command line, type make and run ./oset to run the sample code to test the generic set library.

== Example Output ==
Given the sample code predefined in oset.cc, we get the output:

== Analysis ==
See writeup.pdf