from mpi4py import MPI
import h5py
import numpy as np


# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# File name of the HDF5 dataset
file_name = "example.h5"

# Parallel reading
with h5py.File(file_name, "r", driver="mpio", comm=comm) as f:
    # Access the dataset
    dataset = f["/data"]
    
    # Determine the size of the dataset and divide work among ranks
    total_size = dataset.shape[0]
    chunk_size = total_size // size
    remainder = total_size % size

    # Each rank determines its start and end indices
    start = rank * chunk_size + min(rank, remainder)
    end = start + chunk_size + (1 if rank < remainder else 0)

    # Each rank reads its portion of the data
    local_data = dataset[start:end]
    
    print(f"Rank {rank} read data: {local_data}")

# Finalize MPI (not strictly necessary in mpi4py, but good practice)
MPI.Finalize()
