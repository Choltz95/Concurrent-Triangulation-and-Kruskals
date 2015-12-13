 === CSC 254 A6: Concurrency ===
Chester Holtz - 28264729 - choltz2@u.rochester.edu
Lee Murphy - 28250920 - lmurp14@u.rochester.edu

In this assignment we were required to implement parallelizations of existing sequential programs written in Java. 

== Source Files ==
README.txt - This file
writeup.pdf - our preformance analysis
MST.java - source to implement test code
Coordinator.java
run - File to build and run the test program

== Description ==
The given program constructs a Delaunay Triangulation from a set of randomized points using Dwyers Algorithm. From the triangulation, we compute the MST of the graph using Kruskal's Algorithm. We implemented parallelized versions of the both of these algorithms and tested the speedup. The timing analysis done for the program is in writeup.txt.

== Instructions ==
From the command line, type javac MST.java and then Java MST with valid command line arguments:

−a  [0123]
    Animation mode. 

    0   (default) =>
        print run time to standard output, but nothing else 
    1 =>
        print list of created, destroyed, and selected (tree) edges, plus run time 
    2 =>
        create a GUI that shows the triangulation and MST, and allow the user to re-run with additional sets of points 
    3 =>
        animate the algorithm on the screen as it runs.  

−n  num
    Number of points.  Default = 50.  More than a couple hundred becomes too dense to look good when animated.  You’ll need to run big numbers (more than 10,000) to get multi-second execution times.  
−s  num
    Seed for pseudorandom number generator.  Every value of the seed produces a different set of points.  
−t  num
    Number of threads (max) that should be running at any given time.  This argument is currently unused; it’s it’s here to support your parallelization efforts.  

== Analysis ==
See writeup.txt