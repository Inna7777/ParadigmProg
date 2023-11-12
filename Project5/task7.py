from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, age, total_age')

+ age('Мария', 30)
+ age('Иван', 40)
+ age('Алексей', 20)

total_age[X] = sum(Y, (age[X, Y]))