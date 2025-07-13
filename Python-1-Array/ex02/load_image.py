import numpy as np
from PIL import Image

def ft_load(path: str) -> np.ndarray:
    try:
        # Открываем файл
        img = Image.open(path)

        # Принудительно переводим в RGB, если вдруг не RGB
        img = img.convert('RGB')

        # Переводим в numpy-массив
        img_array = np.array(img)

        # Выводим shape
        print(f"The shape of image is: {img_array.shape}")

        return img_array

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Error loading image: {e}")
