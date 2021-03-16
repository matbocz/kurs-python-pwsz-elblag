import numpy as np

def load_from_file(m, s, k):
    x = np.loadtxt('zad1.csv')
    y = np.cos(x)

    xvals = np.linspace(start=s, stop=k, num=m)
    yinterp = np.interp(xvals, x, y)

    return xvals, yinterp

xvals, yinterp = load_from_file(50, 0, np.pi)

print("XVALS array:\n{0}\n".format(xvals))
print("YINTERP array:\n{0}\n".format(yinterp))