import matplotlib.pyplot as plt
import numpy as np



with open("output.txt") as f:
    data = f.read().splitlines()
    data = [float(i) for i in data]
    fig = plt.figure(figsize=(10, 10))
    plt.xlabel("Number of cores")
    plt.ylabel("Run time (s)")
    plt.plot(np.linspace(0,2*np.pi,100), data)
    plt.show() 