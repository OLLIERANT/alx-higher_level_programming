#!/usr/bin/python3
def print_arg(argv):
    number = len(argv) - 1
    if number == 0:
        print("{:d} argument.".format(number))
        return
    else:
        if number == 1:
            print("{:d} argument:".format(number))
        else:
            print("{:d} arguments:".format(number))
        i = 1
        while i <= number:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1


if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
