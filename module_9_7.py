def isprime(funk):
    def determinant(*args):

        result = funk(*args)

        if result % 2 != 0:
            print('Простое')
        else:
            print("Составное")
        return result

    return determinant


@isprime
def sum_three(*args):
    res = 0
    for c in args:
        res += c
    return res


result = sum_three(2, 3, 6)
print(result)
