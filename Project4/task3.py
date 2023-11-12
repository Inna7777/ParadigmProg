def merge_sort(arr):
    # Проверяем базовый случай: если массив содержит 1 элемент или менее, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Разделение массива на две части
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Рекурсивная сортировка каждой части
    left_half = merge_sort(left_half)  # Рекурсивный вызов merge_sort для левой части
    right_half = merge_sort(right_half)  # Рекурсивный вызов merge_sort для правой части

    # Слияние отсортированных частей
    return merge(left_half, right_half)  # Вызов функции merge для слияния

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    # Слияние отсортированных частей
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Добавление оставшихся элементов, если такие есть
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

# Пример использования
unsorted_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(unsorted_list)  # Вызываем merge_sort для сортировки
print(sorted_list)  # Вывод: [3, 9, 10, 27, 38, 43, 82]