A = int(input("Enter А: "))

while A < 999:
	print(A)
	A = int(input("Enter А: "))

B = A % 1000
C = B // 100

print(C)