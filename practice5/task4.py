def read_grade(prompt):
    while True:
        grade = input(prompt)

        if grade.isdigit():
            grade = int(grade)

            if 0 <= grade <= 100:
                return grade

        print("Введіть ціле число від 0 до 100.")


def to_letter(grade):
    if grade >= 90:
        return "A"
    if grade >= 82:
        return "B"
    if grade >= 74:
        return "C"
    if grade >= 64:
        return "D"
    if grade >= 60:
        return "E"
    return "F"


def average(grades):
    return sum(grades) / len(grades)


def count_above(grades, limit):
    count = 0

    for grade in grades:
        if grade > limit:
            count += 1

    return count


def print_report(name, group, grades):
    avg = average(grades)

    print("\n--- Звіт про оцінки ---")
    print("Ім'я:", name)
    print("Група:", group)
    print("Оцінки:", grades)
    print(f"Середнє: {avg:.2f}")
    print("Буквена оцінка:", to_letter(avg))
    print("Найкращий бал:", max(grades))
    print("Найгірший бал:", min(grades))
    print("Оцінок вище середнього:", count_above(grades, avg))


def main():
    name = "Andriy"
    group = "IT-31"

    n = len(name)

    if n < 3:
        n = 3

    grades = []

    for i in range(n):
        grade = read_grade(f"Введіть оцінку {i + 1}: ")
        grades.append(grade)

    print_report(name, group, grades)


main()