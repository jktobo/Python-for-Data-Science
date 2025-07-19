import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the given path, prints the shape,
    and returns the first and last row concatenated horizontally.

    Args:
        path (str): Path to the image file.

    Returns:
        np.ndarray: Concatenated first and last row of the image.
    """
    try:
        img = Image.open(path)
        if img.format not in ['JPEG', 'JPG']:
            raise ValueError(f"Don't supported image format '{img.format}'. Only JPEG or JPG format.")
        img = img.convert('RGB')
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        return np.concatenate((img_array[0:1], img_array[-1:]), axis=1)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Error loading image: {e}")
