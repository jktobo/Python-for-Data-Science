from load_image import ft_load

def main():
    path = "landscape.jpg"  # заменяешь на своё изображение, если нужно
    result = ft_load(path)
    if result is not None:
        print(result)

if __name__ == "__main__":
    main()
