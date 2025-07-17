# zoom.py
from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def zoom_image(image: np.ndarray, size: int = 400) -> np.ndarray:
    """
    Zooms into the center of the image to a square of given size.

    Args:
        image (np.ndarray): Original image as an array.
        size (int): Size of the zoomed square (default 400).

    Returns:
        np.ndarray: The zoomed and grayscaled image.
    """
    try:
        height, width, _ = image.shape
        center_x, center_y = width // 2, height // 2
        half_size = size // 2
        cropped = image[
            center_y - half_size:center_y + half_size,
            center_x - half_size:center_x + half_size
        ]

        # Convert to grayscale
        gray = np.dot(cropped[...,:3], [0.2989, 0.5870, 0.1140])
        gray = gray.astype(np.uint8)
        print(f"New shape after slicing: {gray.shape}")
        print(gray)

        return gray
    except Exception as e:
        print(f"Error during zoom: {e}")
        return None


def main():
    img = ft_load("animal.jpeg")
    if img is None:
        return
    print(img.shape)
    print(img)

    gray_zoomed = zoom_image(img)

    if gray_zoomed is not None:
        plt.imshow(gray_zoomed, cmap='gray')
        plt.title("Zoomed Grayscale Image")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()


if __name__ == "__main__":
    main()



# import numpy as np
# import matplotlib.pyplot as plt
# from load_image import ft_load

# def main():
#     try:
#         img = ft_load("animal.jpeg")
#         if img is None:
#             return

#         print(f"Original shape: {img.shape}")
#         print(img)

#         # Например, возьмём квадрат 400x400 в центре
#         center_x = img.shape[1] // 2
#         center_y = img.shape[0] // 2

#         half_size = 200  # половина от 400
#         x_start = center_x - half_size
#         x_end = center_x + half_size
#         y_start = center_y - half_size
#         y_end = center_y + half_size

#         zoomed = img[y_start:y_end, x_start:x_end, :]

#         print(f"New shape after slicing: {zoomed.shape}")
#         print(zoomed)

#         grayscale = np.dot(zoomed[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
#         print(f"New shape after converting to grayscale: {grayscale.shape}")
#         print(grayscale)

#         plt.imshow(grayscale)
#         plt.title("Zoomed Image")
#         plt.xlabel("X axis")
#         plt.ylabel("Y axis")
#         plt.show()

#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     main()
