#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return a / b
    except Exception:
        result = None
    finally:
        print(f"Inside result: {result}")
