import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
}


def encode_to_morse(text):
    """
    Encodes a given string into Morse code.

    This function takes a string, converts all characters to uppercase,
    and returns a string representing the Morse code equivalent. Each
    character is mapped to its Morse code representation as defined in
    the `NESTED_MORSE` dictionary.
    """
    morse_code = ""
    for char in text.upper():
        if char in NESTED_MORSE:
            morse_code += NESTED_MORSE[char]
        else:
            raise AssertionError("the arguments are bad")
    return morse_code.strip()


def main():
    """
    Main function that processes command-line arguments to encode a
    string to Morse code.
    """
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    try:
        input_string = sys.argv[1]
        print(encode_to_morse(input_string))
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except AssertionError:
        raise AssertionError("the arguments are bad")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")
