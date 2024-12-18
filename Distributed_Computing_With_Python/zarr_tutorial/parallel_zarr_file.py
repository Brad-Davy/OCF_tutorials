from mpi4py import MPI
import numpy as np
import time
import zarr
import sys

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def process_data(data):
    return data**2

z = zarr.open('large_data.zarr', mode='r')
data_shape = z.shape
chunk_size = data_shape[0]//size
chunks = z[:][chunk_size*rank:chunk_size*(rank+1)]

local_data=chunks
processed_data = process_data(local_data)
print('Rank: ', rank, 'Processed data: ', np.shape(processed_data))

import os
import psutil

process = psutil.Process(os.getpid())

print(f"Memory usage: {process.memory_info().rss / 10**6} MB")