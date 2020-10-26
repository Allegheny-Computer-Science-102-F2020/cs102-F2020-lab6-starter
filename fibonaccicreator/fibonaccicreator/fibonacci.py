"""Compute values in the Fibonacci sequence using different approaches."""

from typing import Tuple

from memory_profiler import profile


@profile
def fibonacci_tuple(number: int) -> Tuple[int]:
    """Compute up to and including the number-th Fibonacci number using a tuple."""
    # TODO: Add all of the required source code for this tuple-based function
    # create an empty tuple that will ultimately contain the results
    result = ()
    return result


@profile
def fibonacci_list(number: int) -> Tuple[int]:
    """Compute up to and including the number-th Fibonacci number using a list."""
    # TODO: Add all of the required source code for this list-based function
    # create an empty list that will ultimately contain the results
    result = []
    return result
