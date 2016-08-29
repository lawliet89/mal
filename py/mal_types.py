class Symbol(str):
    @staticmethod
    def is_symbol(obj):
        return obj is Symbol

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
