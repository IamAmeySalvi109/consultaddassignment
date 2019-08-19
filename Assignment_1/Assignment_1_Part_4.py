x = input("Enter a number: ")
print("Number entered: ",x)

if (int(x) % 2 == 0) and (int(x) % 5 == 0):
	print("Hurrah it is what I am looking for")
else:
	print("Wrong input")