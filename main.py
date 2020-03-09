import random
import time

if __name__ == '__main__':
    start_time = time.time()
    a = []
    for i in range(50000000):
        a.append(random.random())
    print(time.time() - start_time)
