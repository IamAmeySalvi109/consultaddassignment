start = 1
end = 50

for x in range(start, end + 1):
	if (int (x) % 2 != 0) and ((int (x)*int (x)*int (x)) < 50):
		print (int(x))

