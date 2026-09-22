d = 6
c = 6
suma = 0
dobutok = 1
kilkist=0

print("Всі числа: ", end="")
for i in range(d, 32):
    print(i, end=" ")
    suma+=i
    dobutok *= i
    kilkist += 1
serednye = suma/kilkist
print("\n скільки чисел вивелося: ",kilkist)
print("сума цих чисел: ", suma)
print("Добуток всіх чисел: ",dobutok)
print(f"Середнє арифметичне: {serednye:.2f}")

even_count = 0
odd_count = 0
for b in range(d, 32):
    if b%2 ==0:
        even_count += 1
    if b%2 ==1:
        odd_count += 1
print("З них стільки парних чисел: ",even_count)
print("З них стільки непарних чисел: ",odd_count)

even_count2 = 0
odd_count2 = 0
while d<32:
    if d%2 ==0:
        even_count2+=1
    if d%2 !=0:
        odd_count2+=1
    d+=1
print("Парних чисел(через while): ",even_count2)
print("Непарних чисел(через while): ",odd_count2)

for e in range(c,0,-1):
    print(e,end=" ")