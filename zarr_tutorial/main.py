############################################
# Zarr supports chunked, compressed, N-dimensional arrays
# NumPy arrays are memory-bound, meaning they must fit entirely in memory.
# Loading and processing very large datasets is infeasible with standard Python tools.
# Zarr’s chunked storage and on-demand loading allow working with datasets much larger than 
# available memory.
# Zarr's chunking and compression mechanisms enable faster read/write operations compared to 
# directly reading/writing raw files (e.g., CSV, NumPy .npy files).
# Zarr is a game-changer for handling large, multidimensional datasets. Its efficiency, 
# flexibility, and ecosystem support make it superior to standard Python tools for large-scale 
# and high-performance data tasks.
############################################

import zarr
import numpy as np
import sys

z = zarr.open('large_data.zarr', mode='r')
numpy_array = np.zeros((10000, 10000), dtype='f4', order='C')
chunk = z[1000:2000, 1000:2000]

print(sys.getsizeof(chunk))
print(sys.getsizeof(numpy_array))
print(sys.getsizeof(z[:]))
print(z.shape)




