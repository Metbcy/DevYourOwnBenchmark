#INTEGER BENCHMARK
import time

def addition():
    number1 = 500.5234
    number2 = 32.12893
    for i in range(10):
        for o in range(10):
            result = number1 + number2
            
def multiplication():           
    number1 = 60.3549827
    number2 = 56.4178
    for i in range(5):
        for o in range(10**9):
            result = number1 * number2
def division():
    number1 = 100.4462346
    number2 = 20.241254
    for i in range(2):
        for o in range(10**9):
            result = number1 / number2

    
if __name__ == '__main__':
    start = time.perf_counter()
    addition()
    multiplication()
    division()
    end = time.perf_counter()
    print("Time elapsed: ", end - start, "seconds")
