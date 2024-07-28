import time
from functools import wraps

def timeit(unit='seconds'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            
            if unit == 'seconds':
                print(f"Execution time of {func.__name__}: {elapsed_time:.6f} seconds")
            elif unit == 'microseconds':
                print(f"Execution time of {func.__name__}: {elapsed_time * 1_000_000:.2f} microseconds")
            else:
                raise ValueError("Invalid unit. Please use 'seconds' or 'microseconds'.")
            
            return result
        return wrapper
    return decorator

@timeit(unit='seconds')
def example_function():
    time.sleep(1)

@timeit(unit='microseconds')
def another_example_function():
    for _ in range(1000):
        pass

example_function()
another_example_function()
