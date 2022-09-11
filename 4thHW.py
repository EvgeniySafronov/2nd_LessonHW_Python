""" Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных пользователем через пробел позициях. """

n = int(input('Введите число N: '))
prod = 1
my_list = list(range(-n, n+1))
print(my_list)

pr_num = input('Введите числа через пробел ')
print(pr_num.split())
pr_num: int
for i in pr_num:
    prod *= my_list[i]
   
print(prod)