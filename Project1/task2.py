list = [5, 2, 8, 1, 9, 3]
sortedList = sorted(list)
print(sortedList)

list1 = [5, 2, 8, 1, 9, 3]
sortedList1 = []
for i in range(len(list1)):
    min_num = min(list1)
    sortedList1.append(min_num)
    list1.remove(min_num)
print(sortedList1)

list3 = [5, 2, 8, 1, 9, 3]
sorted_numbers = []
for i in range(len(list3)):
    smallest_num = list3[0]
    for n in list3 :
        if n < smallest_num:
            smallest_num = n
    sorted_numbers.append(smallest_num)
    list3.remove(smallest_num)
print(sorted_numbers)