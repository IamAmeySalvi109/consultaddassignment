#Reverse Function

def rev(str, k, Len): 
	i = 0
	while(i < len(str)):
		if (i + k > Len):
			break
		ss = str[i:i + k]
		str = str[:i]+ss[::-1]+str[i + k:]
		i += 2 * k
	return str;

#Main Function

str = "abcdefg"
Len = len(str)
k = int(input("Enter a number: "))
#k = 2
print(rev(str, k, Len))