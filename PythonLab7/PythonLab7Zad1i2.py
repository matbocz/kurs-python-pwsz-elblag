from cv2 import cv2
import numpy as np
import time


def mouse_callback(event, x, y, flags, param):
    mouse_x = int(x / CELL_SIZE)
    mouse_y = int(y / CELL_SIZE)

    if event == cv2.EVENT_LBUTTONDOWN:
        CELL_FIELD[mouse_x][mouse_y] = LIVING_CELL
    if event == cv2.EVENT_RBUTTONDOWN:
        CELL_FIELD[mouse_x][mouse_y] = DEAD_CELL


def prepare_pop(cell_field):
    next_gen = [DEAD_CELL] * CELLS_HORIZONTALLY
    for i in range(CELLS_HORIZONTALLY):
        next_gen[i] = [DEAD_CELL] * CELLS_VERTICALLY

    for y in range(CELLS_VERTICALLY):
        for x in range(CELLS_HORIZONTALLY):
            pop = 0

            try:
                if cell_field[x - 1][y - 1] == LIVING_CELL:
                    pop += 1
            except IndexError:
                pass
            try:
                if cell_field[x][y - 1] == LIVING_CELL:
                    pop += 1
            except IndexError:
                pass
            try:
                if cell_field[x + 1][y - 1] == LIVING_CELL:
                    pop += 1
            except IndexError:
                pass

            try:
                if cell_field[x - 1][y] == LIVING_CELL:
                    pop += 1
            except IndexError:
                pass
            try:
                if cell_field[x + 1][y] == LIVING_CELL:
                    pop += 1
            except IndexError:
                pass

            try:
                if cell_field[x - 1][y + 1] == LIVING_CELL:
                    pop += 1
            except IndexError:
                pass
            try:
                if cell_field[x][y + 1] == LIVING_CELL:
                    pop += 1
            except IndexError:
                pass
            try:
                if cell_field[x + 1][y + 1] == LIVING_CELL:
                    pop += 1
            except IndexError:
                pass

            if cell_field[x][y] == LIVING_CELL and (pop < 2 or pop > 3):
                next_gen[x][y] = DEAD_CELL
            elif cell_field[x][y] == LIVING_CELL and (pop == 3 or pop == 2):
                next_gen[x][y] = LIVING_CELL
            elif cell_field[x][y] == DEAD_CELL and pop == 3:
                next_gen[x][y] = LIVING_CELL

    return next_gen


def draw_pop():
    for y in range(CELLS_VERTICALLY):
        for x in range(CELLS_HORIZONTALLY):
            if CELL_FIELD[x][y] == LIVING_CELL:
                cv2.rectangle(WINDOW, (x*CELL_SIZE, y*CELL_SIZE),
                              (x*CELL_SIZE+CELL_SIZE, y*CELL_SIZE+CELL_SIZE), CELL_FILL_COLOR, -1)
                cv2.rectangle(WINDOW, (x*CELL_SIZE, y*CELL_SIZE),
                              (x*CELL_SIZE+CELL_SIZE, y*CELL_SIZE+CELL_SIZE), CELL_BORDER_COLOR, 1)


WINDOW_NAME = "OpenCV Game of Life"
WINDOW_FILL_COLOR = np.array([0, 0, 0], np.uint8)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

VIDEO_NAME = WINDOW_NAME + ".avi"
VIDEO_FRAMES_PER_SECOND = 60
video = cv2.VideoWriter(VIDEO_NAME, cv2.VideoWriter_fourcc(
    *"MJPG"), VIDEO_FRAMES_PER_SECOND, (WINDOW_WIDTH, WINDOW_HEIGHT))

LIVING_CELL = 1
DEAD_CELL = 0

CELL_SIZE = 10
CELLS_HORIZONTALLY = int(WINDOW_WIDTH / CELL_SIZE)
CELLS_VERTICALLY = int(WINDOW_HEIGHT / CELL_SIZE)
CELL_FILL_COLOR = (255, 255, 255)
CELL_BORDER_COLOR = (255, 0, 0)

CELL_FIELD = [DEAD_CELL] * CELLS_HORIZONTALLY
for i in range(CELLS_HORIZONTALLY):
    CELL_FIELD[i] = [DEAD_CELL] * CELLS_VERTICALLY

cv2.namedWindow(WINDOW_NAME)
cv2.setMouseCallback(WINDOW_NAME, mouse_callback)

run = False
while True:
    k = cv2.waitKey(1) & 0xFF

    if k == 13:  # Enter KEY
        run = True
    if k == 32:  # Space KEY
        run = False
    if k == 115:  # s KEY
        CELL_FIELD = prepare_pop(CELL_FIELD)
    if k == 27:  # Escape KEY
        video.release()
        break

    if run == True:
        CELL_FIELD = prepare_pop(CELL_FIELD)

    WINDOW = np.full((WINDOW_HEIGHT, WINDOW_WIDTH, 3), WINDOW_FILL_COLOR)
    draw_pop()

    video.write(WINDOW)
    cv2.imshow(WINDOW_NAME, WINDOW)
