first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_strings = (len(x[0]) - len(x[1]) for x in zip(first, second) if len(x[0]) != len(x[1]))
second_strings = (len(x) == len(y) for x in first for y in second)
# Я не запутался. Правильно ли я сделал первую строку?
# И мне нужна помощь со второй строкой

print(list(first_strings))
print(list(second_strings))
