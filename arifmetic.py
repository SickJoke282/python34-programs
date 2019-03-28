def arithmetic(num1, num2, operation): 
	if operation == '+':
		print(num1 + num2)
	elif operation == '-':
		print(num1 - num2)
	elif operation == '*':
		print(num1 * num2)
	elif operation == '/':
		print(num1 / num2)
	else:
		print('Неизвестная строка')

Num1 = int(input('Введите первую цыфру: '))
Num2 = int(input('Введите вторую цыфру: '))
x = input('Введите действие: ')
arithmetic(Num1, Num2, x)
