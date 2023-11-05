#Структурное программирование  в том, что
#  задача  разделена на более мелкие функции и последовательное их выполнения.

# Функция  разделения массива на две половины
def split_array(arr):
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return left_half, right_half

# Функция  слияния двух отсортированных массивов
def merge(left_half, right_half):
    i = j = 0
    merged_arr = []

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged_arr.append(left_half[i])
            i += 1
        else:
            merged_arr.append(right_half[j])
            j += 1

    merged_arr += left_half[i:]
    merged_arr += right_half[j:]

    return merged_arr

# Функция  сортировки массива с помощью слияния
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left_half, right_half = split_array(arr)

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

#Функция  вывода отсортированного массива
def sort_array(arr):
    sorted_arr = merge_sort(arr)
    print("Отсортированный массив (Merge Sort):", sorted_arr)

#массив
arr = [64, 34, 25, 12, 22, 11, 90]

#Сортировка массива и вывод отсортированного массива
sort_array(arr)