from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, can_marry')

+ can_marry('Иван', 'Мария')
+ can_marry('Анна', 'Петр')
+ can_marry('Анна', 'Сергей')
+ can_marry('Анна', 'Петр')
+ can_marry('Юля', 'Петр')

# Правило: X может жениться на Y, если Y может выйти замуж за X
can_marry(X, Y) <= can_marry(Y, X)

# Запрос: с кем может жениться Петр?
print(can_marry('Иван', X))