import array
import time
def benchmark():
    start = time.perf_counter()
    data = array.array("I", [0] * (5 * 10**9))
    for i in range(5 * 10**9):
        data[i] = i
    result = 0
    for i in data:
        result += i
    end = time.perf_counter()
    print("Time elapsed: ", end - start, "seconds")
benchmark()