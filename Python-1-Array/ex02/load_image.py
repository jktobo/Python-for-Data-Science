import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the given path, prints its pixel data.

    Args:
        path (str): Path to the image file.

    Returns:
        img_array: Image as an array in RGB format.
    """
    try:
        img = Image.open(path)
        img = img.convert('RGB')
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        return img_array
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Error loading image: {e}")
