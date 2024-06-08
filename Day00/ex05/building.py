import sys


def parser(string: str):
    """
    Parse the string porvided and returns informations
    about it, exemple :
        - Number of characters
        - Number of lower letters
        - Number of upper letters
        - Number of punctuation letters
        - Number of whitespaces
        - Number of digits
    """
    punctuationMarks = 0
    print(f" The text contains {len(string)} characters:")
    print(f"{sum(1 for c in string if c.isupper())} upper letters")
    print(f"{sum(1 for c in string if c.islower())} lower letters")
    for i in range(0, len(string)):
        if string[i] in ('!', ",", "\'", ";", "\"", ".", "-", "?"):
            punctuationMarks += 1
    print(f"{punctuationMarks} punctuation marks")
    print(f"{sum(1 for c in string if c.isspace())} spaces")
    print(f"{sum(1 for c in string if c.isdigit())} digits")


def main():
    """
    It uses the string provided in arguments of the program
    If None or nothing is provided, the user is prompted to provide a string.
    If more than one argument is provided to the program,
    it raises an AssertionError.
    """
    try:
        if len(sys.argv) < 2:
            try:
                stdin = input("What is the text to count?\n")
                stdin += "\n"
                parser(stdin)
            except EOFError:
                sys.exit(0)
            sys.exit(0)
        if len(sys.argv) > 2:
            raise AssertionError("Assertion Error: more than one argument \
is provided")
        parser(sys.argv[1])
    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
