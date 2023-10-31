a = int(input('Enter a two-digit number: '))

while a < 10 or a > 99:
	print(a)
	a = int(input("The number can not be one-digit: "))
c = a % 10
d = a // 10

print(f'{c}{d}')
