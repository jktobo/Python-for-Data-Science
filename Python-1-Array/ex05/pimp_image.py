# pimp_image.py
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """
    Inverts the colors of the input image array.
    """
    inverted = 255 - array
    # plt.imshow(inverted)
    # plt.title("Inverted")
    # plt.show()
    return inverted


def ft_red(array) -> np.ndarray:
    """
    Keeps only the red channel of the image.
    """
    red_only = array.copy()
    red_only[:, :, 1] *= 0  # Zero green channel
    red_only[:, :, 2] *= 0  # Zero blue channel
    # plt.imshow(red_only)
    # plt.title("Red Filter")
    # plt.show()
    return red_only


def ft_green(array) -> np.ndarray:
    """
    Keeps only the green channel of the image.
    """
    green_only = array.copy()
    green_only[:, :, 0] = green_only[:, :, 0] - green_only[:, :, 0]  # Zero red
    green_only[:, :, 2] = green_only[:, :, 2] - green_only[:, :, 2]  # Zero blue
    # plt.imshow(green_only)
    # plt.title("Green Filter")
    # plt.show()
    return green_only


def ft_blue(array) -> np.ndarray:
    """
    Keeps only the blue channel of the image.
    """
    blue_only = array.copy()
    blue_only[:, :, 0] = 0  # Zero red
    blue_only[:, :, 1] = 0  # Zero green
    # plt.imshow(blue_only)
    # plt.title("Blue Filter")
    # plt.show()
    return blue_only


def ft_grey(array) -> np.ndarray:
    """
    Converts the image to grayscale.
    """
    grey = array.copy()
    grey_value = (grey[:, :, 0] / 3) + (grey[:, :, 1] / 3) + (grey[:, :, 2] / 3)
    grey_img = np.stack((grey_value,) * 3, axis=-1).astype(np.uint8)
    # plt.imshow(grey_img)
    # plt.title("Grey Filter")
    # plt.show()
    return grey_img
