import re
import mal_types

class Reader():
    def __init__(self, tokens, position=0):
        self.tokens = tokens
        self.position = position

    def next(self):
        self.position += 1
        return self.tokens[self.position-1]

    def peek(self):
        if len(self.tokens) > self.position:
            return self.tokens[self.position]
        else:
            return None

def tokenizer(str):
    regex = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s\[\]{}()'"`@,;]+)""")
    tokens = [token for token in re.findall(regex, str) if token[0] != ';']
    return tokens

def read_sequence(reader, seq_type, start_token, end_token):
    ast = seq_type()
    if reader.next() != start_token: # consume the start token
        raise Exception("expected '" + start_token + "'")

    token = reader.peek()
    while token != end_token:
        if not token:
            raise Exception("expected '" + end_token + "', got EOF")
        ast.append(read_from(reader))
        token = reader.peek()
    reader.next() # Consume the end token
    return ast

def read_atom(reader):
    int_re = re.compile(r"-?[0-9]+$")
    float_re = re.compile(r"-?[0-9][0-9.]*$")
    token = reader.next()
    if re.match(int_re, token):
        return int(token)
    elif re.match(float_re, token):
        return float(token)
    elif token == "nil":
        return None
    elif token == "true":
        return True
    elif token == "false":
        return False
    elif token[0] == ':':
        return mal_types.keyword(token[1:])
    else:
        return mal_types.Symbol(token)

def read_list(reader):
    return read_sequence(reader, list, '(', ')')

def read_vector(reader):
    return read_sequence(reader, mal_types.Vector, '[', ']')

def read_hash_map(reader):
    sequence = read_sequence(reader, list, '{', '}')
    return { sequence[i]: sequence[i + 1] for i in range(0, len(sequence), 2) }

def read_from(reader):
    token = reader.peek()
    # macros and transformations
    if token[0] == ';':
        reader.next()
        return None
    elif token == '\'':
        reader.next()
        return [mal_types.Symbol('quote'), read_from(reader)]
    elif token == '`':
        reader.next()
        return [mal_types.Symbol('quasiquote'), read_from(reader)]
    elif token == '~':
        reader.next()
        return [mal_types.Symbol('unquote'), read_from(reader)]
    elif token == '~@':
        reader.next()
        return [mal_types.Symbol('splice-unquote'), read_from(reader)]
    elif token == '^':
        reader.next()
        meta = read_from(reader)
        return [mal_types.Symbol('with-meta'), read_from(reader), meta]
    elif token == '@':
        reader.next()
        return [mal_types.Symbol('deref'), read_from(reader)]
    elif token == '(':
        return read_list(reader)
    elif token == '[':
        return read_vector(reader)
    elif token == "{":
        return read_hash_map(reader)
    else:
        return read_atom(reader)

def read_str(str):
    tokens = tokenizer(str)
    if len(tokens) == 0:
        raise Exception("Blank Line")
    return read_from(Reader(tokens))
