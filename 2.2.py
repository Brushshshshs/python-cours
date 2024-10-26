print('Нужно ввсести 3 целых числа')
First = input('Введите 1е число ')
Second = input('Введите 2е число ')
Third = input('Введите 3е число ')
if First == Second == Third :
    print(3)

elif First == Second or Second == Third :
    print(2)

else :
    print(0)