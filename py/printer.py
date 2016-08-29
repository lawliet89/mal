import mal_types

def _escape(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

def pr_str(obj, print_readably=True):
    if mal_types.is_list(obj):
        return "(" + " ".join(map(lambda e: pr_str(e, print_readably), obj)) + ")"
    elif mal_types.is_vector(obj):
        return "[" + " ".join(map(lambda e: pr_str(e, print_readably), obj)) + "]"
    elif mal_types.is_hash_map(obj):
        ret = []
        for key in obj.keys():
            ret.extend((pr_str(key, print_readably), pr_str(obj[key], print_readably)))
        return "{" + " ".join(ret) + "}"
    elif mal_types.is_symbol(obj):
        return obj
    elif mal_types.is_nil(obj):
        return 'nil'
    elif mal_types.is_true(obj):
        return 'true'
    elif mal_types.is_false(obj):
        return 'false'
    elif type(obj) == str:
        if mal_types.is_keyword(obj):
            return ':' + obj[1:]
        elif print_readably:
            return '"' + _escape(obj) + '"'
        else:
            return obj
    return obj.__str__()
