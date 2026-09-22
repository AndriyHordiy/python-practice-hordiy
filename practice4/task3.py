name = "Andriy"
surname = ("Hordiy")
vowels = 0
consonants = 0
total_char = 0
for char in name + surname:
    if char in "AEIOUYaeiouy":
        vowels+=1
    else:
        consonants+=1
    total_char +=1
print("Голосних: ", vowels)
print("Приголосних: ", consonants)
print("Букв всього: ", total_char)