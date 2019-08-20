A = {'a', 'c'}
B = {'c', 'd', 2, 'e' }
C= {1, 2, 3,4}

print("Union")
print("A U B =", A.union(B))
print("B U C =", B.union(C))
print("A U B U C =", A.union(B, C))

print()

print("Intersection")
print("A intersection B =", A.intersection(B))
print("B intersection C =", B.intersection(C))
print("A intersection B intersection C =", A.intersection(B,C))

print()

print("Zip")
name = ["Roger Federer", "Rafael Nadal", "Novak Djokovic", "Andy Murray"]
nationality = ["Switzerland", "Spain", "Serbia", "Scotland"]
slams = [20, 18, 16, 3]
ranking = [3,2,1,329]

mapped = zip(name, nationality, slams, ranking) 
mapped = set(mapped) 

print ("The zipped result is : ") 
print (mapped) 

print()
print("Enumerate")
x = ["England","India","New Zealand","Australia","South Africa","Pakistan","Bangladesh","Sri Lanka","West Indies","Afghanistan"] 

y = list(enumerate(x, 1))
print (y)