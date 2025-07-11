import sys
import string


def chekc_func(text):
    """
    Analyzes the given text and prints the counts of different character types.

    This function takes a string and counts the following types of characters:
    - Uppercase letters
    - Lowercase letters
    - Punctuation marks
    - Spaces
    - Digits

    Parameters:
    text (str): The text to analyze.

    Outputs:
    Prints the total count of each character type in the text.
    """
    print(f"The text contains {len(text)} characters:")
    print(f"{sum(1 for ch in text if ch.isupper())} upper letters")
    print(f"{sum(1 for ch in text if ch.islower())} lower letters")
    print(f"{sum(1 for ch in text if ch in string.punctuation)}"
          " punctuation marks")
    print(f"{sum(1 for ch in text if ch.isspace())} spaces")
    print(f"{sum(1 for ch in text if ch.isdigit())} digits")


def main():
    """
    Main function that handles input and invokes chekc_func
    to analyze the text.

    This function checks if the script is called with a text argument or if it
    prompts the user to input a text. If more than one argument is provided,
    an AssertionError is raised.

    It then calls chekc_func to display the analysis of the provided text.
    """
    try:
        if len(sys.argv) == 1:
            while (True):
                text = input("What is the text to count?\n")
                if not text:
                    continue
                else:
                    break
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        else:
            text = sys.argv[1]
        chekc_func(text)
    except AssertionError as ae:
        print(f"AssertionError: {ae}")


if __name__ == "__main__":
    main()
