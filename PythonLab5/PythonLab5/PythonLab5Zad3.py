import cv2
import os
import numpy as np

# Metoda znaleziona na stronie:
# https://stackoverflow.com/questions/47094930/creating-a-mosaic-of-thumbnails-with-opencv-3-and-numpy
def show_save_images_mosaic(images, width):
    rows = []

    for i in range(0, len(images), width):
        rows.append(np.concatenate(images[i: i + width], axis=1))

    if len(rows) > 1:
        last_row = rows[-1]

        height = images[0].shape[0]
        last_row_width = last_row.shape[1]
        expected_width = rows[0].shape[1]

        if last_row_width < expected_width:
            filler = np.zeros((height, expected_width - last_row_width, 3), dtype=np.uint8)
            rows[-1] = np.concatenate((last_row, filler), axis=1)
        else:
            filler = None

    mosaic = np.concatenate(rows, axis=0)

    cv2.imshow('Mosaic', mosaic)
    cv2.imwrite('Mosaic.jpg', mosaic)

    cv2.waitKey(0)

images = []

for root, dirs, files in os.walk('./miniaturki'):
    for file_name in files:
        img = cv2.imread('./miniaturki/' + file_name, cv2.IMREAD_COLOR)

        images.append(img)

show_save_images_mosaic(images, 3)