# Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.

import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution Time:", end - start)
    return wrapper
@timer
def task():
    time.sleep(2)
    print("Task Completed")
task()

