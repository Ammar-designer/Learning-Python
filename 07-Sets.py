#Sets in Python
phoneCompanies = {"Apple", "Samsung", "OnePlus", "Google", "Nokia"}
print("Phone Companies Set:", phoneCompanies)
print("Length of Phone Companies Set:", len(phoneCompanies))

#Checking an Item in a Set
print("Is \"Apple\" in Phone Companies Set: ", "Apple" in phoneCompanies)
print("Is \"Motorola\" in Phone Companies Set: ", "Motorola" in phoneCompanies)

#Adding an Item to a Set
phoneCompanies.add("Motorola")
print("Phone Companies Set after adding Motorola:", phoneCompanies)

phoneCompanies.update(["Sony", "LG"])
print("Phone Companies Set after adding Sony and LG:", phoneCompanies)

#Removing an Item from a Set
phoneCompanies.remove("Nokia")
print("Phone Companies Set after removing Nokia:", phoneCompanies)

print("Popped item:", phoneCompanies.pop())

#Clearing a Set
alphabetSet = {"A", "B", "C", "D", "E"}
print("Alphabet Set before clearing:", alphabetSet)
alphabetSet.clear()
print("Alphabet Set after clearing:", alphabetSet)

del alphabetSet #Accessing alphabetSet after deletion will raise an error

#Converting a List to a Set
foodList = ["Pizza", "Burger", "Pasta", "Pizza", "Burger"]
foodSet = set(foodList)
print("Food List:", foodList)
print("Food Set:", foodSet)

#Joining Sets
otherFoods = {"Sushi", "Tacos", "Pasta"}
allFoods = foodSet.union(otherFoods)
print("All Foods Set:", allFoods)

num1 = {1, 2, 3, 4, 5}
num2 = {4, 5, 6, 7, 8}
num1.update(num2)
print("Numbers Set after updating with another set:", num1)

#Finding Intersection and Difference, Symmetric Difference of Sets
print("Intersection of Numbers Sets:", num1.intersection(num2))
print("Difference of Numbers Sets:", num1.difference(num2))
print("Difference of Numbers Sets:", num2.difference(num1))
print("Symmetric Difference of Numbers Sets:", num1.symmetric_difference(num2))
print("Symmetric Difference of Numbers Sets:", num2.symmetric_difference(num1))

#Checking Subset and Superset
print("Is num2 a subset of num1: ", num2.issubset(num1))
print("Is num1 a superset of num2: ", num1.issuperset(num2))
print("Is num1 a subset of num2: ", num1.issubset(num2))
print("Is num2 a superset of num1: ", num2.issuperset(num1))

#Joint And Disjoint Sets
setA = {1, 2, 3}
setB = {3, 4, 5}
print("Are setA and setB disjoint: ", setA.isdisjoint(setB))
setC = {6, 7, 8}
print("Are setA and setC disjoint: ", setA.isdisjoint(setC))


#Clearing a Set
setD = {9, 10, 11}
print("Set D before clearing:", setD)
setD.clear()
print("Set D after clearing:", setD)