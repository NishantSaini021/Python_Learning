# Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Function:- {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a,b):
    return a + b
add(3,5)