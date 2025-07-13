import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def main():
    try:
        img = ft_load("animal.jpeg")
        if img is None:
            return

        print(f"Original shape: {img.shape}")
        print(img)

        # Например, возьмём квадрат 400x400 в центре
        center_x = img.shape[1] // 2
        center_y = img.shape[0] // 2

        half_size = 200  # половина от 400
        x_start = center_x - half_size
        x_end = center_x + half_size
        y_start = center_y - half_size
        y_end = center_y + half_size

        zoomed = img[y_start:y_end, x_start:x_end, :]

        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)

        plt.imshow(zoomed)
        plt.title("Zoomed Image")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
