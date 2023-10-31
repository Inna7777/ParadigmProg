# императивный стиль
list = [7, 2, 4, 1, 9, 3]
sorted_numbers = []
for i in range(len(list)):
    bigest_num = list[0]
    for n in list :
        if n > bigest_num:
            bigest_num = n
    sorted_numbers.append(bigest_num)
    list.remove(bigest_num)
print(sorted_numbers);

 # декларативный
list2 = [5, 2, 8, 1, 9, 3]
sortedList = sorted(list2, reverse=True)
print(sortedList)