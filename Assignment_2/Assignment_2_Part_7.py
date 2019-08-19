x=[10,"Python",4.0,25]
y=[3, 20, 12, 1878]

print ("Given List: ",x)

if all(type(num)==int for num in x):
	print("True")
else:
	print("False")

print()

print ("Given List: ",y)

if all(type(num)==int for num in y):
	print("True")
else:
	print("False")