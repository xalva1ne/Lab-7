first_set = set(input('Введите первое множество чисел через пробел: ').split())
second_set = set(input('Введите второе множество чисел через пробел: ').split())

numbers = set('0123456789')
combined_set = first_set.union(second_set)


if numbers == combined_set:
    print(f'В записи этих двух строк используются все десять цифр')
else:
    print(f'В записи этих двух строк НЕ используются все десять цифр')

