def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            for g in i:
                try:
                    result += g
                except TypeError:
                    print(f'Некорректный тип данных для подсчёта суммы - {g}')
                    incorrect_data += 1
        except TypeError:
            incorrect_data += 1
        return (result, incorrect_data)


def calculate_average(*numbers):
    result = personal_sum(numbers)
    count = 0
    for i in numbers:
        if isinstance(i, int):
            print('Такой пример не подходит')
        else:
            for g in i:
                if isinstance(g, str):
                    continue
                else:
                    count += 1
    try:
        res = result[0] / count
    except ZeroDivisionError:
        return 0
    return res



print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
