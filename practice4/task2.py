a = int(input("Введіть ціле число(наприклад ddmmyy: "))
i=0
count_a = 0
suma=0
reverse = 0
largest = 0
smallest = 9
if a>0:
    while a > 0:
        last_digit = a % 10
        if last_digit > largest:
            largest = last_digit
        if last_digit < smallest:
            smallest = last_digit
        reverse = reverse * 10 + last_digit
        suma += last_digit
        a = a // 10
        count_a += 1
    print("Кількість цифр у числі:", count_a)
    print("Сума цифр в числі: ",suma)
    print("Ваше число задом на перед: ",reverse)
    print("Найбільша цифра у числі: ",largest)
    print("Найменша цифра у числі: ",smallest)
else:
    print("Введіть число більще за нуль!")