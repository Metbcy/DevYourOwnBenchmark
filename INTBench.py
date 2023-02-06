import time
def benchmark():
    start = time.perf_counter()
    result = 0
    for i in range(10**10):
        result += 1
    for i in range(5 * 10**9):
        result *= 2
    for i in range(2 * 10**9):
        result /= 2
    end = time.perf_counter()
    print("Time elapsed: ", end - start, "seconds")
benchmark()
