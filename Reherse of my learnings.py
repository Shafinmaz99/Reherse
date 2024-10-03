# This program is my first one

#print("Hello world!") # First line
#print("This is my first program.")
#print("This program prints three lines.")

#print("He said: 'Hello World!' and kept on coding.")
#print("He said: \"Hello World!\" and kept on coding.")
# print("He said: \"Hello World!\" \n and kept on coding.")

# print ("Hello" + "user!")

#input("What is your name?")

#print("Welcome " + input("What is your name? ") + "!")

#Print("Hello"[0])

#print("Hello"[0:2])

#print ("123" + "456")

# Firstname = input("What is your firstname: ")
# Lastname = input("What is your last name: ")
# #print("Hello " + Firstname + ". " + Lastname)
# print("Hello", Firstname, Lastname)

# Sentence = "Finding a substring."

# print(Sentence[1]) finding the letter, it starts with 0

# print(Sentence[-2]) finding the letter, from the back

# print(Sentence[2:9]), finding the letter, starts from 2 ends with 9

# print(Sentence[:9]) finding the letters 0-9

# print(Sentence[-9:-2]) finding from backwards

# print(Sentence[0:9:3]) skips 2 letters not the whole sentence, particular one

# print(Sentence[::3]) Skips 2 letter

# print(Sentence[::-1]) reverse the sentence

# print(123 + 456) Integer

# Check the mobile images

# calcen = len("Calculate the number of characters")

# print(calcen) Calculate the entire number tof the characters, starts with 1

# print(calcen)
# print(type(calcen))

# Num1 = float(10)
# print(type(Num1))

# Num2 = float(10)
# Num3 = 3 + Num2

# print(Num3)

# print(5 * 3 - 4/ 2 + 2)
# print (5 * 3 - 4 / (2+2) )

# from operator import mod
# print(mod(9, 2))

# print(7 /2 ) entire calculation, with points
# print(int (7/2)) whole number no points cause its integer
# print(7%2) to get the remainder

# print(6%2) even number, no remainder

# Name = "Dhruba"
# Age = 25

# Formattedstring = "My name is %s and  I am %d years old." % (Name, Age)

# print(Formattedstring)


# print("{:.2f}" .format(RoundThis))

# RoundThis = 8/3
# Number = ("{:.2f}" .format(RoundThis))
# print("My name is %s and I am %d years old. The number is ")) Couldn't understand

# Easycalc = 0
# Easycalc = Easycalc + 1
# Easycalc += 1
# Easycalc -=1
# Easycalc *=1
# Easycalc /=1

# PI = 3.1416
# Radius = int(input("What is the radius of the cylinder?"))
# Height = int(input("What is the height of your cylinder?"))
# volumeofcylinder = Radius**2*PI*Height

# print(f"The Volume of your cylinder is: {volumeofcylinder}")

# print("Welcome to the movement app!")
# Temperature = int(input("What is temperature of you IoT CPU?"))

# if Temperature >= 80:
#     print("Too hot!")
# else:
#     print("Cool")
    # if i want the temperature i equal to 80 we nned to use two = signs

# print("Welcome to the movement app!")
# Temperature = int(input("What is temperature of you IoT CPU?"))
# Temperature = 80

# if Temperature == 80:
#     print("Too hot!")
# else:
#     print("Cool")

#The following program checks if a number is odd or even

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print(f"{num} is Even")
# else:
#     print(f"{num} is Odd")


# Temperature = int(input("What is the Temperature of your cpu?"))

# if Temperature > 90:
#     print("The CPU is fried. Get Your Fire Extinguisher")

# if Temperature > 80:
#     print("Warning! Temperature is too High")
# else:
#     print("Everything is cool!")


# name1 = input("Enter the first name: ")
# name2 = input("Enter the second name: ")
    
# if len(name1) > len(name2):
#     print(f"The first name '{name1}' is longer than the second name '{name2}'.")
# elif len(name1) < len(name2):
#     print(f"The first name '{name1}' is shorter than the second name '{name2}'.")
# else:
#     print(f"The first name '{name1}' is equal in length to the second name '{name2}'.")


# This code is not working, i am trying another

# Town = "Lahti"
# Street = "Mukkulankatu"
# Building = 19

# if (Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
#     print("You are at LAB")
# elif(Town == "Lahti" and (Street != "Mukkulankatu" or Building != 19)):
#     print("You are in the correct town, but you need to check your address")
# else:
#     print("You are completely lost.")

# Next one


# Town = input("Whcih town are you in right now?: ")
# Street = input("Which street are you in right now?: ")
# Building = int(input("Enter the building number you are seeing.: "))

# if (Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):

#     print("You are at LAB")

# elif (Town == "Lahti" and Street == "Mukkulankatu" and Building > 19):

#     print("You went too far.")

# elif (Town == "Lahti" and Street == "Mukkulankatu" and Building < 19):

#     print("You are not there yet.")

# elif (Town == "Lahti" and (Street != "Mukkulankatu" or Building != 19)):

#     print("You are in the correct town, but you need to check your address")
# else:
#     print("You are completely lost.")

# order the words in alphabetical order using conditionals

# word1 = input("Enter the first word: ")

# word2 = input("Enter the second word: ")

# word3 = input("Enter the third word: ")


# if word1 < word2 and word1 < word3:
#     if word2 < word3:
#         print(f"Alphabetical order: {word1}, {word2}, {word3}")
#     else:
#         print(f"Alphabetical order: {word1}, {word3}, {word2}")
# elif word2 < word1 and word2 < word3:
#     if word1 < word3:
#         print(f"Alphabetical order: {word2}, {word1}, {word3}")
#     else:
#         print(f"Alphabetical order: {word2}, {word3}, {word1}")
# else:
#     if word1 < word2:
#         print(f"Alphabetical order: {word3}, {word1}, {word2}")
#     else:
#         print(f"Alphabetical order: {word3}, {word2}, {word1}")