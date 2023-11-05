# Структурное программирование
def find_lis(arr):
    n = len(arr) # 9
    lis = [1] * n # list[1, 1, 1, 1, 1, 1, 1, 1, 1]

    for i in range(1, n):
        lis_iteration(arr, lis, i)

    max_lis = max(lis)
    return max_lis

def lis_iteration(arr, lis, i):
    for j in range(0, i):
        if arr[i] > arr[j] and lis[i] < lis[j] + 1:
            lis[i] = lis[j] + 1  # list[1, 2, 1, 3, 2, 1, 1, 1, 1]

sequence = [10, 22, 9, 33, 21, 50, 41, 60, 80]
result = find_lis(sequence)
print("Наибольшая возрастающая подпоследовательность:", result) # 10 22 33 50 60 80