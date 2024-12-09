from timeit import timeit

def test_time(func):
    execution_time = timeit(func, number=1)
    print(f"Execution time: {execution_time*1000:.3f} ms")