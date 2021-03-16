import numpy as np

def save_to_file(n, s, k):
    x = np.linspace(start=s, stop=k, num=n)
    y = np.cos(x)

    np.savetxt('zad1.csv', y)

    return x, y

x, y = save_to_file(10, 0, np.pi)

print("X array:\n{0}\n".format(x))
print("Y array:\n{0}\n".format(y))