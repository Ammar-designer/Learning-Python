#Creating a Tuple
laptopCompanies = ("Dell", "HP", "Lenovo", "Apple", "Asus")
print("Laptop Companies Tuple:", laptopCompanies)
print("Length of Laptop Companies Tuple:", len(laptopCompanies))
print("First Laptop Company:", laptopCompanies[0])
print("Last Laptop Company:", laptopCompanies[-1])
print("First Three Laptop Companies:", laptopCompanies[0:3])
print("Every Second Laptop Company:", laptopCompanies[::2])
print("Last Two Laptop Companies:", laptopCompanies[-2:])

#Converting Tuple to List and Modifying Elements
laptopCompaniesList = list(laptopCompanies)
laptopCompaniesList[1] = "Acer"
laptopCompanies = tuple(laptopCompaniesList)
print("Modified Laptop Companies Tuple:", laptopCompanies)

#Checking Items in a Tuple
print("Is \"Apple\" in Laptop Companies Tuple: ", "Apple" in laptopCompanies)
print("Is \"MSI\" in laptop Companies Tuples: ", "MSI" in laptopCompanies)

#Joining Tuples
laptopCompanies2 = ("MSI", "Razer", "Samsung", "LG")
allLaptopCompanies = laptopCompanies + laptopCompanies2
print("All Laptop Companies Tuple:", allLaptopCompanies)

#Unpacking a Tuple
dell, hp, lenovo, apple, asus , *rest = allLaptopCompanies
print("Unpacked Values:")
print("Dell:", dell)
print("HP:", hp)
print("Lenovo:", lenovo)
print("Apple:", apple)
print("Asus:", asus)
print("Rest:", rest)

#Deleting a Tuple
del laptopCompanies2 #Accessing laptopCompanies2 after deletion will raise an error
