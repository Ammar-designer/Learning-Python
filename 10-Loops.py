# Creating A While Loop
count = 1
while count <= 5:
    print(count, end=" ")
    count += 1

# Creating A While Loop With An Else Statement
count = 10
while count >= 0:
    print(count)
    count -= 1
else:
    print("Reached Zero")

# Break and Continue in While Loops
names = ["John", "Paul", "George", "Ringo"]
while True:
    name = "John"
    if name in names:
        print(f"{name} is in the list")
        break
    else:
        print(f"{name} is not in the list")

num = 10
while num > 0:
    if num in [2, 5, 8]:
        num -= 1
        continue
    print(num)
    num -= 1

# Creating A For Loop
for i in range(1, 6):
    print(i)

# Creating A For Loop With A Step
for i in range(1, 11, 2):
    print(i)

# For Loop on Strings, Tuples/Lists and Dictionaries, Sets
carBrand = "Ford"
for letters in carBrand:
    print(letters, end=" ")
print()

cars = ("Porsche", "Chevy", "BMW")
for car in cars:
    print(car)

laptop = {"Brand": "Dell", "Model": "XPS 13", "Year": 2021}
for key in laptop:
    print(key)

for key, value in laptop.items():
    print(f"{key}: {value}")

numbers = {1, 2, 3, 4, 5}
for number in numbers:
    print(number)

# Break And Continue in For Loops
numvalues = [1, 2, 3, 4, 5]
requiredNum = 2
for num in numvalues:
    if num == requiredNum:
        print(f"{num} is in the list")
        break

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print("Next number should be ", number + 1) if number != 5 else print("loop's end")

#For Else Statement
for i in range(1, 6):
    print(i)
else:
    print("Loop's end")

