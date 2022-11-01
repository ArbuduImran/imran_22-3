attempts = []
counter = 0
left = 1
right = 100
while True:
    middle = int((left + right) / 2)
    answer = input(f'ваше число {middle}? ')
    answer = answer.lower()
    attempts.append(middle)
    counter += 1
    if answer == 'да':
        left = middle
        right = middle
        break
    elif answer == 'больше':
        left = middle + 1
    elif answer == 'меньше':
        right = middle - 1
    else:
        print('Неправильная комманда')

with open('result.txt', 'w') as file:
    file.write(f'{counter}, {attempts}, {left}')