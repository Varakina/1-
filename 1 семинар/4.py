# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

print("введите номер четверти: ")
chetvert =  int (input())


if chetvert == 1:
    print("(x > 0)  (y > 0)")
elif chetvert == 2:
    print("((x < 0) and (y > 0))")
        
elif chetvert == 3:
    print("((x < 0) and (y <= 0))")
        
elif chetvert == 4:
    print("((x > 0) and (y < 0))")
       
    

