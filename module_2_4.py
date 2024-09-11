numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    for j in numbers[1: ]:
        if i % j == 0 and i / j != 1:
            not_primes.append(i)
            break
        if i % j == 0 and i / j == 1:
            primes.append(i)
            break
        if i / j <= 1:
            break
print(primes)
print(not_primes)
