calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    len(string), string.lower(), string.upper()
    return (len(string), string.lower(), string.upper())

def is_contains(string, list_to_search):
    n = 0
    count_calls()
    while n < len(list_to_search):
        if string.lower() == list_to_search[n].lower():
            return (True)
        elif string.lower() != list_to_search[n].lower():
            n += 1
            continue
    return (False)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

