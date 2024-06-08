import sys

try:
    if len(sys.argv) < 2:
        sys.exit(1)
    if len(sys.argv) != 2:
        raise AssertionError("Assertion Error: more than one argument \
is provided")
    try:
        value = int(sys.argv[1])
    except ValueError:
        raise AssertionError("Assertion Error: argument is not an integer")

    if value % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as e:
    print(e)
    sys.exit(1)
