import os
from time import sleep
import numpy as np


for i in range(1000):
    array = np.random.rand(10000, 10000)
    pid = os.getpid()
    print(f"Process ID: {pid}") 
    for j in range(1000):
        for i in range(1000):
            for k in range(1000):
                array[i][j] = (array[i][j] * array[i][j])**k
                
