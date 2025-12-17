# Python_Practice
Python Files 

# List with repeated names
name_list = ["Harshada", "Garima", "Ram", "Nimisha", "Ram", "Harshada", "Kiran", "Amit", "Garima", "Sahil"] 

# Tuple with repeated names
name_tuple = ("Ram", "Divya", "Nimisha", "Ram", "Kiran", "Amit", "Rahul", "Divya", "Sahil", "Kiran")

print("List:", name_list)    
print("Tuple:", name_tuple)

## Convert list and tuple to sets to remove duplicates
list_set = set(name_list)
tuple_set = set(name_tuple)

print("Set from list:", list_set)
print("Set from tuple:", tuple_set)


list_set.remove("Amit")
print("After removing Amit:", list_set)
list_set.add("Harshada")
print("After adding Harshada:", list_set)
tuple_set.remove("Ram")
print("After removing Ram:", tuple_set)
tuple_set.add("Ashvitha") 
print("After adding Ashvitha:", tuple_set) 

print("Final Set from list:", list_set)

print("Final Set from tuple:", tuple_set)  



# Union of both sets
union_names = list_set.union(tuple_set)
print("Union of both sets:", union_names)

# Intersection of both sets
common_names = list_set.intersection(tuple_set)
print("Intersection of both sets:", common_names)


frozen_names = frozenset(list_set)
print("Frozen Set:", frozen_names) 


Output:--
List: ['Harshada', 'Garima', 'Ram', 'Nimisha', 'Ram', 'Harshada', 'Kiran', 'Amit', 'Garima', 'Sahil']

Tuple: ('Ram', 'Divya', 'Nimisha', 'Ram', 'Kiran', 'Amit', 'Rahul', 'Divya', 'Sahil', 'Kiran')

Set from list: {'Ram', 'Nimisha', 'Kiran', 'Amit', 'Harshada', 'Sahil', 'Garima'}

Set from tuple: {'Ram', 'Nimisha', 'Sahil', 'Kiran', 'Amit', 'Divya', 'Rahul'} 

After removing Amit: {'Ram', 'Nimisha', 'Kiran', 'Harshada', 'Sahil', 'Garima'} 

After adding Harshada: {'Ram', 'Nimisha', 'Kiran', 'Harshada', 'Sahil', 'Garima'}

After removing Ram: {'Nimisha', 'Sahil', 'Kiran', 'Amit', 'Divya', 'Rahul'}

After adding Ashvitha: {'Nimisha', 'Sahil', 'Kiran', 'Amit', 'Divya', 'Rahul', 'Ashvitha'}

Final Set from list: {'Ram', 'Nimisha', 'Kiran', 'Harshada', 'Sahil', 'Garima'}

Final Set from tuple: {'Nimisha', 'Sahil', 'Kiran', 'Amit', 'Divya', 'Rahul', 'Ashvitha'}

Union of both sets: {'Ram', 'Nimisha', 'Kiran', 'Rahul', 'Amit', 'Divya', 'Harshada', 'Sahil', 'Garima', 'Ashvitha'}

Intersection of both sets: {'Kiran', 'Sahil', 'Nimisha'}

Frozen Set: frozenset({'Ram', 'Nimisha', 'Kiran', 'Sahil', 'Garima', 'Harshada'})


