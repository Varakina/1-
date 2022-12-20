#Напишите программу, удаляющую из текста все слова, содержащие заданную строку.


txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = input("введите заданную строку:\n")
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')