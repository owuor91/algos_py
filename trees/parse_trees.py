import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

LEFT_PAREN = '('
RIGHT_PAREN = ')'


def build_parse_tree(expression):
    tree = {}
    stack = [tree]
    node = tree

    for token in expression:
        if token == LEFT_PAREN:
            node['left'] = {}
            stack.append(node)
            node = node['left']
        elif token == RIGHT_PAREN:
            node = stack.pop()
        elif token in OPERATORS:
            node['val'] = token
            node['right'] = {}
            stack.append(node)
            node = node['right']
        else:
            node['val'] = int(token)
            parent = stack.pop()
            node = parent
    return tree
