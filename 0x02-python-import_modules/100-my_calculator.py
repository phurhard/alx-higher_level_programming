#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    import sys
    length = len(sys.argv)
    if length < 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    if length == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            print("{} {} {} = {}".format(a, sys.argv[2], b, cal.add(a, b)))
        elif sys.argv[2] == '-':
            print("{} {} {} = {}".format(a, sys.argv[2], b, cal.sub(a, b)))
        elif sys.argv[2] == '*':
            print("{} {} {} = {}".format(a, sys.argv[2], b, cal.mul(a, b)))
        elif sys.argv[2] == '/':
            print("{} {} {} = {}".format(a, sys.argv[2], b, cal.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
