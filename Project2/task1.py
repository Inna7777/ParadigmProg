def factorial(n):
    if n < 0:
        return None  # Факториал не определен для отрицательных чисел
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5
fact = factorial(number)
if fact is not None:
    print(f"Факториал числа {number} равен {fact}")
else:
    print("Факториал не определен для отрицательных чисел")


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return None  # Защита от деления на ноль
    return x / y

# Вызываем процедуры (функции)
a = 10
b = 5
sum_result = add(a, b)
diff_result = subtract(a, b)
prod_result = multiply(a, b)
div_result = divide(a, b)

print(f"Сумма: {a} + {b} = {sum_result}")
print(f"Разность: {a} - {b} = {diff_result}")
print(f"Произведение: {a} * {b} = {prod_result}")
if div_result is not None:
    print(f"Деление: {a} / {b} = {div_result}")
else:
    print("Деление на ноль невозможно")