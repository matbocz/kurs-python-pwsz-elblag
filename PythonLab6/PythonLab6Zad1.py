import pyautogui
import numpy as np
import time

# Poczekaj przed uruchomieniem 5 sekund
time.sleep(5)

# Ustaw parametry początkowe
fstart = 0
fstop = 10
fstep = 0.05
ffreq = 10

# Narysuj sinus
for x in np.arange(fstart, fstop, fstep):
    y = np.sin(2 * np.pi * ffreq * (x / fstop))

    pyautogui.drag(x, y * 20)
    print("x = %f y = %f" % (x, y))

    time.sleep(0.01)
