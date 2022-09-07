""" Задайте список из k чисел последовательности(1 + 1\k) ^ k и выведите на экран их сумму."""


k = int(input('Введите число k: '))


def k_mass(k):
    return [round((1 + 1 / x)**x, 2) for x in range(1, k + 1)]


print(k_mass(k))
print(round(sum(k_mass(k)), 2))
