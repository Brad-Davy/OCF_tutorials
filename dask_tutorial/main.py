from dask.distributed import Client
import dask.array as da

def main():
    # Start a Dask client
    client = Client()
    client
    # Print the Dask dashboard link
    print(f"Dask dashboard available at: {client.dashboard_link}")

    # Create a large Dask array
    x = da.random.random((10000, 10000), chunks=(1000, 1000))

    # Perform a computation on the Dask array
    result = x.mean().compute()

    # Print the result
    print(f"Mean of the array: {result}")

    # Close the Dask client
    client.close()

if __name__ == "__main__":
    main()