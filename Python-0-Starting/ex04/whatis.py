# import sys

# def main():
#     if len(sys.argv) < 2:
#         return
    
#     if len(sys.argv) > 2:
#         print("AssertionError: more than one argument is provided")
#         sys.exit(1)

#     if not sys.argv[1].lstrip("-").isdigit():
#         print("AssertionError: argument is not an integer")
#         sys.exit(1)

#     arg = int(sys.argv[1])

#     if (arg % 2 == 0):
#         print("I'm Even.")
#     else:
#         print("I'm Odd.")

# if __name__ == "__main__":
#     main()


import sys

def main():
    if len(sys.argv) == 1:
        return
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        else:
            raise AssertionError("argument is not an integer")

    try:
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")

