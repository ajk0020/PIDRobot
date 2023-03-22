import time
t0= time.time_ns()
print("Hello")
t1 = time.time_ns() - t0
print("Time elapsed: ", t1) # CPU seconds elapsed (floating point)