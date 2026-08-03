#Creating a list of fruits and Accessing its Elements
Fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew"]
print("Fruits List:", Fruits)

print("First Fruit:", Fruits[0])
print("Second Last Fruit:", Fruits[-2])
print("Last Fruit:", Fruits[len(Fruits)-1])

#Unpacking Items
apple, banana, *rest , grape, honeydew = Fruits
print("Apple:", apple)
print("Banana:", banana)
print("Rest:", rest)
print("Grape:", grape)
print("Honeydew:", honeydew)

#Slicing Items
print("Fruits from index 1 to 3:", Fruits[1:4])
print("Every Second Fruit:", Fruits[::2])
print(Fruits[-5:-2])

#Modifying List Elements
Fruits[4] = "Watermelon"
Fruits[-3] = "Pineapple"
Fruits[len(Fruits) - 1] = 'Lime'
print("Modified Fruits List:", Fruits)

#Checking if an Item Exists in the List
print("Is \"Banana\" in Fruits List: ", "Banana" in Fruits)
print("Is \"Mango\" in Fruits List: ", "Mango" in Fruits)

#Adding, Inserting and Removing Items
Fruits.append("Mango")
print("Fruits List after Adding Mango:", Fruits)
Fruits.insert(2, "Papaya")
print("Fruits List after Inserting Papaya at index 2:", Fruits)
Fruits.remove("Date")
print("Fruits List after Removing Date:", Fruits)
Fruits.pop(1)
print("Fruits List after Popping index 1:", Fruits)
del Fruits[2]
print("Fruits List after Deleting index 3:", Fruits)

#Clearing List Items
Alphabets = ["A", "B", "C"]
print("Alphabets List before Clearing:", Alphabets)
Alphabets.clear()
print("Alphabets List after Clearing:", Alphabets)

#Copying and Joining Lists
Vegetables = ["Carrot", "Spinach", "Potato"]
VegetablesCopy = Vegetables.copy()
print("Copied Vegetables List:", VegetablesCopy)

FruitsAndVegetables = Fruits + Vegetables
print("Fruits and Vegetables List:", FruitsAndVegetables)

OtherVegetables = ["Tomato", "Cucumber"]
FruitsAndVegetables.extend(OtherVegetables)
print("Fruits and Vegetables List after Extending with Other Vegetables:", FruitsAndVegetables)

#Counting and Finding Items in a List
numbers = [1, 2, 3, 4, 5, 1, 2, 3]
print("Count of 1 in numbers List:", numbers.count(1))
print("Index of 4 in numbers List:", numbers.index(4))

#Reversing and Sorting Lists
carList = ["Toyota", "Honda", "Ford", "Chevrolet"]
carList.reverse()
print("Reversed Car List:", carList)
print("Normal Car List:", carList[::-1])

numbersList = [5, 2, 9, 1, 5, 6]
numbersList.sort()
print("Sorted Numbers List:", numbersList)

carList.pop()
print("Car List after Popping index 0:", carList)

#Excercise: Splitting a List into Two Halves and Finding the Middle Term(s)
countries = ["USA", "Canada", "Germany", "France", "Japan", "India", "Brazil", "China", "Russia", "Australia", "South Africa", "Mexico", "Italy", "Spain", "Netherlands", "Sweden", "Norway", "Finland", "Denmark", "Belgium"]
print("Length of Countries List:", len(countries))
if len(countries) % 2 == 0:
    midIndex = len(countries) // 2
    middleTerms = [countries[midIndex - 1], countries[midIndex]]
    print("Middle Terms of Countries List:", middleTerms)
    FirstHalf = countries[:midIndex]
    SecondHalf = countries[midIndex:]
    print("First Half of Countries List:", FirstHalf)
    print("Second Half of Countries List:", SecondHalf)
else:
    midIndex = len(countries) // 2
    middleTerm = countries[midIndex]
    print("Middle Term of Countries List:", middleTerm)
    FirstHalf = countries[:midIndex + 1]
    SecondHalf = countries[midIndex + 1:]
    print("First Half of Countries List:", FirstHalf)
    print("Second Half of Countries List:", SecondHalf)
