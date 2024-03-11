import timeit
import matplotlib.pyplot as plt

def linear_operation(array):
    result = 0

    for element in array:
        result += element

    return result

# Measuring execution times for different array sizes
array_sizes = [10, 20, 30, 40, 50]
execution_times = []

for size in array_sizes:
    my_array = list(range(size))
    execution_time = timeit.timeit(lambda: linear_operation(my_array), number=10)
    execution_times.append(execution_time)

# Plotting
plt.plot(array_sizes, execution_times, marker='o')
plt.title('Linear Time Complexity')
plt.xlabel('Array Size')
plt.ylabel('Execution Time')
plt.show()
