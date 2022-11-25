#Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#Нужно написать таблицу истинности

print('x y z')
for x in range(2):
  for y in range(2):
    for z in range(2):
      if (not(x) and y and z) or (not(x) and not(y) and z) or (not(x) and not (y) and not(z))==1:
        print(x, y, z)