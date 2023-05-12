car = []

c = input("Введите марку вашей машины (закончить ввод - end):")
while c != 'end':
    if c in car:
        print("Вы уже вводили данный автомобиль")
    else:
        car.append(c)
    c = input("Введите марку вашей машины (закончить ввод - end):")

print(car)
input()