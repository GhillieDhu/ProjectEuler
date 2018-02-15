import timeit

def timed_execution(repetitions):
    print(timeit.timeit("fizzbuzz.sum_of_multiples([3, 5], 1000)", "import fizzbuzz", number=repetitions) / repetitions)

for i in range(6):
    timed_execution(10**i)