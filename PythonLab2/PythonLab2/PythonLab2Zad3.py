import numpy as np
import matplotlib.pyplot as plt

def save_to_file(n, s, k):
    x = np.linspace(start=s, stop=k, num=n)
    y = np.cos(x)

    np.savetxt('zad1.csv', y)

    return x, y

def load_from_file(m, s, k):
    x = np.loadtxt('zad1.csv')
    y = np.cos(x)

    xvals = np.linspace(start=s, stop=k, num=m)
    yinterp = np.interp(xvals, x, y)

    return xvals, yinterp

x, y = save_to_file(10, 0, np.pi)
xvals, yinterp = load_from_file(50, 0, np.pi)

print("X array:\n{0}\n".format(x))
print("Y array:\n{0}\n".format(y))

print("XVALS array:\n{0}\n".format(xvals))
print("YINTERP array:\n{0}\n".format(yinterp))

plt.plot(x, y, 'r-', linewidth=1)
plt.plot(xvals, yinterp, 'g--', linewidth=2)
plt.show()
