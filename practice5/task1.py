def print_card():
    print("Name: Andriy Hordiy")
    print("Group: IT-31")
    print("Birth Year: 2009")
print_card()
print_card()
print_card()

def print_card_args(name, surname, group, year):
    print(name, surname, group, year)
print_card_args("Andriy", "Hordiy", "IT-31", "2009")
print_card_args(surname="Hordiy", name="Andriy", year="2009", group="IT-31")
print_card_args("Andriy", "Hordiy",  year="2009", group="IT-31")

def print_card_args2(name, surname,  year, group="IT-31"):
    print(name, surname, group, year, "Виведено з групою за замовчуванням!")
print_card_args2("Andriy", "Hordiy", "2009")

# print_card_args("Ivan")
# print_card_args(name="Ivan", "Petrenko")