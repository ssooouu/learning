first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_strings = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_strings = (len(second[c]) == len(first[c]) for c in range(len(second)))

print(list(first_strings))
print(list(second_strings))

