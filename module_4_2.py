def test_function():
    def inner_function():
        print('Я в области видимости функции: test_function')
    inner_function()

test_function()
inner_function()
# при таком вызове функций будет ошибка потому, что функция inner_function() относится к локальному пространству имен
