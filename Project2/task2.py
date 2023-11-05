# Структурный подход

# N = 10
# sum = 0
# for i in range(1, N + 1):
#     sum += i
# print('Сумма чисел от 1 до ' + str(N) +' = ' + str(sum))


# Процедурный подход
def get_sum(N):
    sum = 0
    for i in range(1, N + 1):
        sum += i
    return sum

N = 10
print('Сумма чисел от 1 до ' + str(N) +' = ' + str(get_sum(N)))