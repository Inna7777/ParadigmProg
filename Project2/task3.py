# Структурное программирование
start = 10
end = 50
prime_numbers = []

def digit_is_simple(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

# Проверяем каждое число в диапазоне на простоту
def get_simple_digits(start, end):
    for num in range(start, end + 1):
        if num > 1:
            if (digit_is_simple(num)):
                prime_numbers.append(num)

get_simple_digits(start, end)
print(f"Простые числа в диапазоне от {start} до {end}: {prime_numbers}")