"""
Welcome on this memo Python file
Last update 21/05/2020

As you can see, 3 quotes are useful to comment multiple lines ;-)
"""

# The # caracter is used to comment only one line

"""
Installation :
brew install python # To install python
pip install numpy # To install numpy module (curves)
pip install pillow (image)
"""

# Variable and main types
number=10   # Integer number
decimal=3.14 # Decimal number
prenom="Arnaud" # String
isTrue=True # Boolean
integers = [40, 60, 120] # Array of Integer

# Main Python functions to start
# To write message on screen
print("Hello World !")

# To declare you own function
def printMessage(message):
    print(message)

# To use it
printMessage("Hello " + prenom)

# To return a result from a function
def addition(a, b):
    return a+b

# To call your addition function
result=addition(4,6)
print(result)

# Conditions
a = 10
b = 6
# == equal
# != not equal
# >, <, >=, <= for less, greater, ...
if a > b:
    # str() is used to cast (convert) the int as str
    print(str(a) + " is greater than " + str(b))
else:
    print(str(a) + " is less than " + str(b))

# Loop while i is < or equal at 6
print("Loop with \"while\"") # We use \ to escape the quote caracter
i = 1
while i <= 6:
  print(i)
  i += 1

# Loop in range of i=10 to 20
print("Loop \"for\" with range() :") # We use \ to escape the quote caracter
for i in range(10,20):
    print(i)

print("Loop \"for\" on an Array :") # We use \ to escape the quote caracter
for i in integers:
    print(i)

# How to generate random number
import random
print("display random Integer number between 1 and 100")
x=random.randint(1, 100)
print("random x=",x)
# How to use Array
brandsCars = ["Renault", "Peugeot", "Citroen"] # Array of String

# Print the first value of the Array
print("Array samples :")
print(brandsCars[0])
# Print the length of the Array
print(len(brandsCars))
# To add an element in the Array
brandsCars.append("Dacia")
# To delete an element of the Array by his index
# Delete the second element of the Array : "Peugeot"
brandsCars.pop(1)
# To delete an element of the Array by his value, delete the 1st element with the value
# Delete the brands "Citroen"
brandsCars.remove("Citroen")
# Display the contain of the array after our operations
for brand in brandsCars:
    print(brand)

# How to use dictionnary
# Declare a dictionnary
print("Dictionnary samples :")
person = {
  "firstName": "Laura",
  "lastName": "DUHAMEL",
  "year": 2003
}

# print the firstName
firstName=person["firstName"]
print("firstName=" + firstName)
# or use get() function
lastName=person.get("lastName")
print("lastName=" + lastName)

# change the value of item
person["year"]=2000
print("year=", person["year"])

# Add Item in dictionnary
print("Add gender Item")
person["gender"]="female"
print(person)

familly={"Dad" : {
            "firstName": "Arnaud",
            "lastName": "DUHAMEL",
            "year": 1976
        },
        "Mum" : {
            "firstName": "Cristina",
            "lastName": "DUHAMEL",
            "year": 1971
        },
        "Sister" : {
            "firstName": "Charlotte",
            "lastName": "DUHAMEL",
            "year": 2003
        }
}

print("My familly : ", familly)
print("Mu mum : ", familly.get("Mum"))

# How to get information from user
print("input sample :")
username = input("Enter your name :")
print("Hello " + username + "!")

# How to use Exceptions
print("Exception sample, we try do divide 87 by 0")
try:
  i = 87/0
  f.write("i=" + str(i))
except:
  print("Division by zero !")
finally:
  print("Result is infinity")

# How to use files
print("Sample with file")
try:
    myFile = open("memo.txt") # Open the file
except FileNotFoundError:
    print("File memo.txt doesn't exist, we create it ")
else:
    print("The file memo.txt already exist, are you sure to continue ? The file will be overwritten !")
    response=input("Continue ? (Y/N) :")
    if(response!="Y" and response!="y"):
        myFile.close()
        print("program execution interrupted")
        exit()
    else:
        myFile.close()

myFile = open("memo.txt", "w") # Open the file in writing mode
myFile.write("First line of the file")  # Write the first line of the file
myFile.close() # Close the file
print("Open the file memo.txt and display his contain")
myFile = open("memo.txt","r")  # Open the file in read mode
print(myFile.read())
myFile.close() # Close the file
myFile = open("memo.txt","a")  # Open the file in append mode
myFile.write("Seconde line of the file")
myFile.close() # Close the file
myFile = open("memo.txt","r")  # Open the file in read mode
print(myFile.read())
myFile.close() # Close the file
import os # To delete file, we need to import os module
os.remove("memo.txt")

