d = int(input('Enter a two-digit number: '))

while d< 10 or d > 99:
	print(a)
	d = int(input("The number can not be one-digit: "))
a,b = divmod(d,10)
print(f'Sum of the numbers: {a + b}')
print(f'Product of the numbers: {a * b}')