#if and else statement
num = 10
if num > 5:
    print(num, " is greater than 5")
else:
    print(num , " is not greater than 5")

#if, elif and else with and Logical Operator statement
a = 10
b = 20
c = 40
if a > b and a > c:
    print(a, " is the greatest number")
elif b > a and b > c:
    print(b, " is the greatest number")
else:
    print(c, " is the greatest number")

#if , else with or Logical Operator
user = "Admin"
access_level = 3
if user.lower() == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')

#Short hand if else statement
x = 5 
print("Positive") if x > 0 else print("Negative")

#Nested Condtions
a = 9
if a > 0:
    if a % 2 == 0:
       print(a, "Is a Positive Even Number")
    else:
        print(a, "Is a Positive Odd Number")
elif a == 0:
    print(a, "Is Equal to Zero")
else:
    if a % 2 == 0:
        print(a, "Is a Negative Even Number")
    else:
        print(a, "Is a Negative Odd Number")