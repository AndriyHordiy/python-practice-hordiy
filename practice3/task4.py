bal = int(input("Введіть ваш бал: "))
exday = int(input("Введіть скільки занять ви пропустили: "))

if bal < 0 or bal > 100:
    print("Помилка. Бал введено не правильно.")
else:
    if 90<=bal:
        print("Оцінка: А. ECTS: Відмінно.")
    elif 82<=bal:
        print("Оцінка: B. ECTS: Добре.")
    elif 74<=bal:
        print("Оцінка: C. ECTS: Добре.")
    elif 64<=bal:
        print("Оцінка: D. ECTS: Задовільно.")
    elif 60<=bal:
        print("Оцінка: E. ECTS: Задовільно.")
    elif 0<=bal:
        print("Оцінка: F. ECTS: Незадовільно.")
    if exday > 16*0.3:
        print("Попередження. Недопуск незалежно від балу.")
    else:
        print("Залік складено!")

