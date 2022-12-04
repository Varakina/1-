#Дан массив размера N. После каждого отрицательного 
# элемента массива вставьте элемент с нулевым значением.
import random  
massive=[]
n=int(input("количество элементов в массиве:  "))
for k in range(1,n+1):
    massive.append(random.randint(-10,10))
print(massive)

def transform(massive:list)->list:
    result = []
    for element in massive:
        result.append(element)
        if element < 0:
            result.append(0)
    return result
print(transform(massive))
