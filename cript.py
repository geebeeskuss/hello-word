text = input("Введите строку")

text = text[::-1]
print(text)
text = text[len(text)//2:] + text[len(text)//2]
text = text.replace("а","б").replace("в","г")
print(text)
