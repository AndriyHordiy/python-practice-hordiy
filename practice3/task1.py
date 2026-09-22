username = input("Введіть ваше імʼя:")
age = int(input("Введіть ваш вік: "))

if username:
    print("Ваше імʼя:", username)
else:
    print("Оскільки ви не ввели імʼя, то за замовчуванням буде Anonymous")
    username = "Anonymous"

if age < 0:
    print("На жаль, Ви не правильно ввели ваш вік")
elif 0<=age<=6:
    print("Вітаємо! Ви дитина!")
elif 7<=age<=17:
    print("Вітаємо! Ви школяр!")
elif 18<=age<=64:
    print("Вітаємо! Ви дорослий!")
elif age>64:
    print("Вітаємо! Ви сеньйор!")