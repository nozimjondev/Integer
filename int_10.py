d = int(input('Enter a three-digit number: '))

while d< 100 or d > 999:
	print(d)
	d = int(input("The number can not be one or two digit: "))
a,b = divmod(d,100)
a,b = divmod(b,10)
print(b)

print(a)

