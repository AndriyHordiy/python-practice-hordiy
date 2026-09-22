name = "Andriy"
surname = "Hordiy"

def get_initials(name: str, surname: str) -> str:
    return name[0] + "." + surname[0] + "."

def count_letters(text: str, letter: str = "a") -> int:
    count = 0
    for char in text:
        if char == letter:
            count += 1
    return count
def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    count = 0

    for char in text:
        if char in vowels:
            count += 1
    return count

def reverse_text(text: str) -> str:
    result = ""
    for char in text:
        result = char + result
    return result

print("Повне ім'я:", name, surname)
print("Ініціали:", get_initials(name, surname))

c = len(surname)
vowels = count_vowels(surname)
consonants = c - vowels

print("Довжина прізвища:", c)
print("Голосних:", vowels)
print("Приголосних:", consonants)
for vowel in "aeiou":
    print(vowel, ":", count_letters(surname, letter=vowel))


print("count_letters(surname):", count_letters(surname))

print("Перевернуте прізвище:", reverse_text(surname))


print(count_letters.__doc__)
print(count_letters.__annotations__)