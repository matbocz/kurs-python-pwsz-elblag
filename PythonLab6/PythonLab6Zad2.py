import pyautogui
from PIL import ImageGrab
from PIL import ImageOps
import numpy as np
import time

# Program napisany z pomocą tutoriala:
# youtube.com/watch?v=xYymkeNh2lE

# Program testowany na stronie:
# trex-game.skipser.com

# Poczekaj przed uruchomieniem 5 sekund
time.sleep(5)

# Znajdź przycisk restart i kliknij go
restart_button = pyautogui.locateOnScreen("restart_button.png")
pyautogui.moveTo(restart_button.left, restart_button.top)
pyautogui.click()

# Znajdź głowę dinozaura
dino_head_img = pyautogui.locateOnScreen("dino_head.png")
dino_head = (dino_head_img.left, dino_head_img.top)

# Ustaw parametry przesunięcia screena
leftX = 40
topY = 0
rightX = 130
bottomY = 30

# Zrób początkowego screena terenu przed dinozaurem
start_dino_head_box = (dino_head[0] + leftX, dino_head[1] +
                       topY, dino_head[0] + rightX, dino_head[1] + bottomY)
start_image = ImageGrab.grab(start_dino_head_box)

# Zmień kolory początkowego screena terenu na czarno białe i pobierz wartości kolorów
start_grayImage = ImageOps.grayscale(start_image)
start_colors = np.array(start_grayImage.getcolors())

while True:
    # Zrób nowego screena terenu przed dinozaurem
    dino_head_box = (dino_head[0] + leftX, dino_head[1] +
                     topY, dino_head[0] + rightX, dino_head[1] + bottomY)
    image = ImageGrab.grab(dino_head_box)

    # Zmień kolory nowego screena terenu na czarno białe i pobierz wartości kolorów
    grayImage = ImageOps.grayscale(image)
    colors = np.array(grayImage.getcolors())

    # Porónaj sume watrości kolorów screena początkowego i nowego
    if (start_colors.sum() != colors.sum()):
        pyautogui.keyDown("space")
