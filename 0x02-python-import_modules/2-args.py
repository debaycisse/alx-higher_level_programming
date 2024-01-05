#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    if args == 2:
        print("1 argument:")
    elif args > 2:
        print("{} arguments:". format(args - 1))
    for ag in range(1, args):
        print("{}: {}".format(ag, sys.argv[ag]))
