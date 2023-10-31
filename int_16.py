d = int(input('Enter a three-digit number: '))

while d< 100 or d > 999:
	print(d)
	d = int(input("The number can not be one or two digit: "))
fivescore,decimal = divmod(d,100)
decimal,unit = divmod(decimal,10)
print(d)
print(f'{fivescore}{unit}{decimal}')