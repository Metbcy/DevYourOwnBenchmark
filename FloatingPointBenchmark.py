import time
def floatingaddition():
    number1 = 67
    number2 = 30
    for i in range(10):
        for o in range(10):
            result = number1 + number2
            
def floatingmultiplication():           
    number1 = 89
    number2 = 70
    for i in range(5):
        for o in range(10):
            for p in range(9):
                result = number1 * number2
def floatingdivision():
    number1 = 100
    number2 = 20
    for i in range(2):
        for o in range(10):
            for p in range(9):
                result = number1 / number2

    
if __name__ == '__main__':
    start = time.perf_counter()
    floatingaddition()
    floatingmultiplication()
    floatingdivision()
    end = time.perf_counter()
    print("Time elapsed: ", end - start, "seconds")
 
