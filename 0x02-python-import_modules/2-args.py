#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 1:
        print("{} arguments.".format(length - 1))
    elif length == 2:
        print("{:d} {}:".format((length - 1), "argument"))
        print("{}: {}".format(1, sys.argv[1]))
    elif length > 2:
        print("{:d} {:s}:".format((length - 1), "arguments"))
        for i in range(1, (length)):
            print("{}: {}".format(i, sys.argv[i]))
