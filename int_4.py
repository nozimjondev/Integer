a = int(input('Enter A: '))
b = int(input('Enter B: '))

while a < b:
	print(b)
	b = int(input("B can not be larger than A, Enter B: "))
	pass

result = a // b
print(result)
	