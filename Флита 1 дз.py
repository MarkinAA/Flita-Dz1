n = int(input('Введите количество элементов множества 1 ? '))
print ("Вводите числа в двоичной системе счисления")
my_set_1 = set()
for i in range(n):
    my_set_1.add(input())

n = int(input('Введите количество элементов множества 2 ? '))
print ("Вводите числа в двоичной системе счисления.")
my_set_2 = set()
for i in range(n):
    my_set_2.add(input())

my_list_1 = list(my_set_1)
my_list_2 = list(my_set_2)
#print (my_list)
print("Перевод элементов первого множества.")
for i in range (len(my_list_1)):
    try:
        result = int(my_list_1[i], 2)
        print("Удачно")
    except:
        print("Что-то пошло не так")
    result = int(my_list_1[i], 2)
    print(result, "==", my_list_1[i])

print("Перевод элементов второго множества.")
for i in range (len(my_list_2)):
    result = int(my_list_2[i], 2)
    print(result, "==", my_list_2[i])