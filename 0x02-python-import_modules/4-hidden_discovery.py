#!/usr/bin/python3
if __name__ == "__main__":
    items = []
    for name in dir('hidden_4.pyc'):
        items.append(name)
    items.sort()
    for name in items:
        print(name)
