import os
import time

def write_to_memory(num_elements, element_size):
    array = bytearray(num_elements * element_size)
    for i in range(0, num_elements, element_size):
        element = os.urandom(element_size)
        array[i:i + element_size] = element
    return array

def read_from_memory(array, num_elements, element_size):
    for i in range(0, num_elements, element_size):
        element = array[i:i + element_size]

if __name__ == "__main__":
    num_elements = 5 * (10 ** 9)
    element_size = 4

    start = time.perf_counter()
    array = write_to_memory(num_elements, element_size)
    end = time.perf_counter()

    write_time = end - start
    print(f'Memory write benchmark execution time: {write_time}')

    start = time.perf_counter()
    read_from_memory(array, num_elements, element_size)
    end = time.perf_counter()

    read_time = end - start
    print(f'Memory read benchmark execution time: {read_time}')
