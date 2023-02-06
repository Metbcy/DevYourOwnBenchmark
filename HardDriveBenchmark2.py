import time
def benchmark():
    start = time.perf_counter()
    with open("benchmark.txt", "wb") as file:
        for i in range(10**9 // 10000):
            file.write(b'0' * 10000)
    result = 0
    with open("benchmark.txt", "rb") as file:
        chunk = file.read(10000)
        while chunk:
            result += len(chunk)
            chunk = file.read(10000)
            
    end = time.perf_counter()
    print("Time elapsed: ", end - start, "seconds")
