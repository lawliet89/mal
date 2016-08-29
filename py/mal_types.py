class Symbol(str):
    pass


class Vector(list):
    pass


def keyword(str):
    if str[0] == "\u029e":
        return str
    else:
        return "\u029e" + str


def is_keyword(exp):
    if type(exp) == str:
        return len(exp) != 0 and exp[0] == "\u029e"
    else:
        return False

def is_true(obj):
    return obj is True


def is_false(obj):
    return obj is False


def is_nil(obj):
    return obj is None

def is_list(obj):
    return type(obj) == list

def is_symbol(obj):
    return type(obj) == Symbol

def is_vector(obj):
    return type(obj) == Vector

def is_hash_map(obj):
    return type(obj) == dict
