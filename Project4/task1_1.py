squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Вывод: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x   for x in numbers    if x % 2 == 0]
print(even_numbers)  # Вывод: [2, 4, 6, 8, 10]

# Создание множества, содержащего квадраты чисел от 1 до 5
squares_set = {x ** 2 for x in range(1, 6)}
print(squares_set)  # Вывод: {1, 4, 9, 16, 25}

# Создание словаря, где ключами являются числа от 1 до 5, а значениями - их квадраты
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(squares_dict)  # Вывод: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}