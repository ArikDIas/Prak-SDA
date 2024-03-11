import timeit
import matplotlib.pyplot as plt

def quadratic_operation(array):
    n = len(array)
    result = 0

    for i in range(n):
        for j in range(n):
            result += array[i] * array[j]

    return result

# Measuring execution times for different array sizes
array_sizes = [10, 20, 30, 40, 50]
execution_times = []

for size in array_sizes:
    my_array = list(range(size))
    execution_time = timeit.timeit(lambda: quadratic_operation(my_array), number=10)
    execution_times.append(execution_time)

# Plotting
plt.plot(array_sizes, execution_times, marker='o')
plt.title('Quadratic Time Complexity')
plt.xlabel('Array Size')
plt.ylabel('Execution Time')
plt.show()
