#Declaring And Invoking Functions
def Greeting1():
    print("Hello World")
Greeting1()

#A Function With Parameters
def Greeting2(name):
    print(f"Hello {name}")
Greeting2("Ali")

#A Function With Return
def Greeting3(name):
    print(f"Hello {name}")
    return "Hello World"
print(Greeting3("John"))

#A Function With Multiple Parameters
def Greeting4(firstName, lastName):
    return f"Hello {firstName} {lastName}"

print(Greeting4("John", "Doe"))

#Functions With Defualt Parameters And Calling Function With Keyword Arguments
def generateFullName(firstName = "John", lastName = "Doe"):
    fullName = firstName + " " + lastName
    return fullName
print(generateFullName("John", "Doe"))
print(generateFullName(lastName = "Malik"))
print(generateFullName())

#Function with Arbritrary Number Of Parameters
def sumOfNums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sumOfNums(1, 2, 3, 4, 5))

#Function With Default Parameters And Arbritrary Number Of Parameters
def sumOfNums2(num1, num2, num3, *nums):
    total = num1 + num2 + num3
    for num in nums:
        total += num
    return total

print(sumOfNums2(1, 2, 3, 4, 5, 6, 7, 7, 7, 7))

#Dictionary Unpacking In Functions
myDict = {"firstName": "Ammar", "lastName": "Malik"}
def generateFullName3(firstName, lastName):
    fullName = firstName + " " + lastName
    return fullName
print(generateFullName3(**myDict))


#Function With Arbritrary Number Of Keyword Arguments
def generateFullName2(**partOfName):
    orderOfName = ["firstName", "middleName", "lastName"]
    fullName = []
    for key, value in partOfName.items():
        if key in orderOfName:
            indexOfOrder = orderOfName.index(key)
            fullName.insert(indexOfOrder, value)
    return " ".join(fullName)

print(generateFullName2(firstName = "John", lastName = "Doe"))
print(generateFullName2(middleName = "Michael", lastName = "Doe", firstName = "John"))


#Function as a Parameter In Another Function
def add(num1, num2):
    return num1 + num2

def add2(num1, num2, func):
    return func(num1, num2)

print(add2(2, 3, add))

#Counting Even And Odd Numbers
def countEvenOdd(num):
    evenNum = 0
    oddNum = 0
    for i in range(1, num+1):
        if i % 2 == 0:
            evenNum += 1
        else:
            oddNum += 1
    return f"Even Numbers: {evenNum}, Odd Numbers: {oddNum}"

print(countEvenOdd(103))

# Create List Using Arbritrary Number Of Parameters
def createList(*nums, requiredList = []):
    for num in nums:
        requiredList.append(num)
    return requiredList

print(createList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

     