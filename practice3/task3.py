first_number = int(input("Введіть перше число"))
second_number = int(input("Введіть друге число"))
operation = input("Введіть дію між числами +, -, *, /, //, %, ** ")

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    if second_number != 0:
        print(first_number / second_number)
    elif second_number == 0:
        print("На 0 ділити не можна")
elif operation == "//":
    if second_number != 0:
        print(first_number // second_number)
    elif second_number == 0:
        print("На 0 ділити не можна")
elif operation == "%":
    if second_number != 0:
        print(first_number % second_number)
    elif second_number == 0:
        print("На 0 ділити не можна")
elif operation == "**":
    print(first_number ** second_number)
else:
    print("Ви некоректно ввели дію між числами")