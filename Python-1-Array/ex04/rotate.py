# rotate.py
from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def grayscale(image: np.ndarray) -> np.ndarray:
    """
    Converts an RGB image to grayscale.
    """
    gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    return gray.astype(np.uint8)


def transpose(image: np.ndarray) -> np.ndarray:
    """
    Manually transposes a 2D image array (grayscale).
    """
    if len(image.shape) != 2:
        raise ValueError("Only 2D grayscale images can be transposed.")

    rows, cols = image.shape
    transposed = []
    for i in range(cols):  # для каждого столбца в оригинальной матрице
        new_row = []
        for j in range(rows):  # проходим по каждой строке
            new_row.append(image[j][i])  # берем элемент из строки j, столбца i
        transposed.append(new_row)  # добавляем новую строку в транспонированную матрицу
    return np.array(transposed)


def main():
    img = ft_load("animal.jpeg")
    if img is None:
        return

    height, width, _ = img.shape
    size = 400
    center_x, center_y = width // 2, height // 2
    half_size = size // 2

    cropped = img[
        center_y - half_size:center_y + half_size,
        center_x - half_size:center_x + half_size
    ]

    gray = grayscale(cropped)
    print(f"The shape of image is: {gray.shape}")
    print(gray)

    transposed = transpose(gray)
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)

    # Display original grayscale
    plt.subplot(1, 2, 1)
    plt.title("Grayscale")
    plt.imshow(gray, cmap='gray')
    plt.xticks(np.arange(0, transposed.shape[1], 50))
    plt.yticks(np.arange(0, transposed.shape[0], 50))

    # Display transposed image
    plt.subplot(1, 2, 2)
    plt.title("Transposed")
    plt.imshow(transposed, cmap='gray')
    plt.xticks(np.arange(0, transposed.shape[1], 50))
    plt.yticks(np.arange(0, transposed.shape[0], 50))
    plt.show()


if __name__ == "__main__":
    main()
