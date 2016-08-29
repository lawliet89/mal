#!/usr/bin/env python3
import sys
import reader
import printer
import traceback
import mal_types

def READ(str):
    return reader.read_str(str)

def eval_ast(ast, env):
    if mal_types.is_symbol(ast):
        try:
            return env[ast]
        except:
            raise Exception("'" + ast + "' not found")
    elif mal_types.is_list(ast):
        return list(map(lambda x: EVAL(x, env), ast))
    elif mal_types.is_vector(ast):
        return mal_types.Vector(map(lambda x: EVAL(x, env), ast))
    elif mal_types.is_hash_map(ast):
        return { key: EVAL(value, env) for key, value in ast.items() }
    else:
        return ast


def EVAL(ast, env):
    if mal_types.is_list(ast):
        if len(ast) == 0:
            return ast
        else:
            eval = eval_ast(ast, env)
            return eval[0](*eval[1:])
    else:
        return eval_ast(ast, env)

def PRINT(ast):
    return printer.pr_str(ast)

def rep(str, env):
    return PRINT(EVAL(READ(str), env))

def main():
    repl_env = dict()
    repl_env['+'] = lambda a,b: a+b
    repl_env['-'] = lambda a,b: a-b
    repl_env['*'] = lambda a,b: a*b
    repl_env['/'] = lambda a,b: int(a/b)

    while True:
        try:
            print("user> ", end="", flush=True)
            line = sys.stdin.readline()
            if line == "":
                return 0
            print(rep(line, repl_env), flush=True)
        except Exception as e:
            print("".join(traceback.format_exception(*sys.exc_info())))

if __name__ == "__main__":
    main()

# Add full line editing and command history support to your interpreter REPL.
# https://github.com/kanaka/mal/blob/master/process/guide.md#optional
