d = 6
c = 6
n = d*c
suma = 0
divisors_count = 0
print("Дільники: ",end=" ")
for Divisors in range(1, n+1):
    if n % Divisors == 0:
        suma += Divisors
        print(Divisors,end=" ")
        divisors_count += 1
print("\nВсього дільників: ", divisors_count)
print("Сума дільників: ", suma)

for Divisors2 in range(2, n):
    if n % Divisors2 == 0:
        print("Число не є простим, бо воно ділиться на ", Divisors2)
        break
else:
    print("Число просте")

simple_count = 0
print("Прості числа від 2 до",n,"-", end=" ")
for simple in range(2, n+1):
    for simples_divisor in range(2, simple):
        if simple % simples_divisor == 0:
            break
    else:
        print(simple, end=" ")
        simple_count += 1
print("\nВсього простих чисел від 2 до", n, "-", simple_count)