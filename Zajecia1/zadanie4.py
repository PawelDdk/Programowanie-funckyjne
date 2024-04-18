import time


def timeit(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Funkcja {func.__name__} wykonana w {execution_time:.6f} sekund")
        return result
    return wrapper

@timeit
def example_function():
    time.sleep(2)
    print("Example function executed")

example_function()