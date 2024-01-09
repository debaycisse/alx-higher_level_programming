def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple(tuple_a[i] if i < len(tuple_a) else 0 for i in range(2))
    b = tuple(tuple_b[i] if i < len(tuple_b) else 0 for i in range(2))
    return tuple(a[i] + b[i] for i in range(2))
