import mal_types

def pr_str(obj):
    if mal_types.is_list(obj):
        return "(" + " ".join(map(lambda e: pr_str(e), obj)) + ")"
    elif mal_types.is_vector(obj):
        return "[" + " ".join(map(lambda e: pr_str(e), obj)) + "]"
    elif mal_types.is_hash_map(obj):
        ret = []
        for key in obj.keys():
            ret.extend((pr_str(key), pr_str(obj[key])))
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
        else:
            return obj
    return obj.__str__()
