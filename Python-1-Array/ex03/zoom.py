from load_image import ft_load
import numpy as np
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
        new_size = image[
            center_y - half_size:center_y + half_size,
            center_x - half_size:center_x + half_size
        ]

        gray = np.dot(new_size[..., :3], [0.2989, 0.5870, 0.1140])
        gray = gray.astype(np.uint8)
        gray = gray[:, :, np.newaxis]
        print(f"New shape after slicing: {gray.shape} or {gray.squeeze().shape}")
        np.set_printoptions(threshold=2)
        print(np.concatenate((gray[0:1], gray[-1:]), axis=1))

        return gray
    except Exception as e:
        print(f"Error during zoom: {e}")
        return None


def main():
    """
    Main function that loads an image, prints its first and last rows concatenated,
    applies the zoom and grayscale transformation, and displays the result.

    The function loads the image 'animal.jpeg', shows its edge rows,
    then zooms into the center, converts the zoomed area to grayscale,
    and visualizes the result using matplotlib.
    """
    img = ft_load("animal.jpeg")
    if img is None:
        return
    print(np.concatenate((img[0:1], img[-1:]), axis=1))

    img_zoom = zoom_image(img)

    if img_zoom is not None:
        plt.imshow(img_zoom, cmap='gray')
        plt.title("Zoomed Grayscale Image")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()


if __name__ == "__main__":
    main()
