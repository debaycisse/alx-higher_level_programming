def add_tuple(tuple_a=(), tuple_b=()):
    n_tuple_a, n_tuple_b = (0, 0), (0, 0)
    if len(tuple_a) == 2 and len(tuple_b) == 2:
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    if len(tuple_a) == 0:
        pass
    elif len(tuple_a) == 1:
        if tuple_a[0]:
            n_tuple_a = (tuple_a[0], 0)
        else:
            n_tuple_a = (0, tuple_a[1])
    elif len(tuple_a) > 2:
        n_tuple_a = (tuple_a[0], tuple_a[1])
    else:
        n_tuple_a = (tuple_a[0], tuple_a[1])

    if len(tuple_b) == 0:
        pass
    elif len(tuple_b) == 1:
        if tuple_b[0]:
            n_tuple_b = (tuple_b[0], 0)
        else:
            n_tuple_b = (0, tuple_b[1])
    elif len(tuple_b) > 2:
        n_tuple_b = (tuple_b[0], tuple_b[1])
    else:
        n_tuple_a = (tuple_a[0], tuple_a[1])

    return (n_tuple_a[0] + n_tuple_b[0], n_tuple_a[1] + n_tuple_b[1])
