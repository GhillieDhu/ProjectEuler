import timeit
from typing import Sequence


def timed_execution(approaches: Sequence[str], repetitions: int):
    """"""
    for approach in approaches:
        print(approach + ": " +
              str(timeit.timeit("fizzbuzz."+approach+"([3, 5], 1000)",
                  "import fizzbuzz", number=repetitions) / repetitions))


for i in range(6):
    timed_execution(["sum_of_multiples"], 10**i)
