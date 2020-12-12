# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import numpy
import math

def load_input_image(image_path):
    test_img = cv2.imread(image_path)
    h, w, _ = test_img.shape

    return test_img, h, w

# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/