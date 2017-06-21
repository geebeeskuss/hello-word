inpur random
player1 = {"счёт":0,"ставка":0,"сумма":1000}
player2 = {"счёт":0,"ставка":0,"сумма":1000}
player1["имя"] = input("Введите своё имя: ")
player2["имя"] = input("Введите своё имя: ")

player1["ставка"] = input("Введите ставку: ")
if player1["ставка"] > player1["сумма"]:
	player1["ставка"] = player1["сумма"]

player2["ставка"] = input("Введите ставку: ")
if player2["ставка"] > player2["сумма"]:
	player2["ставка"] = player2["сумма"]

player1["бросок"] = random.randit(2,12)
player1["бросок"] = random.randit(2,12)
if player1["бросок"] > player2["бросок"]:
	print(player2["имя"],"выйграл ставку")
	player2["сумма"] += player1["сумма"]
	player1["сумма"] -= player2["сумма"] 
elif player2["бросок"] > player1["сумма"]:
	print(player1["имя"],"выйграл ставку")
	player1["сумма"] += player2["сумма"]
	player2["сумма"] -= player1["сумма"]