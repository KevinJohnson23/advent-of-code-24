from timeit import timeit

def test_time(func, n=1000):
    execution_time = timeit(func, number=n)
    average_time = execution_time / n
    print(f"Average execution time: {average_time*1000:.3f} ms")