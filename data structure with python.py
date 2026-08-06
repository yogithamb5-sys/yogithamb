fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)
print("First element:", fruits[0])
print("Last element:", fruits[-1])
fruits.append("orange") 
fruits.insert(1, "blueberry") 
print("After adding elements:", fruits)
fruits.remove("banana")
popped_item = fruits.pop()  
print("After removals:", fruits) 
print("Popped item:", popped_item) 
l1 = [10,15,20,25,30,]
l1.reverse()
print("Reversed list:", l1)
l2 = [40, 10, 30, 20]
l2.sort()
print("Sorted list:", l2)
l3=l1+l2 
print(l3)

