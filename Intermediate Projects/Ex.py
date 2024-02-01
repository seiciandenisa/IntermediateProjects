from timeit import timeit

s = {3, 4, 1, 1}

print(sum(s))

print([1, 2].extend([3, 4]))

a = [1, 2]
b = [x ** 2 for x in a if x < 2]

print(b)

code = """
from time import sleep
def method():
    sleep(1)
    
method()
"""

print(timeit(code, number=1))
