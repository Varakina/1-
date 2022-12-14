 #Задайте список из нескольких чисел. 
 # Напишите программу, которая найдёт сумму элементов списка,
 #  стоящих на нечётной позиции.
import random
from typing import List
def create_list(numbs = []):
    for i in range(int(input("Введеите количество элементов: "))):
        numbs.append(random.randint(1,9))
    return numbs



def get_sum(numbers:List[int])-> int:
    summa = 0
    for n in range(1,len(numbers),2):
        summa += n
    return summa

numbers = create_list()
print(numbers)
print(f'сумма элементов на нечетных позициях = {get_sum(numbers)}')