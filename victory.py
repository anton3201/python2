questions = {"Мэл Гибсон": 1956,
            "Джулия Ормонд": 1965,
            "Андриано Чилинтано": 1938,
            "Николас Кейдж": 1964,
            "Элвис Пресли": 1935}

correctanswercount:int = 0

for question in questions :
    answer = int(input(f"Введи год рождения актера {question}:"))
    if answer == questions.get(question):
        correctanswercount = correctanswercount + 1


print(f"Правильных ответов:{correctanswercount}\n",
      f"% правильных ответов: {correctanswercount/5*100}")
