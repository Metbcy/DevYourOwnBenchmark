import time
def benchmark():
    start = time.perf_counter()
    with open("benchmark.txt", "wb") as file:
        for i in range(10**9 // 100):
            file.write(b'0' * 100)
    result = 0
    with open("benchmark.txt", "rb") as file:
        chunk = file.read(100)
        while chunk:
            result += len(chunk)
            chunk = file.read(100)
            
    end = time.perf_counter()
    print("Time elapsed: ", end - start, "seconds")
    
benchmark()
