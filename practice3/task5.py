day = int(input("Введіть день: "))
month = int(input("Введіть місяць(1-12): "))
year = int(input("Введіть рік: "))

if month>=1 and month<=12:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day>0 and day<=31:
            if year>=0:
                print("Day:", day, "; Month:", month, "; Year:", year)
            else:
                print("Рік введено не правильно! Рік має бути додатнім.")
        else:
            print("День введено не правильно, бо січень, березень, травень, липень, серпень, жовтень, грудень мають лише 31день.")
    elif month in [4, 6, 9, 11]:
        if day > 0 and day <= 30:
            if year >= 0:
                print("Day:", day, "; Month:", month, "; Year:", year)
            else:
                print("Рік введено не правильно! Рік має бути додатнім.")
        else:
            print("День введено не правильно, бо квітень, червень, вересень та листопад мають лише 30днів.")
    elif month==2:
        if year%4==0:
            if day > 0 and day <= 29:
                if year >= 0:
                    print("Day:", day, "; Month:", month, "; Year:", year)
                else: print("Рік введено не правильно! Рік має бути додатнім.")
            else: print("День введено не правильно, бо лютий у високосний рік має лише 29днів.")
        if year % 4 != 0:
            if day > 0 and day <= 28:
                if year >= 0:
                    print("Day:", day, "; Month:", month, "; Year:", year)
                else: print("Рік введено не правильно! Рік має бути додатнім.")
            else: print("День введено не правильно, бо лютий у невисокосний рік має лише 28днів.")
else:
    print("There isn't this month")