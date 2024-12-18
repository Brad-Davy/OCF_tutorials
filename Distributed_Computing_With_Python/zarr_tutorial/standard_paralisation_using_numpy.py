import matplotlib.pyplot as plt
import numpy as np
from mpi4py import MPI
import sys

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = np.ones((10000, 10000), dtype='f4')
data_shape = data.shape
chunk_size = data.shape[1] // size

# Each rank processes its chunk of the Zarr array
local_start = chunk_size * rank
local_end = chunk_size * (rank + 1)

# Write back the local data to the Zarr array
data[:, local_start:local_end] = rank

import os
import psutil

process = psutil.Process(os.getpid())

print(f"Memory usage: {process.memory_info().rss / 10**6} MB")