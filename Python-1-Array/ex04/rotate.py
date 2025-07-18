from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def gray_img(image: np.ndarray) -> np.ndarray:
    """
    Converts an RGB image to grayscale using weighted averages.

    Args:
        image (np.ndarray): An RGB image represented as a NumPy array 
                            with shape (height, width, 3).

    Returns:
        np.ndarray: A 2D grayscale image as a NumPy array with shape (height, width).
    """
    gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    return gray
    # return gray.astype(np.uint8)


def transpose(image: np.ndarray) -> np.ndarray:
    """
    Manually transposes a 2D grayscale image.

    The transpose is performed by swapping the rows and columns of the input array.

    Args:
        image (np.ndarray): A 2D grayscale image as a NumPy array.

    Returns:
        np.ndarray: The transposed grayscale image.

    Raises:
        ValueError: If the input image is not a 2D array.
    """
    if len(image.shape) != 2:
        raise ValueError("Only 2D gray images can be transposed.")

    rows, cols = image.shape
    transposed = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(image[j][i])
        transposed.append(new_row)
    return np.array(transposed)


def main():
    """
    Main function to load an image, crop its center region, convert it to grayscale,
    manually transpose it, and display the transposed image using Matplotlib.
    It also prints intermediate array shapes and example pixel data.
    """
    img = ft_load("animal.jpeg")
    if img is None:
        return

    height, width, _ = img.shape
    size = 400
    center_x, center_y = width // 2, height // 2
    half_size = size // 2

    new_size = img[
        center_y - half_size:center_y + half_size,
        center_x - half_size:center_x + half_size
    ]

    gray = gray_img(new_size)
    gray = gray.astype(np.uint8)
    gray1 = gray[:, :, np.newaxis]
    print(f"The shape of image is: {gray1.shape} or {gray.squeeze().shape}")
    np.set_printoptions(threshold=2)
    print(np.concatenate((gray1[0:1], gray1[-1:]), axis=1))

    transposed = transpose(gray)
    print(f"New shape after Transpose: {transposed.shape}")
    np.set_printoptions(threshold=2)
    print(transposed[0:1])
    print('  ...')
    print(transposed[-1:])

    plt.subplot(1, 1, 1)
    plt.title("Transposed")
    plt.imshow(transposed, cmap='gray')
    plt.xticks(np.arange(0, transposed.shape[1], 50))
    plt.yticks(np.arange(0, transposed.shape[0], 50))
    plt.show()

if __name__ == "__main__":
    main()
