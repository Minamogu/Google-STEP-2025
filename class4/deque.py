import time
from collections import deque

num_list = [i for i in range(1000000)]
num_deque = deque(i for i in range(10000))

def queue(num):
    """dequeを用いたキューの操作"""
    for i in range(100):
        num.append(i)
        num.popleft()
    return num

def without_deque(num):
    """listによるキューの操作"""
    for i in range(100):
        num.append(i)
        num.pop(0)
    return num

if __name__ == '__main__':
    start = time.perf_counter()
    num = without_deque(num_list)
    print(f'list: {time.perf_counter() - start}s')
    print(num[:50])

    start = time.perf_counter()
    num = queue(num_deque)
    print(f'deque: {time.perf_counter() - start}s')
    print(list(num[i] for i in range(50)))

#queueはappendとpopleft, stackはappendとpop