import random

def rand_expr(func_set, term_set, max_d):
    arg = []
    if max_d == 0:
        expr = term_set[random.randint(0, len(term_set) - 1)]
    else:
        func = func_set[random.randint(0, len(func_set) - 1)]
        for i in range(2):
            arg.append(rand_expr(func_set, term_set, max_d - 1))
        expr = func
        for j in arg:
            expr = expr + j
    return expr

FUNC = ['+', '-', '*', '/']
TERM = ['x']

print(rand_expr(FUNC, TERM, 3))
