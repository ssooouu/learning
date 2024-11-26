def add_everything_up(a, b):
    try:
        d = a + b
        return d
    except:
        a = f'{a}'
        b = f'{b}'
        d = a + b
        return d


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
