#!/usr/bin/python3
if __name__ == "__main__":
    def print_arg(argv):

        """Print the number and lists of its arguments."""
    import sys
    print_arg(sys.argv)

    number = len(sys.argv) - 1
    if number == 0:
        print("0-arguments.")
    elif number == 1:
        print("1-argument:")
    else:
        print("{} arguments:".format(number))
    for i in range(number):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
