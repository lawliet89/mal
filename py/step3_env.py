#!/usr/bin/env python3
import sys
import reader
import printer
import traceback
import mal_types
from env import Env

def READ(str):
    return reader.read_str(str)

def eval_ast(ast, env):
    if mal_types.is_symbol(ast):
        try:
            return env.get(ast)
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
            operator = ast[0]
            if operator == "def!":
                key = ast[1]
                result = EVAL(ast[2], env)
                return env.set(key, result)
            elif operator == "let*":
                let_env = Env(env)
                bindings, expr = ast[1], ast[2]
                for i in range(0, len(bindings), 2):
                    let_env.set(bindings[i], EVAL(bindings[i + 1], let_env))
                return EVAL(expr, let_env)
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
    repl_env = Env(None)
    repl_env.set(mal_types.Symbol('+'), lambda a,b: a+b)
    repl_env.set(mal_types.Symbol('-'), lambda a,b: a-b)
    repl_env.set(mal_types.Symbol('*'), lambda a,b: a*b)
    repl_env.set(mal_types.Symbol('/'), lambda a,b: int(a/b))

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
