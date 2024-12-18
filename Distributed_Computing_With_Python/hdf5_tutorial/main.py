import h5py
import numpy as np

############################################
# An HDF5 file is a container for two kinds of objects: datasets, which are array-like 
# collections of data, and groups, which are folder-like containers that hold datasets and 
# other groups. The most fundamental thing to remember when using h5py is:
#
# Groups work like dictionaries, and datasets work like NumPy arrays
#
# Worth noting that it works with different applications like paraview, visit, etc.
############################################

def create_random_data():
    # Create some data
    data = np.random.random(size=(100, 100))

    # Create a new HDF5 file
    with h5py.File('data.h5', 'w') as f:
        # Create a dataset in the file
        f.create_dataset('dataset', data=data)

def create_subgroup():
    # Append to the file
    with h5py.File('data.h5', 'a') as f:
        # Create a group in the file
        grp = f.create_group('subgroup')
        nested_subgroup = grp.create_group('nested_subgroup')
        nested_subgroup.create_dataset('dataset', data=np.random.random(size=(50, 50)))

def read_data():
    # Open the file for reading
    with h5py.File('data.h5', 'r') as f:
        # Read the dataset
        data = f['dataset'][:]
        return data
    
def print_data_set_keys():
    # Open the file for reading
    with h5py.File('data.h5', 'r') as f:
        # Print the keys
        print(type(f['subgroup/nested_subgroup/dataset'].shape))
    
if __name__ == '__main__':   
    data = read_data()
    create_random_data()
    create_subgroup()
    print_data_set_keys()
