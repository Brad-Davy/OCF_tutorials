import zarr
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 1
plt.rcParams["figure.autolayout"] = True
cm = 1/2.54  # centimeters in inches


def plot_striped_array():
    cores = 1

    # Open the Zarr file
    zarr_file = zarr.open('zarr_files/output_array_{}_cores.zarr'.format(cores), mode='r')

    # Read the array
    array = zarr_file[:]

    # Plot the array using imshow
    figure = plt.figure(figsize=(7.5*cm ,7.5*cm))
    plt.imshow(array, cmap='viridis')
    plt.xticks([0,5000,10000],[0,5000,10000])
    plt.yticks([0,5000,10000],[0,5000,10000])
    plt.savefig('img/striped_zarr_array_{}.svg'.format(cores), dpi=300)
    plt.show()

def plot_memory_usage():
    cores = [1,2,3,4]
    memory_per_core = [468, 267, 200, 166]
    standard_np_memory_per_core = [458, 458, 458, 458]
    figure = plt.figure(figsize=(9*cm ,12*cm))
    plt.scatter(cores, memory_per_core, color='black', marker = 'v', s=100, label = 'Zarr')
    plt.scatter(cores, standard_np_memory_per_core, color='orange', marker = 'v', s=100, label = 'Numpy')
    plt.axhline(y=400, color='red', linestyle='--', label='400 MB')
    plt.ylim(0,600)
    plt.legend(ncol=1, frameon=False)
    plt.xticks(cores, cores)
    plt.xlabel('Number of cores')
    plt.ylabel('Memory usage per core (MB)')
    plt.savefig('img/memory_usage_per_core.svg', dpi=500)
    plt.show()

plot_memory_usage()