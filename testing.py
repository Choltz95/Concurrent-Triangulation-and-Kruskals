#!/usr/bin/env python

from subprocess import call
from collections import defaultdict
import sys
import os
import random
import time
import re

log = "stats/node_time_log.txt"
_inf = 2147483647
vals = []

def main():
    call("rm stats/node_time_log.txt", shell = True)
    call("javac MST.java", shell = True)
    f = open(log, "a+") # append to file
    nums_threads = [1,2,3,4,6,8,12,16,24,32,48]
    for i in nums_threads:
        print "THREAD: " + str(i)
        for j in range (0,5):
            seed = random.randrange(-_inf,_inf)
            print(j)
            call("java MST -a 0 -t " + str(i)  +" -n 500000 -s "+ str(seed), shell=True, stdout = f)
    f.close()
'''
    regexp = re.compile(r'.*\+.*')
    with open(log) as f:
        lines = f.readlines()
        for line in lines:
            if regexp.search(line):
                vals.append(line.split()[4])
                #print line.split()[4]

    #print vals
    sum = 0.0
    for val in vals:
        sum = sum + float(val)
    print sum/len(vals) # print average
'''
main()
