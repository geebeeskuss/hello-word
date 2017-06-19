#print("Охота на велосипидиста-пончика началась")
name = 'Ибра "Игривый"'
#name2 = "Ибра \"Игривый\""
#print(name[0:4])
#print(name[5:14])
#print(name[5])
#print(name[4:15])
#print(name[6:]) #если ввести только начальную координату, то ввыведиться все до конца
#print(name[:8]) #если же только конечную,то начинает автоматом с 0
#print(name[-4:6])
#print(name[::5])
poem = """Привет мой друг,
Мой друг далёкий.
Пишу в надежде донести
Как много в мире нашем жизней...
И как прекрасна наша жизнь"""
print(poem)
print(poem.find("он"))
print(poem.rfind("в"))
print(poem.lower())
print(poem.upper())
print(poem.title())
print(poem.replace("Мой","в"))