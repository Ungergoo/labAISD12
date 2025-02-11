import numpy as np

def compute_series(X, t):
    """Вычисляет сумму знакопеременного ряда до достижения заданной точности t."""
    n = 1
    sum_series = 0
    prev_term = 0
    sign = 1  # Знак первого слагаемого

    while True:
        # Вычисляем (n-1)! (факториал)
        factorial = np.math.factorial(n - 1)
        
        # Возводим X в степень (n-1) поэлементно
        X_power = np.power(X, n - 1)
        
        # Вычисляем поэлементный модуль X^n-1
        term = np.sum(np.abs(X_power)) / factorial * sign
        
        # Если разница с предыдущим слагаемым меньше заданной точности, завершаем вычисления
        if abs(term - prev_term) < t:
            break
        
        sum_series += term
        prev_term = term
        n += 1
        sign *= -1  # Меняем знак

    return sum_series

# Генерация случайной матрицы X размером kxk (например, k = 3)
k = 3
X = np.random.random((k, k))  # Генерация случайной матрицы размером kxk

# Задание точности
t = 1e-6

# Вызов функции для вычисления суммы ряда
result = compute_series(X, t)
print(f"Результат суммы ряда: {result}")
