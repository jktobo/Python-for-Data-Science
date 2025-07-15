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

        # === Invert filter ===
        inverted = 255 - img

        print(f"Inverted shape: {inverted.shape}")
        print(inverted)

        plt.imshow(inverted)
        plt.title("Inverted Image")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()

        # === Switch channels ===
        switched = img[:, :, [2, 1, 0]]

        plt.imshow(switched)
        plt.title("Switched Channels (BGR)")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()

        # === Grayscale ===
        gray = np.dot(img[...,:3], [0.299, 0.587, 0.114])
        gray_rgb = np.stack((gray,)*3, axis=-1).astype(np.uint8)

        plt.imshow(gray_rgb)
        plt.title("Grayscale Image")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
