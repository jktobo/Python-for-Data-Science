# tester.py
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt

def main():
    array = ft_load("landscape.jpg")
    if array is None:
        return

    invert_img = ft_invert(array)
    red_img = ft_red(array)
    green_img = ft_green(array)
    blue_img = ft_blue(array)
    grey_img = ft_grey(array)

    fig, axes = plt.subplots(3, 2, figsize=(10, 12))

    axes[0, 0].imshow(array)
    axes[0, 0].set_title("Figure VIII.1: Original")
    axes[0, 0].axis('off')

    axes[0, 1].imshow(invert_img)
    axes[0, 1].set_title("Figure VIII.2: Invert")
    axes[0, 1].axis('off')

    axes[1, 0].imshow(red_img)
    axes[1, 0].set_title("Figure VIII.3: Red")
    axes[1, 0].axis('off')

    axes[1, 1].imshow(green_img)
    axes[1, 1].set_title("Figure VIII.4: Green")
    axes[1, 1].axis('off')

    axes[2, 0].imshow(blue_img)
    axes[2, 0].set_title("Figure VIII.5: Blue")
    axes[2, 0].axis('off')

    axes[2, 1].imshow(grey_img, cmap='gray')
    axes[2, 1].set_title("Figure VIII.6: Grey")
    axes[2, 1].axis('off')

    plt.tight_layout(h_pad=0.3, w_pad=0.3)
    plt.show()

    print(ft_invert.__doc__)

if __name__ == "__main__":
    main()



# from load_image import ft_load
# from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
# ...
# array = ft_load("landscape.jpg")
# ft_invert(array)
# ft_red(array)
# ft_green(array)
# ft_blue(array)
# ft_grey(array)
# print(ft_invert.__doc__)