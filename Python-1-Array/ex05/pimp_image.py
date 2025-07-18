import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """
    Inverts the colors of the input RGB image array.

    Args:
        array (np.ndarray): An RGB image represented as a NumPy array.

    Returns:
        np.ndarray: The color-inverted image.
    """
    inverted = 255 - array
    return inverted


def ft_red(array) -> np.ndarray:
    """
    Extracts the red channel from the input RGB image array, 
    setting the green and blue channels to zero.

    Args:
        array (np.ndarray): An RGB image represented as a NumPy array.

    Returns:
        np.ndarray: Image with only the red channel preserved.
    """
    red_only = array.copy()
    red_only[:, :, 1] *= 0
    red_only[:, :, 2] *= 0
    return red_only


def ft_green(array) -> np.ndarray:
    """
    Extracts the green channel from the input RGB image array, 
    setting the red and blue channels to zero.

    Args:
        array (np.ndarray): An RGB image represented as a NumPy array.

    Returns:
        np.ndarray: Image with only the green channel preserved.
    """
    green_only = array.copy()
    green_only[:, :, 0] = 0
    green_only[:, :, 2] = 0
    return green_only


def ft_blue(array) -> np.ndarray:
    """
    Extracts the blue channel from the input RGB image array, 
    setting the red and green channels to zero.

    Args:
        array (np.ndarray): An RGB image represented as a NumPy array.

    Returns:
        np.ndarray: Image with only the blue channel preserved.
    """
    blue_only = array.copy()
    blue_only[:, :, 0] = 0
    blue_only[:, :, 1] = 0
    return blue_only


def ft_grey(array) -> np.ndarray:
    """
    Converts the input RGB image array to grayscale using average weighting.

    Args:
        array (np.ndarray): An RGB image represented as a NumPy array.

    Returns:
        np.ndarray: Grayscale version of the image, replicated across RGB channels.
    """
    grey = array.copy()
    grey_value = (grey[:, :, 0]/3)+(grey[:, :, 1]/3)+(grey[:, :, 2]/3)
    grey_img = np.stack((grey_value,) * 3, axis=-1).astype(np.uint8)
    return grey_img


def show_images(array: np.array):
    """
    Displays the original image along with its inverted, red, green, blue, 
    and grayscale versions in a 3x2 grid using Matplotlib.

    Args:
        array (np.ndarray): An RGB image represented as a NumPy array.

    Raises:
        Exception: Prints an error message if any unexpected error occurs.
    """
    try:
        invert_img = ft_invert(array)
        red_img = ft_red(array)
        green_img = ft_green(array)
        blue_img = ft_blue(array)
        grey_img = ft_grey(array)

        fig, axes = plt.subplots(3, 2, figsize=(9, 8))

        axes[0, 0].imshow(array)
        axes[0, 0].set_title("Figure VIII.1: Original", y=-0.11, x=0.5)
        axes[0, 0].axis('off')

        axes[0, 1].imshow(invert_img)
        axes[0, 1].set_title("Figure VIII.2: Invert", y=-0.11, x=0.5)
        axes[0, 1].axis('off')

        axes[1, 0].imshow(red_img)
        axes[1, 0].set_title("Figure VIII.3: Red", y=-0.11, x=0.5)
        axes[1, 0].axis('off')

        axes[1, 1].imshow(green_img)
        axes[1, 1].set_title("Figure VIII.4: Green", y=-0.11, x=0.5)
        axes[1, 1].axis('off')

        axes[2, 0].imshow(blue_img)
        axes[2, 0].set_title("Figure VIII.5: Blue", y=-0.11, x=0.5)
        axes[2, 0].axis('off')

        axes[2, 1].imshow(grey_img, cmap='gray')
        axes[2, 1].set_title("Figure VIII.6: Grey", y=-0.11, x=0.5)
        axes[2, 1].axis('off')

        plt.tight_layout(h_pad=0.3, w_pad=0.3)
        plt.show()
    except Exception as e:
        print(f"Unexpected error: {e}")
