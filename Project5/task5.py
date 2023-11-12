from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, age, average_age, total_age, number_of_people')

+ age('Мария', 30)
+ age('Иван', 40)
+ age('Алексей', 20)

# Сумма возрастов
total_age[X] = sum_(Y, for_each=age[X, Y])

# Количество людей
number_of_people[X] = count_(Y, for_each=age[X, Y])

# Средний возраст
average_age[X] = (total_age[X] / number_of_people[X])

# Запрос: какой средний возраст людей?
print(average_age[X])