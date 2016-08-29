#!/usr/bin/env python3
import sys
import reader
import printer
import traceback


def READ(str):
    return reader.read_str(str)

def EVAL(ast):
    return ast

def PRINT(ast):
    return printer.pr_str(ast)

def rep(str):
    return PRINT(EVAL(READ(str)))

def main():
    while True:
        try:
            print("user> ", end="", flush=True)
            line = sys.stdin.readline()
            if line == "":
                return 0
            print(rep(line), flush=True)
        except Exception as e:
            print("".join(traceback.format_exception(*sys.exc_info())))

if __name__ == "__main__":
    main()

# Add full line editing and command history support to your interpreter REPL.
# https://github.com/kanaka/mal/blob/master/process/guide.md#optional
