y = 2009
def print_age(year):
    print("Ваш вік:", 2026 - year)
def get_age(year, current_year=2026):
    if year > current_year or year < 0:
        return -1

    return current_year - year
    print("after return")

print_age(y)
print(get_age(y))
print(print_age(y))

age = get_age(y)
print("Вік в місяцях:", age *12)
print("Вік в тижнях:", age *52)
age_2030 = get_age(y, 2030)
print("У 2030 році мені буде:", age_2030)
# print_age(y) * 12