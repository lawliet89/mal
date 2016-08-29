import mal_types
import printer

# String functions
def pr_str(*args):
    return ' '.join(map(lambda s: printer.pr_str(s, True), args))

def str_args(*args):
    return ''.join(map(lambda s: printer.pr_str(s, False), args))

def prn(*args):
    print(' '.join(map(lambda s: printer.pr_str(s, True), args)))
    return None

def println(*args):
    print(' '.join(map(lambda s: printer.pr_str(s, False), args)))
    return None

def list_args(*args):
    return list(args)

def count(obj):
    if mal_types.is_nil(obj):
        return 0
    else:
        return len(obj)

ns = {
        '<':  lambda a,b: a<b,
        '<=': lambda a,b: a<=b,
        '>':  lambda a,b: a>b,
        '>=': lambda a,b: a>=b,
        '+':  lambda a,b: a+b,
        '-':  lambda a,b: a-b,
        '*':  lambda a,b: a*b,
        '/':  lambda a,b: int(a/b),

        'pr-str': pr_str,
        'str': str_args,
        'prn': prn,
        'println': println,

        'list': list_args,
        'list?': mal_types.is_list,
        'empty?': lambda l: len(l) == 0,
        'count': count,
        '=': mal_types.is_equal
}
