a = int(input("Какую хотите положить сумму в банк "))
years = int(input("На сколько вы хотите оставить деньги "))
def bank(a, years):
	new_a = (a * 110) / 100
	print("Через", years, "лет у вас будет", new_a * years, "рублей под 10% годовых")
bank(a, years)