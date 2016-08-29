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

def is_string(obj):
    return type(obj) == str

def is_sequential(obj):
    return is_list(obj) or is_vector(obj)

def is_equal(a, b):
    type_a, type_b = type(a), type(b)
    if is_string(a) and is_string(b):
        return a == b
    if not (type_a == type_b or (is_sequential(a) and is_sequential(b))):
        return False;
    if is_symbol(a):
        return a == b
    elif is_list(a) or is_vector(a):
        if len(a) != len(b): return False
        for i in range(len(a)):
            if not is_equal(a[i], b[i]): return False
        return True
    elif is_hash_map(a):
        akeys = a.keys()
        akeys.sort()
        bkeys = b.keys()
        bkeys.sort()
        if len(akeys) != len(bkeys): return False
        for i in range(len(akeys)):
            if akeys[i] != bkeys[i]: return False
            if not is_equal(a[akeys[i]], b[bkeys[i]]): return False
        return True
    else:
        return a == b
