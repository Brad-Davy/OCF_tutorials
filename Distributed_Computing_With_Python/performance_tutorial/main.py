import psutil

class monitor:

    def __init__(self, pid):
        self.pid = pid

    def get_cpu_usage(self):
        try:
            # Get the process object for the given PID
            process = psutil.Process(self.pid)

            # Get the CPU usage percentage of the process
            process_cpu_usage = process.cpu_percent(1)

            print(f"Process {self.pid} CPU Usage: {process_cpu_usage}%")
            # Get the CPU usage percentage per core

            return process_cpu_usage

        except psutil.NoSuchProcess:
            print(f"No process found with PID {self.pid}")
        except KeyboardInterrupt:
            print("Monitoring stopped.")

        
    def get_memory_usage(self):
        try:
            # Get the process object for the given PID
            process = psutil.Process(self.pid)

            # Get the memory usage of the process
            process_memory_usage = process.memory_info().rss

            print(f"Process {self.pid} Memory Usage: {process_memory_usage / 1e6}")
            return process_memory_usage

        except psutil.NoSuchProcess:
            print(f"No process found with PID {self.pid}")
        except KeyboardInterrupt:
            print("Monitoring stopped.")