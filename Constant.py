import matplotlib.pyplot as plt
import timeit

def access_element(array, index):
    return array[index]

# Example usage
array_sizes = [10, 100, 1000, 10000, 100000]  # Different sizes of the array
execution_times = []

for size in array_sizes:
    my_array = list(range(size))
    execution_time = timeit.timeit(lambda: access_element(my_array, size // 2), number=100000)
    execution_times.append(execution_time)

# Plotting
plt.plot(array_sizes, execution_times, marker='o')
plt.title('Constant Time Complexity')
plt.xlabel('Array Size')
plt.ylabel('Execution Time')
plt.show()
