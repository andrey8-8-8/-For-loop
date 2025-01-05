def get_matrix(n, m, value):
    matrix = []  # Создаем пустой список для матрицы
    for i in range(n):  # Внешний цикл для строк
        row = []  # Создаем пустой список для строки
        for j in range(m):  # Внутренний цикл для столбцов
            row.append(value)  # Добавляем значение в строку
        matrix.append(row)  # Добавляем строку в матрицу
    return matrix  # Возвращаем заполненную матрицу

# Примеры использования функции
result1 = get_matrix(2, 3, 120)
result2 = get_matrix(4, 5, 50)
result3 = get_matrix(6, 3, 33)

# Вывод результатов на экран
print(result1)  # Вывод: [[10, 10], [10, 10]]
print(result2)  # Вывод: [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
print(result3)  # Вывод: [[13, 13], [13, 13], [13, 13], [13, 13]]
print('Andrey')
