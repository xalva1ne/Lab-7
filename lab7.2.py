number_tuple = (26,-31,51,-76,-94,11,-4,2)

number_list = []

for num in number_tuple:
    if num < 0:
        number_list.append(num)

print(f'Кортеж: {number_tuple}\nСписок основанный на кортеже: {number_list}')

