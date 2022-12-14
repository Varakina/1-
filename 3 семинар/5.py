#Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
def get_fibonachi (num):
    if num ==0:
        get_fibonachi = [0]
        return get_fibonachi
    get_fibonachi = [0,1]
    for i in range (0,num-1):
        fib_1=get_fibonachi[i]
        fib_2= get_fibonachi[i+1]
        fib =fib_1+fib_2
        get_fibonachi.append(fib)
    return get_fibonachi

def get_n_fibonachi(get_fibonachi):
    n_fibonachi=[]
    n = 0
    for i in get_fibonachi:
        negafib = ((-1)**(n+1))*i
        n_fibonachi.append(negafib)
        n+=1
    n_fibonachi.reverse()

fibonachi = get_fibonachi(int(input('введите число ')))
n_fibonachi = get_n_fibonachi(fibonachi)

print(n_fibonachi[:-1]+fibonachi)
