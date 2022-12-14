#Напишите программу, которая найдёт произведение пар чисел
# списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д
import random
import math
from typing import List

def create_list(numbers:List[int])-> list:
    for i in range(int(input("Введеите количество элементов: "))):
        numbers.append(random.randint(1,9))
    return numbers

def pairs(numbers: list )-> list:
    product_list=[]
    for i in range(math.ceil(len(numbers)/2)):
        product_list.append(numbers[i]*numbers[-(i+1)])
    return product_list

numbers = []
print(F"список  {create_list(numbers)}")
print(F"произведение  {pairs(numbers)}")
