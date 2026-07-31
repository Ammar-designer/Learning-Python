#String Concatenation
firstName = "Arthur"
lastName = "Morgan"
space = ""
fullName = firstName + space + lastName
print(fullName)

#String Formatting Using % Operator
radius = 10
PI = 3.14
areaOfCircle = PI * (radius ** 2)
print("Area of Circle with radius %d is %.2f" %(radius, areaOfCircle))

#String Formatting Using .format() Method
length = 10
width = 5
areaOfRectangle = length * width
print("Area of Rectangle with length {} and width {} is {}".format(length, width, areaOfRectangle))

#String Formatting Using f-Strings
height = 1.75
side = 5
areaOfTriangle = 0.5 * side * height
print(f"Area of Triangle with height {height} and side {side} is {areaOfTriangle}")

#String as Sequence of Characters
language = "Python"
p,y,t,h,o,n = language
print(p, y, t, h, o, n)
print(language[0], language[1])
lastIndex = len(language) - 1
print(language[lastIndex])
SecondToLastLetter = language[-2]
print(SecondToLastLetter)

#String Slicing
name = "Arthur Morgan"
print(name[0:6]) #Arthur , From index 0 to 5, 1 Less Than The Second Index
print(name[7:]) #Morgan , Start At index 7, Second Left Empty Means Till End

print(name[-3:])#Last Three
print(name[3:])#All Except First Three

print(name[0:6:2])

print(name[::-1])

#String Methods
challenge = 'thirty days of python'
print(challenge.capitalize())
print(challenge.lower())
print(challenge.count("y"))
print(challenge.count("y", 2, 6)) #Count "y" from index 2 to 5
print(challenge, "Endswith \"on\" or Not:" ,challenge.endswith("on"))
print(challenge, "Endswith \"tion\" or Not:", challenge.endswith("tion"))
print(challenge, "StartsWith \"th\" or Not:" ,challenge.startswith("th"))
print(challenge, "StartsWith \"python\" or Not:", challenge.startswith("python"))
challengeWithTabs = 'thirty\tdays\tof\tpython'
print(challengeWithTabs.expandtabs())
print(challengeWithTabs.expandtabs(20))
print(challenge.find("y", 7, 14)) #Find "y" from index 7 to 13
print(challenge.find("y")) #Find First "y" in the String
print(challenge.rfind("y")) #Find Last "y" in the String
print(challenge.index("y")) #Find "y" from index 7 to 13
print(challenge.rindex("y")) #Find Last "y" in the String
alNumChallenge = 'ThirtyDaysofPython123' #Space is Not AlphaNumeric
alphaChallenge = 'ThirtyDaysofPython'
print(challenge, "is AlphaNumeric: " ,challenge.isalnum())
print(alNumChallenge, "is AlphaNumeric:" , alNumChallenge.isalnum())
print(alphaChallenge, "is Alpha: ", alphaChallenge.isalpha())
print(challenge, "is Alpha: ", challenge.isalpha())
num = "2134"
numWithUnicode = "2134 \u2B16 "
print(num, "is Decimal: " , num.isdecimal())
print(challenge, "is Decimal: " ,challenge.isdecimal())
print(num, "is Digit: " , num.isdigit())
print(numWithUnicode , "is Digit: " , num.isdigit()) # Also Includes UNICODE Charcters
print(num, "is Numeric: " , num.isnumeric())
print(numWithUnicode , "is Numeric: " , num.isnumeric()) # Also Includes UNICODE Charcters
print(num, "is Identifier: " , num.isidentifier())
print(alNumChallenge, "is Identifier: " ,alNumChallenge.isidentifier())
print(challenge, "is Lower: " ,challenge.islower())
print(alphaChallenge, "is Lower: ", alphaChallenge.islower())
print(challenge, "is Upper: " ,challenge.isupper())
print(alphaChallenge.upper(), "is Upper: ", alphaChallenge.upper().isupper())
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
print(' '.join(web_tech))
print('_'.join(web_tech))
print(challenge.strip("thniryo"))
print(challenge.replace("python", "coding"))
print(challenge.split())
challengeWithCommas = 'thirty,days,of,python'
print(challengeWithCommas.split(","))
print(challenge.swapcase())
print(challenge.title())