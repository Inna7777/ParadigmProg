# Пример 1: Обработка данных с использованием функционального программирования

# Импортируем функции из модуля functools
from functools import reduce

# Функция для фильтрации студентов младше 22 лет
def filter_young_students(student):
    return student["age"] < 22

# Функция для вычисления среднего балла студентов
def calculate_average_score(students):
    total_score = reduce(lambda x, y: x + y, [student["score"] for student in students])
    return total_score / len(students)

# Отфильтровать студентов
students = [
    {"name": "Alice", "age": 22, "score": 95},
    {"name": "Bob", "age": 21, "score": 88},
    {"name": "Charlie", "age": 23, "score": 92},
    {"name": "David", "age": 22, "score": 78},
]

young_students = list(filter(filter_young_students, students))

# Вычислить средний балл
average_score = calculate_average_score(students)

print("Пример 1: Обработка данных с использованием функционального программирования")
print(young_students)
print(average_score)

