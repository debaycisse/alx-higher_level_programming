#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as c
    import sys
    args_len = len(sys.argv)
    if args_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if operator == '+':
        print(c.add(a, b))
        sys.exit(0)
    elif operator == '-':
        print(c.sub(a, b))
        sys.exit(0)
    elif operator == '*':
        print(c.mul(a, b))
        sys.exit(0)
    elif operator == '/':
        print(c.div(a, b))
        sys.exit(0)
