from load_image import ft_load
from pimp_image import show_images


def main():
    array = ft_load("landscape.jpg")
    if array is None:
        return
    show_images(array)

    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
