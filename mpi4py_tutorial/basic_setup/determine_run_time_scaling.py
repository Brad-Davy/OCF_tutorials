import subprocess
import time
import matplotlib.pyplot as plt
cm = 1/2.54
# Define the number of cores to test
core_counts = [1, 2, 4]
run_times = []

for cores in core_counts:
    start_time = time.time()
    subprocess.run(["mpirun", "-np", str(cores), "python", "main.py"])
    end_time = time.time()
    run_time = end_time - start_time
    print(cores, run_time)
    run_times.append(run_time)

fig = plt.figure(figsize=(10*cm, 10*cm))
plt.xlabel("Number of cores")
plt.ylabel("Run time (s)")

plt.scatter(core_counts, run_times)
plt.show()