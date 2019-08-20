import re
from collections import Counter
x = "Hello&*$$world"

print("My string: ",x)  

#y = {} 

#for i in x: 
#	if i in y: 
#		y[i] += 1
#	else: 
#		y[i] = 1

#print (y)

#for key,value in y.items():
#	if ((key>='a' and key<='z')or(key>='A'and key<='Z')or(key>='0'and #key<='9')):
#		del y[key,value]
#print(y)

z = re.findall('[^A-Za-z0-9]',x)
y = Counter(z)
print(y)