from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y,  friend, is_friend')

+ friend('Алексей', 'Игорь')
+ friend('Игорь', 'Светлана')
+ friend('Светлана', 'Алексей')

is_friend(X, Y) <= friend(X, Y)
is_friend(X, Y) <= friend(Y, X)

# Запрос: кто является другом для Игоря?
print(is_friend('Игорь', X))