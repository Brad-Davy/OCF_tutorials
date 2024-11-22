from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
size = comm.Get_size()

def simple_process_data(data):
    return np.sin(data)

def complex_process_data(data):
    start_time = MPI.Wtime()
    temporary_data = []
    for lines in data:
        temporary_data.append(np.sin(lines))
    end_time = MPI.Wtime()
    print("Rank", comm.Get_rank(), "took", end_time - start_time, "seconds")
    return temporary_data

if comm.Get_rank() == 0:
    with open('input.txt', 'r') as f:
        data = f.read().split('\n') 
        numeric_data = np.linspace(0, 2*np.pi, 1000000)
        chunk_size = len(numeric_data) // size

if comm.Get_rank() == 0:
    chunks = [numeric_data[i:i + chunk_size] for i in range(0, len(numeric_data), chunk_size)]
else:
    chunks = None

local_data = comm.scatter(chunks, root=0)
processed_data = complex_process_data(local_data)
