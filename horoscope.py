class DayError(Exception):
    pass

class MonthError(Exception):
    pass

while True:
    try:
        date  = input("Введите дату рождения в ввиде ДД.ММ.ГГГГ: ")
        day = int(date[0:2])
        # print(day)
        month = int(date[3:5])
        # print(month)
        year = int(date[6:])
        # print(year)
        if day <= 0 or day > 31:
            raise DayError 
        if month in range(1,32):
            raise MonthError

        if (day >21 and month == 6) or (day < 21 and month == 7):
            print("Ты Рак")
        break
        if (day >21 and month == 3) or (day <19 and month == 4):
            print("Ты Овен")
        break
        if (day >19 and month == 4) or (day <21 and month == 5):
            print("Ты Телец")
        break
        if (day >21 and month == 5) or (day <21 and month == 6):
            print("Ты Близнецы")
        break
        if (day >23 and month == 7) or (day <23 and month == 8):
            print("Ты Лев")
        break
        if (day >23 and month == 8) or (day <23 and month == 9):
            print("Ты Дева")
        break
        if (day >23 and month == 9) or (day <23 and month == 10):
            print("Ты Весы")
        break
        if (day >23 and month == 10) or (day <22 and month == 11):
            print("Ты Скорпион")
        break
        if (day >22 and month == 11) or (day <22 and month == 12):
            print("Ты Стрелец")
        break
        if (day >22 and month == 12) or (day <20 and month == 1):
            print("Ты Козерок")
        break
        if (day >20 and month == 1) or (day <19 and month == 2):
            print("Ты Водолей")
        break
        if (day >19 and month == 2) or (day <21 and month == 3):
            print("Ты Рыбы")
        break
    except ValueError:
        print("Введите дату в правильном формате")
    except DayError:
        print("Введите правильный день")
    except MonthError:
        print("Введите правильный месяц")