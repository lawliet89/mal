import mal_types

def prn(*args):
    pr_str(args[0], True)
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

        'prn': prn,
        'list': list_args,
        'list?': mal_types.is_list,
        'empty?': lambda l: len(l) == 0,
        'count': count,
        '=': mal_types.is_equal
}
