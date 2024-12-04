import matplotlib.pyplot as plt
import numpy as np
from mpi4py import MPI
import zarr
import sys

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define Zarr array dimensions and chunk size
zarr_shape = (10000, 10000)
chunk_size = zarr_shape[1] // size

# Create a Zarr array in write mode
store = zarr.DirectoryStore('zarr_files/output_array_{}_cores.zarr'.format(size))  # Save as a directory on disk
zarr_array = zarr.open(store, mode='w', shape=zarr_shape, chunks=(10000, chunk_size), dtype='f4')

# Each rank processes its chunk of the Zarr array
local_start = chunk_size * rank
local_end = chunk_size * (rank + 1)

# Fill the local data with the rank value
local_data = np.zeros((zarr_shape[0], chunk_size), dtype='f4')
local_data[:] = rank  # Each rank fills its chunk with its rank value

# Write back the local data to the Zarr array
zarr_array[:, local_start:local_end] = local_data


import os
import psutil

process = psutil.Process(os.getpid())

print(f"Memory usage: {process.memory_info().rss / 10**6} MB")