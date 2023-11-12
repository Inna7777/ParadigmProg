# Пример 2: Работа с функциями высшего порядка

numbers = [1, 2, 3, 4, 5]

# Функция для применения серии функций к числу
def apply_operations(num, operations):
    result = num
    for operation in operations:
        result = operation(result)
    return result

# Операции, которые будут применены к числам
operations = [
    lambda x: x * 2,
    lambda x: x + 3,
    lambda x: x ** 2,
]

# Применить операции к числам
result = list(map(lambda x: apply_operations(x, operations), numbers))

print("\nПример 2: Работа с функциями высшего порядка")
print(result)

# Генерация списка списков с числами от 1 до 3 в каждом внутреннем списке
matrix = [[x for x in range(1, 4)] for _ in range(3)]
print(matrix)

