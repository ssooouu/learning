calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    global calls
    calls += 1
    print(len(string), string.lower(), string.upper())

def is_contains(string, list_to_search):
    n = 0
    w = 0
    global calls
    calls += 1
    while n < len(list_to_search):
        if string.lower() == list_to_search[n].lower():
            print(True)
        if string.lower() != list_to_search[n].lower():
            n += 1
            continue
        print(False)
        break
# У меня в ответе почему то получаются какие то None. Откуда они берутся и что это вообще такое?
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

