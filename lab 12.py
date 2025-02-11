import math
import random
import numpy as np
from decimal import Decimal, getcontext


flag = 0
precision = input('Введите число t > 0: ')

while True:
    try:
        precision = int(precision)
    except ValueError:
        print('Ошибка: введено не число. Повторите ввод.')
        precision = None
    finally:
        if precision is None:
            pass
        elif float(precision) < 0:
            print('Ошибка: число меньше нуля. Повторите ввод.')
        elif int(precision) == 0:
            flag = 1
            break
        else:
            getcontext().prec = precision
            break
    precision = input('Введите число t > 0:')


matrix_rank = random.randint(1, 10)  
matrix_x = np.random.uniform(-1, 1, (matrix_rank, matrix_rank)) 
print('Матрица x:\n' + str(matrix_x))


n = 1  
calculated_matrix = matrix_x
factorial_divisor = 1
curr_answer = Decimal(0)


while True:
    int_current_operator = n - 1

    calculated_matrix = np.multiply(calculated_matrix, matrix_x)  

    factorial_divisor = math.factorial(int_current_operator) if int_current_operator > 0 else 1

    curr_answer += Decimal(np.linalg.det(calculated_matrix)) / Decimal(factorial_divisor)

    if len(str(curr_answer).split('.')[1]) >= precision:
        break

    n += 1  

if flag == 1:
    curr_answer = math.ceil(float(curr_answer))

print('Ответ: ' + str(curr_answer))
