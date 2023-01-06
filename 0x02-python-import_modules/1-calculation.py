#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    a = 10
    b = 5
    # ADD
    print("{} + {} = {}".format(a, b, cal.add(a, b)))
    # SUBTRACT
    print("{} + {} = {}".format(a, b, cal.sub(a, b)))
    # MULTIPLY
    print("{} + {} = {}".format(a, b, cal.mul(a, b)))
    # DIVIDE
    print("{} + {} = {}".format(a, b, cal.div(a, b)))
