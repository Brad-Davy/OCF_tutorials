import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from main import monitor

job_monitor = monitor(3328)
intial_memory = job_monitor.get_memory_usage()

# Initialize the figure and axis
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10, 6))
xdata, ydata = [i for i in range(60)], [50]*60
ln, = ax1.plot([0,1], [0,1], 'ro')
xdata2, ydata2 = [i for i in range(60)], [intial_memory / 1e6]*60
ln2, = ax2.plot([0,1], [0,1], 'bo')

def init():
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('CPU Usage (%)')
    ax1.set_xlim(0, 60)
    ax1.set_ylim(0, 100)

    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Memory Usage Mb')
    ax2.set_xlim(0, 60)
    ax2.set_ylim(0, 2 * intial_memory / 1e6)

    return ln, ln2

def update(frame):

    ## change this logic to pop from the start of the list and append to the end

    ydata.append(job_monitor.get_cpu_usage())
    ydata.pop(0)

    ydata2.append(job_monitor.get_memory_usage() / 1e6)
    ydata2.pop(0)
    
    ln.set_data(xdata, ydata)
    ln.set_linestyle('-')
    ln.set_color('r')
    ln.set_markersize(1)
    ln2.set_data(xdata2, ydata2)
    ln2.set_linestyle('-')
    ln2.set_color('b')
    ln2.set_markersize(1)


    return ln, ln2

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 60, 60),
                              init_func=init, blit=True, interval=10)

plt.show()