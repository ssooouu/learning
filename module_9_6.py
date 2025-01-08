def all_variants(text):
    for size in range(len(text)):
        for l in range(len(text) - size):
            yield text[l:l + size + 1]

a = all_variants("abc")
for i in a:
    print(i)
