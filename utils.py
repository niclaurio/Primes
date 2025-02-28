from typing import Iterable, Callable
import time
import os
from matplotlib import pyplot as plt
from collections import defaultdict
from primesAlgorithms.v1 import get_primes_lower_n as v1_func
from primesAlgorithms.v2 import get_primes_lower_n as v2_func
from primesAlgorithms.v3 import get_primes_lower_n as v3_func
from primesAlgorithms.v4 import get_primes_lower_n as v4_func
from primesAlgorithms.v5 import get_primes_lower_n as v5_func
from primesAlgorithms.v6 import get_primes_lower_n as v6_func
from concurrent.futures import ProcessPoolExecutor, as_completed, ThreadPoolExecutor


def get_function_execution_time(n: int, func: Callable) -> float:
    execution_start_time = time.perf_counter()
    func(n)
    return time.perf_counter() - execution_start_time


def plot_times(title: str, times_1: list[float], times_2, x_values: Iterable) -> None:
    plt.plot(list(x_values), times_1, label="oldest_version")
    plt.plot(list(x_values), times_2, label="newest_version")
    plt.title(title)
    plt.xlabel("range")
    plt.ylabel("times")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join("plots", title + ".png"))
    plt.clf()


def is_test():
    return "PYTEST_CURRENT_TEST" in os.environ


def get_execution_times(
    max_workers: int, start: int, stop: int, increment: int
) -> dict[str, list[float]]:
    functions = [v1_func, v2_func, v3_func, v4_func, v5_func, v6_func]

    functions_execution_times = defaultdict(list)
    pool_executor = (
        ThreadPoolExecutor(max_workers=max_workers)
        if is_test()
        else ProcessPoolExecutor(max_workers=max_workers)
    )

    with pool_executor as executor:
        futures = {
            executor.submit(get_function_execution_time, number, func): func
            for func in functions
            for number in range(stop-increment, start-increment, -increment)
        }

        for future in as_completed(futures):
            execution_time = future.result()
            function = futures[future]
            version = function.__module__.split(".")[-1]

            functions_execution_times[version].append(execution_time)

    return functions_execution_times
