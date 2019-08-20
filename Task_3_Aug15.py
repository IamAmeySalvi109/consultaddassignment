print("Dictionary")

cars = {'1' : {'Brand' : 'Ferrari', 'Model' : '458 Spider', 'Year' : '2015'}, '2' : {'Brand' : 'Chevrolet', 'Model' : 'Impala', 'Year' : '1967'}}

print ("Initial Dictionary:")
print(cars)

cars.popitem()
print ("After Popping:")
print(cars)

print()

print("List")

List = [1,2,3,4,5,6,7,8,9] 
print("Intial List: ") 
print(List) 
  
Sliced_List = List[4:7] 
print("Sliced elements: ") 
print(Sliced_List) 

for i in range(2, 6): 
    List.remove(i) 
print("After Removing: ") 
print(List) 