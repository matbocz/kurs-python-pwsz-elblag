import cv2
import os

for root, dirs, files in os.walk('./obrazy'):
    for file_name in files:
        print("Znaleziono: " + file_name)

        img = cv2.imread('./obrazy/' + file_name, cv2.IMREAD_COLOR)
        img_r = cv2.resize(img, (240, 320))

        new_file_name = file_name[:-4] + "_mini.jpg"
        cv2.imwrite('./miniaturki/' + new_file_name, img_r)

        print("Zapisano jako: " + new_file_name)