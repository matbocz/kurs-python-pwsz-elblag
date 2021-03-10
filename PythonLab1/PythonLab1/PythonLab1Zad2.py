import timeit

def is_lower(txt):
    for x in txt:
        if(ord(x) >= 65 and ord(x) <= 90):
            return False

    return True

txt = "Lorem ipsum"
test = timeit.Timer("is_lower(txt)", "from __main__ import is_lower, txt")

print("Time(10):", test.timeit(10))
print("Time(1000):", test.timeit(1000))
print("Time(100 000):", test.timeit(100000))
print("Time(10 000 000):", test.timeit(10000000))