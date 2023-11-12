from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, parent, grandparent')

+ parent('Мария', 'Иван')
+ parent('Иван', 'Сергей')

# Определение отношения 'дедушка/бабушка'
grandparent(X, Y) <= parent(X, Z) & parent(Z, Y)

# Запрос: кто является дедушкой или бабушкой для Сергея?
print(grandparent(X, 'Сергей'))