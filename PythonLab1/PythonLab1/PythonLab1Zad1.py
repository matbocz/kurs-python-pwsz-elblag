import timeit

txt = "Lorem ipsum"
test = timeit.Timer("txt.islower()", "from __main__ import txt")

print("Time(10):", test.timeit(10))
print("Time(1000):", test.timeit(1000))
print("Time(100 000):", test.timeit(100000))
print("Time(10 000 000):", test.timeit(10000000))