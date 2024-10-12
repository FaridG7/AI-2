import timeit

from typing import Callable

def benchmark(func: Callable[[int], str], goal: int) -> str:
    start_time = timeit.default_timer()
    func(goal)
    time_taken = timeit.default_timer() - start_time
    return f"{func.__name__}({goal}) took {time_taken:.6f} seconds"
