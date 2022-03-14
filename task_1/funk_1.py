# Сформировать и заполнить массив случайным числами и вывести максимальное, минимальное и среднее значение. 
# Для генерации случайного числа использовать метод  Math.random() , который возвращает значение в промежутке [0, 1].

from statistics import mean
from random import randint

random_numbers = [randint(0, 1) for i in range(int(input('Количество чисел? - ')))]
print(f'максимальное: {max(random_numbers)}, минимальное: {min(random_numbers)}, среднее: {mean(random_numbers)}')