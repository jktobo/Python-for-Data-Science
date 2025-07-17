from load_image import ft_load

def main():
    path = "landscape.jpg"
    result = ft_load(path)
    if result is not None:
        print(result)

if __name__ == "__main__":
    main()
