#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
