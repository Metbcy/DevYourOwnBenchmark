import time
def benchmark():
    start = time.perf_counter()
    with open("benchmark.txt", "wb") as file:
        for i in range(10**9 // 10000):
            file.write(b'0' * 10000)

    end = time.perf_counter()
    print("Time elapsed: ", end - start, "seconds")
