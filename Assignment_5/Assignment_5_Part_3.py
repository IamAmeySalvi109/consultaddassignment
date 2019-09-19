def swapalt(s, k, Len): 
    i = 0
      
    while(i < len(s)): 
  
        if (i + k > Len): 
            break
  

        ss = s[i:i + k] 
        s = s[:i]+ss[::-1]+s[i + k:] 
          

        i += 2 * k 
      
    return s; 
  
  
s = input("Enter string: ")
print("String: ", s)


Len = len(s) 

c = input("Enter k: ")
k = int(c)
print(swapalt(s, k, Len)) 