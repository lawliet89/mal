#!/usr/bin/env python3
from sys import stdin


def READ(str):
    return str

def EVAL(str):
    return str

def PRINT(str):
    return str

def rep(str):
    return PRINT(EVAL(READ(str)))

def main():
    while True:
        print('user> ', end="", flush=True)
        print(rep(stdin.readline()), end="", flush=True)

if __name__ == "__main__":
    main()

# Add full line editing and command history support to your interpreter REPL.
# https://github.com/kanaka/mal/blob/master/process/guide.md#optional
