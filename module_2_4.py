numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    is_Prime = True
    if i < 2:
        is_Prime = False
    else:
        for j in numbers:
            if (i % j) == 0:
                is_Prime = True

    if is_Prime == True:
        primes.append(i)

    else:
        not_primes.append(i)

print('Простые числа: ', primes)
print('Составные числа: ', not_primes)