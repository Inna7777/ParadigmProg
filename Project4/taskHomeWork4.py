# Расчет коэффициента корреляции Пирсона производится следующем образом:
# Вычислим суммы анализируемых значений X и Y:
# Σ(X) = x1+x2+x3+x4
# Σ(Y) = y1+y2+y3+y4
# Найдем средние арифметические для X и Y:
# Mx = Σ(X) / n
# My = Σ(Y) / n
# Рассчитаем для каждого значения сопоставляемых показателей величину отклонения от среднего арифметического
# dx = X - Mx и dy = Y - My:
# Рассчитаем для каждой пары анализируемых значений произведение отклонений dx x dy
# Определим значения суммы квадратов отклонений Σ(dx2) и Σ(dy2):
# Σ(dx2)
# Σ(dy2)
# Найдем значение суммы произведений отклонений Σ(dx x dy):
# Σ(dx x dy)
# функциональная парадигма для расчета

import math

# вычисление среднеарифметического
def aritfmeticMean(array):
    return sum(array) / len(array)

# сумма квадратов отклонений
def deviationArifmeticMean(array, mean):
    squaredSum = sum([(x - mean)**2 for x in array])
    return math.sqrt(squaredSum / len(array))

# сумма произведений отклонений
def sumDeviations(array1, array2, mean1, mean2):
    covariance = sum([(x1 - mean1) * (x2 - mean2) for x1, x2 in zip(arrayX, arrayY)])
    return covariance / len(arrayX)

def arifmeticMeanArray(arrayX, arrayY):
#вычисление среднеарифметического каждого массива
    mean1 = aritfmeticMean(arrayX)
    mean2 = aritfmeticMean(arrayY)
# вычисление квадрата отклонения каждого массива
    squareDev1 = deviationArifmeticMean(arrayX, mean1)
    squareDev2 = deviationArifmeticMean(arrayY, mean2)

    covariance = sumDeviations(arrayX, arrayY, mean1, mean2)
# Вычисление корреляция
    correlation = covariance / (squareDev1 * squareDev2)
    return correlation

# Массивы для вычислений
arrayX = [1, 2, 3, 4, 5]
arrayY = [6, 5, 4, 3, 2]

correlation = arifmeticMeanArray(arrayX, arrayY)
print("Корреляция Пирсона:", correlation)
