import time
import os

def write():
    with open("benchmark.txt", "wb") as file:
        for i in range(10**9 // 100):
            file.write(b'0' * 100)
 
    
def read():
    result = 0
    with open("benchmark.txt", "rb") as file:
        chunk = file.read(100)
        while chunk:
            result += len(chunk)
            chunk = file.read(100)
    return result


if __name__ == '__main__':
    start = time.perf_counter()
    write()
    read()
    result=read()
    end = time.perf_counter()
    print("Time elapsed: ", end - start, "seconds")
     
