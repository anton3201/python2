
yearborn = int(input("Введи год рождения АС Пушкина:"))
correct_answer:int = 1799

if yearborn != correct_answer:
    print("Некорректный год!!!")
else:
    dayborn = input("Введи дату рождения в формате dd.mm:")
    if dayborn == "06.06":
        print("День рождения верный!")
    else:
        print("День рождения Не верный!")


