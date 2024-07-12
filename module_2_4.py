numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    is_Prime = True
    if i < 2:
        is_Prime = False
    else:
        for j in range(2, int(i) + 1):
            if (i % j // 2) == 0:
                is_Prime = True
            else:
                is_Prime = False

    if is_Prime:
        primes.append(i)
    elif is_Prime == False:
        not_primes.append(i)

print('Простые числа: ', primes)
print('Составные числа: ', not_primes)