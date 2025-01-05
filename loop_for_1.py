numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    if num == 1:  # Пропускаем число 1
        continue

    is_prime = True  # Предполагаем, что число простое

    for divisor in range(2, num):  # Проверяем делители
        if num % divisor == 0:  # Если делится на divisor
            is_prime = False  # Устанавливаем флаг в False
            break  # Прерываем цикл, если нашли делитель

    if is_prime:
        primes.append(num)  # Добавляем в список простых
    else:
        not_primes.append(num)  # Добавляем в список составных

# Выводим результаты
print("Primes:", primes)
print("Not Primes:", not_primes)
