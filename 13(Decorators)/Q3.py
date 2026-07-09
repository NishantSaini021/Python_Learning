# Problem 3: Cache Return Values
# Problem: Implement a decorator that caches the return values of a function,
# so that when it's called with the same arguments,
# the cached value is returned instead of re-executing the function.

def cache_decorator(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        else:
            print("Calculating...")
            result = func(*args, **kwargs)
            cache[args] = result
        return result
    return wrapper

@cache_decorator
def square(a):
    return a*a
print(square(4))
print(square(4))
print(square(4))
print(square(4))
