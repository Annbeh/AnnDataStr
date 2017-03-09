'''
Created on 9 Mar 2017

@author: annub
'''
from data_structures.set_adt_linked_list import Set
import time
import matplotlib.pyplot as plt

running_times = []

# Increase size of n in increments. 
for n in range (0, 1000, 10):
    s = Set()
    # Add n elements to the set.
    for i in range(n):
        s.add(i)

    start = time.time()
    # Insert operation you want to test here
    end = time.time()

    run_time = end - start
    print(n, run_time)
    running_times.append(run_time)
# Plot the running times
plt.plot(running_times, 'bx')
plt.xlabel('Size of N (x 1000)')
plt.ylabel('Time')
plt.show()

