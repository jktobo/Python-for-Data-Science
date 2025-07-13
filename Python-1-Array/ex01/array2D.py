def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise TypeError("Input must be a list of lists.")
    if len(family) == 0:
        raise ValueError("Family list cannot be empty.")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end must be integers")


    row_length = len(family[0])
    for row in family:
        if not isinstance(row, list):
            raise TypeError("Family must be a 2D list (list of lists).")
        if len(row) != row_length:
            raise ValueError("All rows must have the same length.")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("All elements must be numbers.")

    shape = (len(family), row_length)
    print(f"My shape is : {shape}")

    sliced = family[start:end]
    new_shape = (len(sliced), row_length)
    print(f"My new shape is : {new_shape}")

    return sliced


def main():
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2],
        [5.88, 85.2]
    ]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -3))

if __name__ == "__main__":
    main()
