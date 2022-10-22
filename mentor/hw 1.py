ten = list(range(1, 11))
evens = list(filter(lambda i: i % 2 == 0, ten))
evens1 = list(map(lambda i: i ** 2, evens))

print(evens1)
def function(lst=(list(ten))):
    while True:
        index = input("Введите индекс для вывода объекта из списка:")
        if index.lower() == 'exit' or index.lower() == 'Выход':
            break
        try:
                print(lst[int(index)])
        except:
                print('Неверный индекс или данного индекса не существует')
function()