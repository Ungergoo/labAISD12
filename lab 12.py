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

matrix_rank = np.random.randint(1, 11)  
matrix_x = np.random.uniform(-1, 1, (matrix_rank, matrix_rank))  
print('Матрица x:\n', matrix_x)

n = 1
calculated_matrix = matrix_x
curr_answer = Decimal(0)  
factorial_divisor = 1


while True:
    int_current_operator = n * 3 - 1

    #3n - 1
    calculated_matrix = np.multiply(calculated_matrix, matrix_x ** (3 * n - 1))

    factorial_divisor *= (int_current_operator - 1) * (int_current_operator - 2) if int_current_operator > 2 else 1

    if factorial_divisor == 0:  #делениe на ноль
        factorial_divisor = 1

    det_matrix = np.linalg.det(calculated_matrix)  
    curr_answer += -1 * (Decimal(abs(det_matrix))) / Decimal(factorial_divisor)

    n += 1 

    if len(str(curr_answer).split('.')[1]) >= precision:
        break

if flag == 1:
    curr_answer = curr_answer.quantize(Decimal(10) ** -precision)  #округление

print('Ответ: ', curr_answer)
