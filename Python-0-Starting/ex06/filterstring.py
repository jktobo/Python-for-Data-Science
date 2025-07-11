
import sys
from ft_filter import ft_filter


def main():
    """
    Main function to filter words from the input text based on their length.

    This function:
    - Accepts two command-line arguments: a string (`text`) and
    an integer (`num`).
    - Splits the input string into words.
    - Filters the words that have a length greater than `num`.
    - Prints the filtered list of words.
    """
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    S = sys.argv[1]
    try:
        N = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")
    if not isinstance(S, str) or not isinstance(N, int):
        raise AssertionError("the arguments are bad")

    words = S.split()
    result = ft_filter(lambda word: len(word) > N, words)
    print(result)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")
