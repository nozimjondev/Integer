A = int(input("Enter А: "))

while A < 999:
	print(A)
	A = int(input("Enter А: "))

B = A % 10000
C = B // 1000

print(C)