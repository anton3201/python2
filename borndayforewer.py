yearborn = int(input("Введи год рождения АС Пушкина:"))
correct_answer:int = 1799

while yearborn != correct_answer:
    yearborn = int(input("Попробуй еще раз:"))

dayborn = input("Введи дату рождения в формате dd.mm:")
while dayborn != "06.06":
    dayborn = input("Попробуй еще раз! Введи дату рождения в формате dd.mm:")

print("Верно!!!")

