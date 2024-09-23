data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*arg):
    donvenient_variable = []
    open_dictionary = []
    final = []
    for i in arg:
        for j in i:
            for k in j:
                if isinstance(j, dict):
                    donvenient_variable.append(tuple(j.values()))
                    donvenient_variable.append(tuple(j.keys()))
                    break
                elif isinstance(k, dict):
                    donvenient_variable.append(tuple(k.values()))
                    donvenient_variable.append(tuple(k.keys()))
                    break
                elif isinstance(k, int) or isinstance(k, str):
                    donvenient_variable.append(k)
                elif isinstance(k, list):
                    for s in list(k):
                        for g in s:
                            for t in g:
                                if isinstance(t, int) or isinstance(t, str):
                                    donvenient_variable.append(t)
                                if isinstance(t, tuple):
                                    donvenient_variable.append(t)
    for h in donvenient_variable:
        if isinstance(h, tuple):
            for v in h:
                if isinstance(v, int):
                    final.append(v)
                if isinstance(v, str):
                    final.append(len(v))
        if isinstance(h, int):
            final.append(h)
            continue
        if isinstance(h, str):
            final.append(len(h))
            continue
    final1 = sum(final)

    return final1


result = calculate_structure_sum(data_structure)
print(result)
