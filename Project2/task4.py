# Определение функции selection_sort, которая принимает список arr в качестве параметра.

def get_min_index(arr, n, i):
    min_index = i
    # Внутренний цикл для поиска минимального элемента в оставшейся части списка.
    for j in range(i + 1, n):
        # Проверка, является ли элемент с индексом j меньшим, чем элемент с индексом min_index.
        if arr[j] < arr[min_index]:
            # Если условие выполняется, обновляем min_index.
            min_index = j
    return min_index

def switch_arr_elms(arr, i, min_index):
    arr[i], arr[min_index] = arr[min_index], arr[i]

def selection_sort(arr):
    # Вычисление длины списка arr и сохранение в переменной n.
    n = len(arr) # 7

    # Внешний цикл от 0 до n-1 для прохода по всем элементам списка arr.
    for i in range(n):
        # Инициализация переменной min_index с текущим значением i.
        min_index = get_min_index(arr, n, i)

        # После завершения внутреннего цикла меняем местами элементы arr[i] и arr[min_index],
        # чтобы поместить минимальный элемент на правильную позицию в отсортированной части списка.
        switch_arr_elms(arr, i, min_index)


# Создание списка my_array с неупорядоченными значениями.
my_array = [64, 34, 25, 12, 22, 11, 90]

# Вызов функции selection_sort для сортировки списка my_array.
selection_sort(my_array)

# Вывод отсортированного списка.
print("Отсортированный массив (Selection Sort):", my_array)