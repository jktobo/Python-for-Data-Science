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

        # Поворот 90° по часовой стрелке
        rotated = np.transpose(img, (1, 0, 2))  # меняем оси
        rotated = np.flip(rotated, axis=1)      # переворачиваем

        print(f"Rotated shape: {rotated.shape}")
        print(rotated)

        plt.imshow(rotated)
        plt.title("Rotated Image 90°")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
