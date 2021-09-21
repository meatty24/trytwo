print("Приветик, напиши своё имя")
name = input()
#insert your name
print("\tNice to meet you,", name)
h = float(input("Введи рост М"))
m = float(input("Введи вес КГ"))
bmi = m/h**2
print("Ваш ИМТ", bmi)
age = int(input("Сколько вам полных лет?"))
if age>30:
    if bmi<20.0: print("ты дрищ")
    elif bmi>20.1: print("норм")
    elif bmi>26.0: print("жир")
else:
    if bmi < 19.0: print("ты дрищ")
    elif bmi > 19.1: print("норм")
    elif bmi > 23.0: print("жир")
