cache = {}

def fibonacci(n):
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = res
    return res

for i in range(1000):
    resultado = fibonacci(i)
    print(i, resultado)
