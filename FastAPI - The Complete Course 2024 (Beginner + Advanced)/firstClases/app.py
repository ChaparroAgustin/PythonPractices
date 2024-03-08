#lists, sets and tuples 

my_set = {1,2,3,4,5,6}# the only thing that we cant do is access by index, for example my_set[2], this return an error 

#print(my_set[2])    this is to check the error 

my_list = [1,2,3,4,5] #we can do anything

my_tuple = (1,2,3,4,5,6)# tuples are not changiable, we can not add, update or delete from them 


#Task to learn 
# Crate a list of 5 animals called "zoo" and append an animal, delete the firts one , print all the animals, and print only the first 3


zoo = ["elefant", "lion", "tiger", "horse", "zebra"]

zoo.append("cheeta")


zoo.pop(0)


# print(zoo[0:3])



#-----o------

# - Create a variable grade holding an integer between 0 - 100

# - Code if, elif, else statements to print the letter grade of the number grade variable

# Grades:

# A = 90 - 100

# B = 80 - 89

# C = 70-79

# D = 60 - 69

# F = 0 - 59

grade = 22
# if grade > 100:
#     print("el numero debe ser menor a 100")
# elif grade > 0 and grade < 60:
#     print("F")
# elif grade > 59 and grade < 70:
#     print("D")
# elif grade > 69 and grade < 80:
#     print("C")
# elif grade > 79 and grade < 90:
#     print("B")
# else:
#     print("A")


#------------o----------
    



userDiccionary = {
    'username':'achaparro',
    'name': 'Agustin',
    'age': 32
}
# print(userDiccionary["username"])
# userDiccionary["married"] = True
# print(userDiccionary)

# Based on the dictionary:

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
# - Create a for loop to print all keys and values

# - Create a new variable vehicle2, which is a copy of my_vehicle

# - Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4

# - Delete the mileage key and value from vehicle2

# - Print just the keys from vehicle2


# for x, y in my_vehicle.items():
#     print(x , y )

# vehicule2 = my_vehicle.copy()

# vehicule2["number_of_tires"] = 4

# vehicule2.pop("mileage")
# for i in vehicule2:
#     print(i)



#-----------o-----
#funtions

# - Create a function that takes in 3 parameters(firstname, lastname, age) and

# returns a dictionary based on those values

def userDictionary (firstname, lastname,age):
    createUserDictionary = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return createUserDictionary

solutionDictionary = userDictionary("agustin","chaparro",32)
# print(solutionDictionary)

#--------o----------
#Imports

from funtionToImport import calculateHomaework

homeworkAssigmentArg = {
    'homework1':85,
    'homework2':100,
    'homework3':81
}

# calculateHomaework(homeworkAssigmentArg)

# ---0-----------

# POO

from studentClass import Student, collegeStudent

student1 = collegeStudent("agustin", "chaparro", "technical support")

# print(student1.fullnameWithMajor())
