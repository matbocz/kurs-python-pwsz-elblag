import cv2

def change_height(v, img):
    img_r = cv2.resize(img, (0, 0), fx=1, fy=v / 100)
    cv2.imshow('obraz', img_r)

def change_width(v, img):
    img_r = cv2.resize(img, (0, 0), fx=v / 100, fy=1)
    cv2.imshow('obraz', img_r)

def change_blur(v, img):
    img_b = cv2.blur(img, (v, v))
    cv2.imshow('obraz', img_b)

img = cv2.imread("obraz.jpg", cv2.IMREAD_COLOR)
img_r = cv2.resize(img, (993, 776))

cv2.imshow('obraz', img_r)

cv2.createTrackbar('Wysokosc:', 'obraz', 100, 200, lambda v: change_height(v, img_r))
cv2.createTrackbar('Szerokosc:', 'obraz', 100, 200, lambda v: change_width(v, img_r))
cv2.createTrackbar('Blur:', 'obraz', 1, 20, lambda v: change_blur(v, img_r))

cv2.waitKey(0)