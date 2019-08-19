x = range(1,21)
even = []
odd = []

for n in x:
	if n%2==0:
		even.append(n)
	else:
		odd.append(n)

print("The pair of numbers whose sum is equal to even number are:")
for i in even:
	for j in even:
		print(("({},{})".format(i, j)), end=", ") 
for i in odd:
	for j in odd:
		print(("({},{})".format(i, j)), end=",")