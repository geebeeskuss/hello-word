cities = ["Махачкала","Санта-Моника","Кельн","Майами"]
print(cities)
print(cities[1:])
cities.append("Абмер")
said_wishes = ["Мачу-Пикчу","Запретный город"]
cities.extend(said_wishes)
print(cities)
cities.insert(1,"Хасавюрт")
print(cities)
print(cities.pop(0))
print(cities)
del cities[0]
print(cities)
cities.remove("Кельн")
print(cities)
cities[4]="Одобренный город"
print(cities)
cities_str = "<3".join(cities)
print(cities_str)
cities.sort()
print(cities)
vegetable = ("Тыква","Кабачок","Баклажан")
print(vegetable[1])

