number = int(input('Введіть ціле число: '))
number_len = len(str(abs(number)))

if number>0:
    print("Число додатнє")
    if number%2==0:
        print("Ваше число парне!")
    elif number%2!=0:
        print("Ваше число непарне")
elif number<0:
    print("Число відʼємне!")
    if number%2==0:
        print("Ваше число парне!")
    elif number%2!=0:
        print("Ваше число непарне")
elif number==0:
    print("Ваше число дорівнює нулю")
else:
    print("Некоректне число.")

if number_len==1:
    print("Ваше число одноцифрове")
elif number_len==2:
    print("Ваше число двоцифрове")
elif number_len==3:
    print("Ваше число трицифрове")
else:
    print("Або воно дуже велике")


